#!/usr/bin/env python3
"""Gera a matriz granular de Knowledge of e Skills in do guia SAA-C03.

As competências são obtidas das páginas oficiais em Markdown. O mapeamento de
evidências usa os capítulos, laboratórios, questões e checklists existentes na
branch, preservando uma trilha auditável até cada arquivo.
"""

from __future__ import annotations

import argparse
import csv
import io
import re
import sys
import unicodedata
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "02_Planejamento" / "Matriz_Competencias_Oficiais_SAA-C03.csv"
VALIDATION_DATE = "2026-08-01"
DOMAIN_WEIGHTS = {1: "30%", 2: "26%", 3: "24%", 4: "20%"}
DOMAIN_URLS = {
    domain: (
        "https://docs.aws.amazon.com/aws-certification/latest/"
        "solutions-architect-associate-03/"
        f"solutions-architect-associate-03-domain{domain}.md"
    )
    for domain in range(1, 5)
}
DOMAIN_HTML_URLS = {
    domain: url.removesuffix(".md") + ".html" for domain, url in DOMAIN_URLS.items()
}
EXPECTED_TASKS = {
    "1.1",
    "1.2",
    "1.3",
    "2.1",
    "2.2",
    "3.1",
    "3.2",
    "3.3",
    "3.4",
    "3.5",
    "4.1",
    "4.2",
    "4.3",
    "4.4",
}
DEFAULT_BLOCK = {
    "1.1": 21,
    "1.2": 22,
    "1.3": 11,
    "2.1": 14,
    "2.2": 24,
    "3.1": 5,
    "3.2": 16,
    "3.3": 8,
    "3.4": 23,
    "3.5": 19,
    "4.1": 11,
    "4.2": 3,
    "4.3": 8,
    "4.4": 24,
}
# Every expression below is a regular expression over normalized ASCII text.
# Word boundaries are intentional: the former substring matcher routed
# ``Outposts`` and ``costs`` to STS because both contain the letters ``sts``.
TASK_ROUTING_RULES: dict[str, tuple[tuple[tuple[str, ...], int], ...]] = {
    "2.1": (
        ((r"\bcompute, storage, networking, and database\b",), 18),
    ),
    "2.2": (
        ((r"\bmetrics? based on business requirements\b",), 14),
        ((r"\bsingle points? of failure\b",), 1),
        ((r"\blegacy applications?\b", r"\bnot built for the cloud\b"), 15),
        ((r"\bbasic networking concepts?\b", r"\broute tables?\b"), 22),
    ),
    "3.3": (
        ((r"\bdesigning database architectures?\b",), 18),
    ),
    "3.4": (
        ((r"\bplacement of resources\b", r"\bresource placement\b"), 22),
    ),
    "3.5": (
        ((r"\bdata ingestion patterns?\b", r"\bconfigurations? for ingestion\b", r"\bsizes? and speeds?\b"), 15),
        ((r"\bdata processing\b", r"\bemr\b"), 18),
    ),
    "4.4": (
        ((r"\bcontent delivery\b", r"\bcdn\b", r"\bcloudfront\b", r"\bedge caching\b"), 12),
        ((r"\bload balanc", r"\balb\b", r"\bnetwork load balancer\b"), 6),
        ((r"\bnat gateway", r"\bnat instance"), 22),
        ((r"\bdns\b", r"\bnetwork services\b"), 9),
        ((r"\bthrottl", r"\brate limit"), 17),
        ((r"\bbandwidth\b", r"\bdirect connect\b", r"\bvpn\b", r"\bnetwork connect"), 23),
        ((r"\bnetwork rout", r"\btopology\b", r"\bpeering\b", r"\btransit gateway\b"), 23),
        ((r"\bcost management\b", r"\bcost explorer\b", r"\bbudgets?\b", r"\bcost and usage report\b"), 25),
    ),
    "4.3": (
        ((r"\bmigrat.*database", r"\bdatabase schemas?\b"), 24),
        ((r"\bcost management\b", r"\bcost explorer\b", r"\bbudgets?\b", r"\bcost and usage report\b"), 25),
    ),
    "4.2": (
        ((r"\boutposts\b", r"\bhybrid compute\b"), 25),
        ((r"\bcompute utilization\b", r"\bcost-effective aws compute\b"), 25),
        ((r"\bcost management\b", r"\bcost explorer\b", r"\bbudgets?\b", r"\bcost and usage report\b"), 25),
    ),
    "4.1": (
        ((r"\bcost management\b", r"\bcost explorer\b", r"\bbudgets?\b", r"\bcost and usage report\b"), 25),
    ),
}
ROUTING_RULES: tuple[tuple[tuple[str, ...], int], ...] = (
    ((r"\bcontent delivery\b", r"\bcdn\b", r"\bcloudfront\b", r"\bglobal accelerator\b", r"\bedge accelerator"), 12),
    ((r"\bcost management\b", r"\bcost explorer\b", r"\bbudgets?\b", r"\bcost and usage report\b", r"\bcost allocation\b"), 25),
    ((r"\bdata analytics\b", r"\bvisualization\b", r"\bathena\b", r"\blake formation\b", r"\bquicksuite\b", r"\bdata lake\b", r"\bglue\b", r"\bparquet\b"), 19),
    ((r"\bcomprehend\b", r"\bpolly\b", r"\btranscribe\b", r"\btranslate\b", r"\brekognition\b", r"\btextract\b"), 19),
    ((r"\bdisaster recovery\b", r"\brpo\b", r"\brto\b", r"\bpilot light\b", r"\bwarm standby\b", r"\bactive-active\b"), 24),
    ((r"\bmigrat.*database", r"\bdatabase schemas?\b"), 24),
    ((r"\bfailover\b",), 10),
    ((r"\bmultiple aws accounts?\b", r"\bmultiple accounts?\b", r"\bcontrol tower\b", r"\bservice control policies?\b", r"\bscps?\b"), 21),
    ((r"\bfederat", r"\bidentity center\b", r"\bdirectory service\b", r"\brole-based\b", r"\baws sts\b", r"\bcross-account\b", r"\bresource polic"), 21),
    ((r"\bshared responsibility\b", r"\bglobal infrastructure\b", r"\bavailability zones?\b", r"\baws regions?\b"), 1),
    ((r"\broot users?\b", r"\biam users?\b", r"\bleast privilege\b", r"\bmulti-factor\b", r"\bmfa\b", r"\bauthorization model\b"), 1),
    ((r"\bapplication configuration\b", r"\bcredentials? security\b", r"\bsecrets manager\b"), 22),
    ((r"\bservice endpoints?\b", r"\bvpc endpoints?\b"), 23),
    ((r"\bshield\b", r"\bwaf\b", r"\bguardduty\b", r"\bmacie\b", r"\bddos\b", r"\bsql injection\b", r"\bthreat vectors?\b"), 22),
    ((r"\bports?\b", r"\bprotocols?\b", r"\bnetwork traffic\b", r"\bsegmentation\b", r"\bpublic subnets?\b", r"\bprivate subnets?\b", r"\bsecurity groups?\b", r"\bnetwork acls?\b"), 22),
    ((r"\bnat gateways?\b", r"\bnat instances?\b"), 22),
    ((r"\bcompliance\b", r"\baudit\b"), 20),
    ((r"\bencrypt", r"\bkms\b", r"\bkey management\b", r"\bencryption keys?\b"), 21),
    ((r"\bcertificate", r"\bacm\b", r"\btls\b"), 7),
    ((r"\bdata retention\b", r"\bclassification\b", r"\blifecycle\b", r"\bdata access\b", r"\bgovernance\b", r"\bbackups?\b", r"\bdata recovery\b"), 11),
    ((r"\bapi creation\b", r"\bapi gateway\b", r"\bworkflow orchestration\b", r"\bstep functions\b", r"\bcognito\b", r"\bthrottl"), 17),
    ((r"\bread replicas?\b", r"\brds proxy\b", r"\bproxy concepts?\b", r"\bdatabase connections?\b", r"\bdatabase capacity\b", r"\bdatabase engines?\b", r"\bdatabase replication\b"), 8),
    ((r"\bcaching\b", r"\belasticache\b"), 8),
    ((r"\bdynamodb\b", r"\bnon-relational\b", r"\bdatabase types?\b"), 17),
    ((r"\bmigrat.*containers?\b",), 15),
    ((r"\bcontainers?\b", r"\becs\b", r"\beks\b", r"\bfargate\b"), 16),
    ((r"\bevent-driven\b", r"\bqueuing\b", r"\bmessaging\b", r"\bpublish/subscribe\b", r"\bloose coupling\b", r"\bdecoupl", r"\bsqs\b", r"\bsns\b"), 14),
    ((r"\bload balancing\b", r"\bapplication load balancer\b", r"\balb\b"), 6),
    ((r"\bstorage types?\b", r"\bobject, file, block\b", r"\bebs\b", r"\befs\b", r"\bvolume types?\b", r"\bhdd\b", r"\bssd\b"), 5),
    ((r"\btransfer family\b", r"\bdata transfer\b", r"\btransfer(?:ring)? data\b", r"\bmigrat.*storage\b", r"\bhybrid storage\b", r"\bdatasync\b", r"\bstorage gateway\b"), 13),
    ((r"\bserverless\b", r"\blambda\b"), 17),
    ((r"\bworkload visibility\b", r"\bx-ray\b", r"\bobservability\b"), 20),
    ((r"\broute 53\b",), 10),
    ((r"\bimmutable infrastructure\b", r"\bautomation strategies\b", r"\binfrastructure integrity\b"), 25),
    ((r"\bstorage services?\b", r"\bstorage performance\b", r"\bstorage scale\b", r"\bstorage size\b"), 5),
    ((r"\bcompute services?\b", r"\binstance types?\b", r"\bresource type and size\b", r"\binstance famil"), 3),
    ((r"\bpurchasing options?\b", r"\bspot instances?\b", r"\breserved instances?\b", r"\bsavings plans?\b"), 3),
    ((r"\bscaling actions?\b", r"\bauto scaling\b", r"\belastic workloads?\b", r"\bscaling strategies?\b", r"\bhorizontal scaling\b", r"\bvertical scaling\b"), 7),
    ((r"\bstreaming\b", r"\bkinesis\b"), 15),
    ((r"\bnetwork topology\b", r"\bnetwork routes?\b", r"\bnetwork connection\b", r"\bdirect connect\b", r"\bprivatelink\b", r"\bvpn\b", r"\bbandwidth\b", r"\bpeering\b", r"\btransit gateway\b"), 23),
    ((r"\bdns\b", r"\bnetwork services\b"), 9),
    ((r"\bmulti-tier\b", r"\bthree-tier\b"), 18),
    ((r"\bpurpose-built\b", r"\bdistributed design\b", r"\bmicroservices?\b"), 18),
    ((r"\boutposts\b", r"\bhybrid compute\b"), 25),
)

ROUTING_SENTINELS = {
    "Hybrid compute options (for example, AWS Outposts)": ("4.2", 25),
    "NAT gateways (for example, NAT instance costs compared with NAT gateway costs)": ("4.4", 22),
    "Configuring appropriate network routes to minimize network transfer costs (for example, Region to Region, Availability Zone to Availability Zone, private to public, AWS Global Accelerator, VPC endpoints)": ("4.4", 23),
    "Determining strategic needs for content delivery networks (CDNs) and edge caching": ("4.4", 12),
    "Selecting an appropriate throttling strategy": ("4.4", 17),
    "Implementing visualization strategies": ("3.5", 19),
    "Failover strategies": ("2.2", 10),
    "AWS cost management tools with appropriate use cases (for example, AWS Cost Explorer, AWS Budgets, AWS Cost and Usage Report)": ("4.4", 25),
    "Decoupling workloads so that components can scale independently": ("3.2", 14),
    "Horizontal scaling and vertical scaling": ("2.1", 7),
    "Selecting the appropriate service for data migration to storage services": ("4.1", 13),
    "Determining the lowest cost method of transferring data for a workload to AWS storage": ("4.1", 13),
    "How to migrate applications into containers": ("2.1", 15),
    "Multi-tier architectures": ("2.1", 18),
    "Recommending appropriate compute, storage, networking, and database technologies based on requirements": ("2.1", 18),
    "Identifying metrics based on business requirements to deliver a highly available solution": ("2.2", 14),
    "Implementing designs to mitigate single points of failure": ("2.2", 1),
    "Using AWS services that improve the reliability of legacy applications and applications not built for the cloud (for example, when application changes are not possible)": ("2.2", 15),
    "AWS service endpoints": ("1.2", 23),
    "Designing database architectures": ("3.3", 18),
    "Determining the appropriate placement of resources to meet business requirements": ("3.4", 22),
    "Data ingestion patterns (for example, frequency)": ("3.5", 15),
    "Sizes and speeds needed to meet business requirements": ("3.5", 15),
    "Selecting appropriate compute options for data processing (for example, Amazon EMR)": ("3.5", 18),
    "Selecting appropriate configurations for ingestion": ("3.5", 15),
}
LAB_BLOCK_OVERRIDES = {
    "AWS service endpoints": 23,
    "AWS global infrastructure (for example, Availability Zones, AWS Regions, Amazon Route 53)": 6,
    "Secure application access": 22,
    "Data access and governance": 11,
    "Design principles for microservices (for example, stateless workloads compared with stateful workloads)": 18,
    "Multi-tier architectures": 18,
    "Designing database architectures": 18,
    "Determining the appropriate placement of resources to meet business requirements": 22,
    "Data ingestion patterns (for example, frequency)": 15,
    "Sizes and speeds needed to meet business requirements": 15,
    "Selecting appropriate compute options for data processing (for example, Amazon EMR)": 18,
    "Selecting appropriate configurations for ingestion": 15,
    "How to migrate applications into containers": 15,
    "When to use read replicas": 8,
    "Configuring read replicas to meet business requirements": 8,
    "Recommending appropriate compute, storage, networking, and database technologies based on requirements": 18,
    "Using purpose-built AWS services for workloads": 18,
    "AWS Managed Services (AMS) with appropriate use cases (for example, Amazon Comprehend, Amazon Polly)": 19,
    "Basic networking concepts (for example, route tables)": 23,
    "Proxy concepts (for example, Amazon RDS Proxy)": 8,
    "Service quotas and throttling (for example, how to configure the service quotas for a workload in a standby environment)": 17,
    "Immutable infrastructure": 25,
    "Determining automation strategies to ensure infrastructure integrity": 25,
    "Identifying metrics based on business requirements to deliver a highly available solution": 14,
    "Implementing designs to mitigate single points of failure": 6,
    "Using AWS services that improve the reliability of legacy applications and applications not built for the cloud (for example, when application changes are not possible)": 15,
    "Reviewing existing workloads for network optimizations": 23,
}
FIELDNAMES = [
    "domínio",
    "peso",
    "tarefa",
    "knowledge ou skill",
    "competência",
    "bloco",
    "capítulo",
    "seção",
    "comparação",
    "cenário resolvido",
    "laboratório",
    "questão fundamental",
    "questão integrada",
    "questão de múltipla resposta",
    "D+2",
    "D+7",
    "referência oficial",
    "data de validação",
    "status",
    "lacuna",
]
TOKEN_RE = re.compile(r"[a-z0-9][a-z0-9+./-]*")
CONCEPT_PATTERNS: dict[str, tuple[str, ...]] = {
    "access_control": (r"\baccess controls?\b", r"\bauthoriz", r"\bleast privilege\b", r"\bresource polic", r"\bacesso\b", r"\bpermisso", r"\bpoliticas?\b"),
    "identity": (r"\biam\b", r"\bidentity\b", r"\bidentidade\b", r"\bfederat", r"\bdirectory\b", r"\bdiretorio\b", r"\bmfa\b"),
    "multi_account": (r"\bmultiple accounts?\b", r"\bmulti-account\b", r"\bcross-account\b", r"\borganizations?\b", r"\bcontrol tower\b", r"\bscp\b", r"\bcontas?\b"),
    "global_infrastructure": (r"\bglobal infrastructure\b", r"\bavailability zones?\b", r"\baws regions?\b", r"\bmulti-az\b", r"\bregions?\b", r"\bzonas? de disponibilidade\b"),
    "shared_responsibility": (r"\bshared responsibility\b", r"\bresponsabilidade compartilhada\b", r"\bsecurity of the cloud\b", r"\bsecurity in the cloud\b", r"\bguest os\b", r"\bresponsabilidade da aws\b", r"\bresponsabilidade do cliente\b"),
    "security": (r"\bsecurity\b", r"\bsecure\b", r"\bseguranca\b", r"\bprotecao\b"),
    "application_security": (r"\bsecure application access\b", r"\bapplication security\b", r"\blayered application.*defen", r"\bwaf\b", r"\bfirewall manager\b", r"\bacesso seguro.*aplic", r"\bseguranca.*aplic"),
    "credentials": (r"\bcredentials?\b", r"\bsecrets?\b", r"\bcredenciais?\b", r"\bsegredos?\b", r"\bparameter store\b"),
    "endpoint": (r"\bendpoints?\b", r"\bprivate access\b", r"\bprivatelink\b", r"\bpontos? de extremidade\b"),
    "network_security": (r"\bsecurity groups?\b", r"\bnetwork acls?\b", r"\bnacls?\b", r"\bports?\b", r"\bprotocols?\b", r"\bsegmentation\b", r"\bsubnets?\b", r"\bgrupos? de seguranca\b"),
    "threat": (r"\bguardduty\b", r"\bmacie\b", r"\bshield\b", r"\bwaf\b", r"\bddos\b", r"\bsql injection\b", r"\bthreat\b", r"\bameaca\b"),
    "encryption": (r"\bencrypt", r"\bcriptograf", r"\bkms\b", r"\bkey management\b", r"\bchaves?\b"),
    "certificate": (r"\bcertificates?\b", r"\bcertificados?\b", r"\bacm\b", r"\btls\b", r"\bhttps\b"),
    "compliance": (r"\bcompliance\b", r"\baudit", r"\bconformidade\b", r"\bartifact\b"),
    "governance": (r"\bgovernance\b", r"\bclassification\b", r"\bgovernanca\b", r"\bclassificacao\b", r"\bdata access\b"),
    "backup_recovery": (r"\bbackups?\b", r"\brecovery\b", r"\brestore\b", r"\bsnapshots?\b", r"\brecuperacao\b", r"\brestaur"),
    "lifecycle_retention": (r"\blifecycles?\b", r"\bretention\b", r"\barchive\b", r"\btiering\b", r"\bstorage tiers?\b", r"\bciclo de vida\b", r"\bretencao\b", r"\barquiv"),
    "replication": (r"\breplication\b", r"\breplicas?\b", r"\breplicacao\b"),
    "api": (r"\bapi gateway\b", r"\brest api\b", r"\bgraphql\b", r"\bappsync\b", r"\bapi\b"),
    "cache": (r"\bcach", r"\belasticache\b", r"\bredis\b", r"\bmemcached\b"),
    "microservices": (r"\bmicroservices?\b", r"\bmicroservicos?\b", r"\bstateless\b", r"\bstateful\b"),
    "event_driven": (r"\bevent-driven\b", r"\beventos?\b", r"\beventbridge\b"),
    "scaling": (r"\bscal", r"\bauto scaling\b", r"\belastic\b", r"\bescal"),
    "edge_delivery": (r"\bcontent delivery\b", r"\bcdn\b", r"\bcloudfront\b", r"\bglobal accelerator\b", r"\bedge\b"),
    "container": (r"\bcontainers?\b", r"\becs\b", r"\beks\b", r"\bfargate\b", r"\bconteiner"),
    "load_balancing": (r"\bload balanc", r"\balb\b", r"\bnlb\b", r"\bgwlb\b", r"\bbalanceador"),
    "multi_tier": (r"\bmulti-tier\b", r"\btres camadas\b", r"\bthree-tier\b", r"\bweb tier\b", r"\bwebsite serverless\b", r"\barquitetura serverless\b", r"\bserverless architecture\b"),
    "messaging": (r"\bqueu", r"\bmessag", r"\bpublish/subscribe\b", r"\bloose coupling\b", r"\bdecoupl", r"\bsqs\b", r"\bsns\b", r"\bfilas?\b", r"\bmensageria\b", r"\bdesacopl"),
    "serverless": (r"\bserverless\b", r"\blambda\b", r"\bsem servidor\b"),
    "storage": (r"\bstorage\b", r"\barmazenamento\b", r"\bs3\b", r"\bebs\b", r"\befs\b", r"\bfsx\b", r"\bobject\b", r"\bblock\b", r"\bfile\b"),
    "storage_services": (r"\bstorage services?\b", r"\bs3\b", r"\bebs\b", r"\befs\b", r"\bfsx\b", r"\bservicos? de armazenamento\b"),
    "hybrid_storage": (r"\bhybrid storage\b", r"\bstorage gateway\b", r"\bfile gateway\b", r"\bvolume gateway\b", r"\btape gateway\b", r"\barmazenamento hibrido\b"),
    "storage_access": (r"\bstorage access patterns?\b", r"\brequester pays\b", r"\bbatch uploads?\b", r"\bindividual uploads?\b", r"\bpadroes? de acesso.*armazenamento\b"),
    "storage_sizing": (r"\bstorage size\b", r"\bvolume size\b", r"\bcorrect storage size\b", r"\bsizing decision\b", r"\bprojected usage\b", r"\bheadroom\b", r"\btamanho.*(?:storage|volume|armazenamento)\b", r"\bdimensionamento.*capacidade\b"),
    "storage_types": (r"\bstorage types?\b", r"\bobject,? file,? block\b", r"\bblock storage\b", r"\bvolume types?\b", r"\bhdd\b", r"\bssd\b", r"\bobjeto\b", r"\barquivo\b", r"\bbloco\b"),
    "workflow": (r"\bworkflow\b", r"\bstep functions\b", r"\borquestr"),
    "purpose_built": (r"\bpurpose-built\b", r"\bproposito especifico\b", r"\bneptune\b", r"\bdocumentdb\b", r"\bkeyspaces\b", r"\btimestream\b", r"\bqldb\b"),
    "network": (r"\bnetwork\b", r"\bvpc\b", r"\brede\b", r"\bsubnet\b", r"\bcloudfront\b", r"\bapi gateway\b", r"\bload balanc", r"\broute 53\b"),
    "disaster_recovery": (r"\bdisaster recovery\b", r"\bdr\b", r"\brpo\b", r"\brto\b", r"\bpilot light\b", r"\bwarm standby\b", r"\brecuperacao de desastre\b"),
    "distributed": (r"\bdistributed\b", r"\bdistribuid"),
    "failover": (r"\bfailover\b", r"\bactive-passive\b", r"\bsecondary\b"),
    "immutable": (r"\bimmutable\b", r"\bimutavel\b", r"\bcloudformation\b", r"\binfrastructure as code\b", r"\bautomation strategies\b", r"\binfrastructure integrity\b"),
    "quota_throttle": (r"\bquotas?\b", r"\bthrottl", r"\brate limit", r"\blimites?\b"),
    "observability": (r"\bvisibility\b", r"\bobservab", r"\bx-ray\b", r"\btrac", r"\bmetrics?\b", r"\bcloudwatch\b"),
    "availability": (r"\bhighly available\b", r"\bfault-tolerant\b", r"\bavailability\b", r"\balta disponibilidade\b", r"\btolerancia a falhas\b"),
    "compute": (r"\bcompute\b", r"\bec2\b", r"\bbatch\b", r"\bemr\b", r"\blambda\b", r"\becs\b", r"\bfargate\b", r"\binstancias?\b"),
    "instance_selection": (r"\binstance types?\b", r"\binstance famil", r"\binstance sizes?\b", r"\bmemory optimized\b", r"\bcompute optimized\b", r"\btipo.*instancia\b", r"\bfamilia.*instancia\b"),
    "workload_criticality": (r"\bproduction workloads?\b", r"\bnon-production workloads?\b", r"\bclasses of workloads?\b", r"\bworkload criticality\b", r"\bclasses? de workloads?\b", r"\bclasse de producao\b", r"\bcheckout de producao\b", r"\bambiente de desenvolvimento\b", r"\bproducao critica\b", r"\bnao producao\b", r"\bcriticidade\b", r"\bcargas? (?:de )?producao\b"),
    "streaming": (r"\bstream", r"\bkinesis\b", r"\bmsk\b", r"\bflink\b"),
    "database": (r"\bdatabase\b", r"\bbanco de dados\b", r"\brds\b", r"\baurora\b", r"\bdynamodb\b", r"\bmysql\b", r"\bpostgres"),
    "database_engine": (r"\bdatabase engines?\b", r"\bmysql\b", r"\bpostgres", r"\bheterogeneous migrations?\b", r"\bhomogeneous migrations?\b", r"\bengine de banco\b"),
    "database_type": (r"\bdatabase types?\b", r"\brelational.*non-relational\b", r"\bnon-relational\b", r"\bkey-value\b", r"\bdynamodb\b", r"\baurora\b", r"\btipo.*banco\b"),
    "database_architecture": (r"\bdatabase architectures?\b", r"\bdatabase design\b", r"\bchoosing a database\b", r"\bmatriz de bancos\b", r"\bescolha.*banco\b", r"\bneptune\b", r"\bdynamodb\b", r"\baurora\b", r"\brds\b"),
    "database_capacity": (r"\bcapacity units?\b", r"\bprovisioned iops\b", r"\bdatabase capacity\b", r"\bcapacidade\b"),
    "database_proxy": (r"\bdatabase connections?\b", r"\brds proxy\b", r"\bconnection churn\b", r"\bconexoes?\b"),
    "read_pattern": (r"\bread-intensive\b", r"\bwrite-intensive\b", r"\bread replicas?\b", r"\bleitura\b", r"\bescrita\b"),
    "analytics": (r"\banalytics\b", r"\bathena\b", r"\bredshift\b", r"\bquicksuite\b", r"\bquick sight\b", r"\banalise\b"),
    "ingestion": (r"\bingestion\b", r"\bingestao\b", r"\bfrequenc", r"\bcapacity modes?\b", r"\bpartition keys?\b", r"\bshards?\b", r"\bbuffer(?:ing| interval)?\b", r"\bbatch process", r"\bstreaming process"),
    "ingestion_endpoint": (r"\bingestion access points?\b", r"\bsecure access.*ingestion\b", r"\bacesso seguro.*ingestao\b", r"\bkinesis interface vpc endpoints?\b", r"\bputrecords?\b"),
    "data_processing": (r"\bdata processing\b", r"\bemr\b", r"\bapache spark\b", r"\bprocessamento de dados\b"),
    "data_volume_velocity": (r"\bsizes? and speeds?\b", r"\bvolume and velocity\b", r"\bdata velocity\b", r"\bevents? per second\b", r"\bvolume e velocidade\b", r"\bshards?\b", r"\bcapacity modes?\b", r"\bthroughput\b", r"\bhot shard\b"),
    "data_transfer": (r"\bdata transfer\b", r"\btransfer(?:ring)? data\b", r"\bdatasync\b", r"\btransfer family\b", r"\bstorage gateway\b", r"\btransferencia\b"),
    "transformation": (r"\btransformation\b", r"\bglue\b", r"\bparquet\b", r"\bcsv\b", r"\btransformacao\b"),
    "visualization": (r"\bvisualization\b", r"\bquick sight\b", r"\bquicksuite\b", r"\bdashboards?\b", r"\bvisualizacao\b"),
    "data_lake": (r"\bdata lakes?\b", r"\blake formation\b", r"\blago de dados\b"),
    "cost_management": (r"\bcost management\b", r"\bcost explorer\b", r"\baws budgets?\b", r"\bcost and usage report\b", r"\bcur 2.0\b"),
    "cost_optimization": (r"\bcost-effective\b", r"\blowest cost\b", r"\bcost optim", r"\breduce costs?\b", r"\bmenor custo\b", r"\botimiz.*custo\b"),
    "purchasing": (r"\bpurchasing options?\b", r"\bspot\b", r"\breserved instances?\b", r"\bsavings plans?\b", r"\bmodelos? de compra\b"),
    "outposts": (r"\boutposts\b", r"\bhybrid compute\b", r"\bcompute hibrido\b"),
    "utilization": (r"\butilization\b", r"\brightsiz", r"\bcompute optimizer\b", r"\butilizacao\b", r"\bdimensionamento\b"),
    "nat": (r"\bnat gateways?\b", r"\bnat instances?\b", r"\bnat regional\b"),
    "routing": (r"\brout", r"\bpeering\b", r"\btransit gateway\b", r"\btopology\b", r"\brotas?\b", r"\broteamento\b", r"\btopologia\b"),
    "connectivity": (r"\bconnect", r"\bvpn\b", r"\bdirect connect\b", r"\bprivate lines?\b", r"\bconectividade\b", r"\bipsec\b"),
    "dns": (r"\bdns\b", r"\broute 53\b", r"\bttl\b"),
    "bandwidth": (r"\bbandwidth\b", r"\bthroughput\b", r"\bbanda\b", r"\bvazao\b"),
    "migration": (r"\bmigrat", r"\bdms\b", r"\bmgn\b", r"\bmigracao\b"),
    "ai_services": (r"\bcomprehend\b", r"\bpolly\b", r"\btranscribe\b", r"\btranslate\b", r"\brekognition\b", r"\btextract\b"),
    "ha_metrics": (r"\bmetrics? based on business requirements\b", r"\bbusiness metrics?\b", r"\bqueue (?:depth|backlog)\b", r"\bage of oldest message\b", r"\bbacklog per instance\b", r"\bmetricas?.*negocio\b", r"\bbacklog\b"),
    "spof": (r"\bsingle points? of failure\b", r"\bspof\b", r"\bponto unico de falha\b", r"\bno single point\b", r"\bload balanc.*multi-az\b", r"\bmulti-az\b"),
    "legacy_reliability": (r"\blegacy applications?\b", r"\bnot built for the cloud\b", r"\bapplication changes? (?:are )?not possible\b", r"\bamazon mq\b", r"\bjms\b", r"\baplicacoes? legad", r"\bsem alterar.*aplic"),
    "resource_placement": (r"\bplacement of resources\b", r"\bresource placement\b", r"\bplace resources\b", r"\bposicionamento.*recursos\b", r"\bpublic subnets?.*private\b", r"\bsubnets? por az e funcao\b", r"\bsubnet publica\b", r"\bsubnet.*availability zone\b", r"\balb publico.*banco privado\b"),
    "network_scalability": (r"\bnetwork configurations?.*scale\b", r"\bscalable network\b", r"\bmesh of peerings? grows\b", r"\bmalha de peerings cresce\b", r"\btransit gateway (?:is|e) (?:a )?regional hub\b", r"\btgw.*hub\b"),
    "network_optimization": (r"\bnetwork optimiz", r"\boptimiz.*network\b", r"\bexisting workloads?.*network\b", r"\botimiz.*rede\b", r"\bcross-az\b", r"\bnat processing\b", r"\bgateway endpoint\b", r"\bevitar nat\b", r"\bcompare custo\b", r"\bcustos? de rede\b"),
    "performance": (r"\bperformance\b", r"\bhigh-performing\b", r"\blatency\b", r"\biops\b", r"\bdesempenho\b", r"\blatencia\b"),
}
GENERIC_CONCEPTS = {
    "security", "availability", "network", "storage",
    "database", "compute", "performance",
}
STRICT_EVIDENCE_REQUIREMENTS: dict[str, tuple[set[str], int]] = {
    # Mencionar apenas containers não demonstra o fluxo de migração pedido pelo
    # guia; a evidência precisa cobrir explicitamente as duas dimensões.
    "How to migrate applications into containers": ({"container", "migration"}, 2),
    # Esta competência é deliberadamente transversal; uma evidência deve unir
    # ao menos três das quatro camadas, não apenas repetir "arquitetura".
    "Recommending appropriate compute, storage, networking, and database technologies based on requirements": (
        {"compute", "storage", "network", "database"},
        3,
    ),
}
MANDATORY_EVIDENCE_CONCEPTS: dict[str, set[str]] = {
    # "Streaming" ou "shard" demonstra ingestão, mas não demonstra controle
    # de acesso no ponto de entrada. Sem esta trava, a linha era falsamente
    # ligada a questões de hot shard e a um laboratório de SQS.
    "Secure access to ingestion access points": {"ingestion_endpoint"},
}
EXCLUDED_HEADING_TERMS = (
    "objetivos", "como estudar", "aulas deste bloco", "ligacoes",
    "referencias", "checklist", "continue o bloco", "registro antes",
)
SCENARIO_HEADING_RE = re.compile(r"\bcenarios? resolvidos?\b")
COMPARISON_HEADING_RE = re.compile(
    r"\btabelas? (?:de )?(?:decisao|escolha)\b|"
    r"\bcompar(?:acao|acoes|ar|ando|ado|ada|ativo|ativa|e|ed|ing|ison|isons)\b|"
    r"\bversus\b|"
    r"\btrade-?offs?\b|\bcapsula de decisao\b|\bdecisoes em camadas\b"
)


@dataclass(frozen=True)
class Competency:
    domain: int
    task: str
    kind: str
    text: str


@dataclass(frozen=True)
class QuestionEvidence:
    question_id: str
    task: str
    question_type: str
    question_format: str
    body: str


@dataclass(frozen=True)
class LabEvidence:
    block: int
    path: Path
    body: str


@dataclass(frozen=True)
class MarkdownSection:
    heading: str
    body: str
    level: int

    @property
    def evidence_text(self) -> str:
        return f"{self.heading}\n{self.body}"


def fetch_markdown(url: str) -> str:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "AmazonCertificate-SAA-C03-audit/1.0"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8")


def parse_competencies(domain: int, markdown: str) -> list[Competency]:
    competencies: list[Competency] = []
    task: str | None = None
    kind: str | None = None
    for raw_line in markdown.splitlines():
        line = raw_line.strip()
        task_match = re.match(r"^## Task (\d\.\d):", line)
        if task_match:
            task = task_match.group(1)
            kind = None
            continue
        if line == "Knowledge of:":
            kind = "knowledge"
            continue
        if line == "Skills in:":
            kind = "skill"
            continue
        if task and kind and line.startswith("+ "):
            competencies.append(Competency(domain, task, kind, line[2:].strip()))
    return competencies


def normalize_text(text: str) -> str:
    decomposed = unicodedata.normalize("NFKD", text)
    return "".join(char for char in decomposed if not unicodedata.combining(char)).casefold()


@lru_cache(maxsize=None)
def semantic_features(text: str) -> frozenset[str]:
    normalized = normalize_text(text)
    return frozenset(
        concept
        for concept, patterns in CONCEPT_PATTERNS.items()
        if any(re.search(pattern, normalized) for pattern in patterns)
    )


def evidence_relevance_score(competency: str, evidence: str) -> int:
    """Return a positive score only for auditable semantic overlap.

    Generic overlap such as merely mentioning ``storage`` or ``cost`` is not
    sufficient. At least one specific architectural concept must occur in both
    the official competency and the cited evidence.
    """

    competency_features = semantic_features(competency)
    evidence_features = semantic_features(evidence)
    mandatory = MANDATORY_EVIDENCE_CONCEPTS.get(competency)
    if mandatory is not None and not mandatory <= evidence_features:
        return 0
    strict = STRICT_EVIDENCE_REQUIREMENTS.get(competency)
    if strict is not None:
        required, minimum = strict
        matched_required = required & evidence_features
        if len(matched_required) < minimum:
            return 0
        return len(matched_required) * 10 + len(competency_features & evidence_features)
    shared = competency_features & evidence_features
    specific = shared - GENERIC_CONCEPTS
    if not specific:
        return 0
    return len(specific) * 10 + len(shared)


def _matches_rules(text: str, rules: Iterable[tuple[tuple[str, ...], int]]) -> int | None:
    normalized = normalize_text(text)
    for patterns, block in rules:
        if any(re.search(pattern, normalized) for pattern in patterns):
            return block
    return None


def choose_block(task: str, competency: str) -> int:
    task_match = _matches_rules(competency, TASK_ROUTING_RULES.get(task, ()))
    if task_match is not None:
        return task_match
    general_match = _matches_rules(competency, ROUTING_RULES)
    return general_match if general_match is not None else DEFAULT_BLOCK[task]


def validate_routing_model() -> list[str]:
    failures: list[str] = []
    for competency, (task, expected) in ROUTING_SENTINELS.items():
        actual = choose_block(task, competency)
        if actual != expected:
            failures.append(f"{competency!r}: B{actual:02d} != B{expected:02d}")
    return failures


def chapter_for(block: int) -> Path:
    matches = sorted((ROOT / "03_Guia_do_Estudante" / "Capitulos").glob(f"B{block:02d}_*.md"))
    if len(matches) != 1:
        raise RuntimeError(f"B{block:02d}: esperado um capítulo; encontrado {len(matches)}")
    return matches[0]


def lab_for(block: int) -> Path:
    matches = sorted((ROOT / "05_Laboratorios").glob(f"LAB_B{block:02d}_*.md"))
    if len(matches) != 1:
        raise RuntimeError(f"B{block:02d}: esperado um laboratório; encontrado {len(matches)}")
    return matches[0]


def lab_evidence() -> list[LabEvidence]:
    result: list[LabEvidence] = []
    for path in sorted((ROOT / "05_Laboratorios").glob("LAB_B??_*.md")):
        match = re.match(r"LAB_B(\d{2})_", path.name)
        if match:
            result.append(
                LabEvidence(
                    block=int(match.group(1)),
                    path=path,
                    body=path.read_text(encoding="utf-8"),
                )
            )
    return result


def select_lab(
    competency: str,
    preferred_block: int,
    labs: list[LabEvidence],
) -> str:
    override_block = LAB_BLOCK_OVERRIDES.get(competency)
    if override_block is not None:
        override = next((lab for lab in labs if lab.block == override_block), None)
        if override and evidence_relevance_score(competency, override.body) > 0:
            return relative(override.path)
    ranked = [
        (
            lab.block == preferred_block,
            evidence_relevance_score(competency, lab.body),
            -lab.block,
            lab,
        )
        for lab in labs
    ]
    ranked = [entry for entry in ranked if entry[1] > 0]
    ranked.sort(reverse=True, key=lambda entry: entry[:3])
    return relative(ranked[0][3].path) if ranked else ""


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


@lru_cache(maxsize=None)
def markdown_sections(path: Path) -> tuple[MarkdownSection, ...]:
    text = path.read_text(encoding="utf-8")
    matches = list(re.finditer(r"^(#{2,4}) (.+)$", text, re.MULTILINE))
    sections: list[MarkdownSection] = []
    for index, match in enumerate(matches):
        level = len(match.group(1))
        end = len(text)
        for following in matches[index + 1 :]:
            if len(following.group(1)) <= level:
                end = following.start()
                break
        sections.append(
            MarkdownSection(
                heading=match.group(2).strip(),
                body=text[match.end() : end].strip(),
                level=level,
            )
        )
    return tuple(sections)


def section_for_heading(path: Path, heading: str) -> MarkdownSection | None:
    return next((section for section in markdown_sections(path) if section.heading == heading), None)


def is_scenario_section(section: MarkdownSection) -> bool:
    return bool(SCENARIO_HEADING_RE.search(normalize_text(section.heading)))


def is_comparison_section(section: MarkdownSection) -> bool:
    return bool(COMPARISON_HEADING_RE.search(normalize_text(section.heading)))


def is_theory_section(section: MarkdownSection) -> bool:
    # Cenários e comparações demonstram aplicação. Não devem ser reutilizados
    # como a evidência teórica que torna a mesma linha "completa".
    return not is_scenario_section(section) and not is_comparison_section(section)


def best_relevant_section(
    competency: str,
    candidates: Iterable[MarkdownSection],
) -> str:
    ranked: list[tuple[bool, int, int, int, str]] = []
    for section in candidates:
        normalized_heading = normalize_text(section.heading)
        if any(term in normalized_heading for term in EXCLUDED_HEADING_TERMS):
            continue
        score = evidence_relevance_score(competency, section.evidence_text)
        if score <= 0:
            continue
        heading_score = evidence_relevance_score(competency, section.heading)
        # Uma correspondência no próprio título e uma subseção mais específica
        # são preferíveis a um H2 genérico cujo corpo agrega o capítulo inteiro.
        ranked.append(
            (heading_score > 0, heading_score, section.level, score, section.heading)
        )
    ranked.sort(reverse=True)
    return ranked[0][4] if ranked else ""


def parse_metadata_table(text: str) -> dict[str, dict[str, str]]:
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.startswith("| ID |"):
            headers = [value.strip() for value in line.strip("|").split("|")]
            rows: dict[str, dict[str, str]] = {}
            for row in lines[index + 2 :]:
                if not row.startswith("|"):
                    break
                values = [value.strip() for value in row.strip("|").split("|")]
                if len(values) != len(headers):
                    continue
                record = dict(zip(headers, values))
                rows[record["ID"]] = record
            return rows
    return {}


def question_evidence() -> list[QuestionEvidence]:
    result: list[QuestionEvidence] = []
    directory = ROOT / "04_Questoes_e_Revisoes" / "Blocos"
    for path in sorted(directory.glob("B??_Questoes.md")):
        text = path.read_text(encoding="utf-8")
        metadata = parse_metadata_table(text)
        matches = list(re.finditer(r"^### (B\d{2}-\d{2})$", text, re.MULTILINE))
        for index, match in enumerate(matches):
            end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
            question_id = match.group(1)
            record = metadata.get(question_id, {})
            question_body = text[match.end() : end].split("\n## ", 1)[0]
            result.append(
                QuestionEvidence(
                    question_id=question_id,
                    task=record.get("Tarefa", ""),
                    question_type=record.get("Tipo", ""),
                    question_format=record.get("Formato", ""),
                    body=question_body,
                )
            )
    return result


def select_question(
    competency: str,
    task: str,
    questions: list[QuestionEvidence],
    *,
    kind: str,
) -> str:
    # A tarefa do banco é a classificação primária da questão, não uma barreira
    # para evidência transversal. A matriz pode reutilizar um cenário de outra
    # tarefa somente quando a pertinência com a competência é positiva.
    candidates = list(questions)
    if kind == "fundamental":
        candidates = [question for question in candidates if question.question_type == "fundamental"]
    elif kind == "integrated":
        candidates = [question for question in candidates if question.question_type == "integrada"]
    elif kind == "multi":
        candidates = [question for question in candidates if question.question_format in {"multi-2", "multi-3"}]
    ranked = [
        (
            evidence_relevance_score(competency, question.body),
            task in {value.strip() for value in question.task.split("/")},
            question.question_id,
        )
        for question in candidates
    ]
    ranked = [entry for entry in ranked if entry[0] > 0]
    ranked.sort(reverse=True)
    return ranked[0][2] if ranked else ""


def review_values(block: int) -> tuple[str, str]:
    path = ROOT / "06_Progresso" / f"B{block:02d}_Checklist_e_Revisoes.md"
    text = path.read_text(encoding="utf-8")
    d2_match = re.search(r"^\*\*D\+2[^:]*:\*\* (.+)$", text, re.MULTILINE)
    d7_match = re.search(r"^\*\*D\+7[^:]*:\*\* (.+)$", text, re.MULTILINE)
    path_text = relative(path)
    d2 = f"{path_text} — {d2_match.group(1)}" if d2_match else path_text
    d7 = f"{path_text} — {d7_match.group(1)}" if d7_match else path_text
    return d2, d7


def build_rows(competencies: list[Competency]) -> list[dict[str, str]]:
    questions = question_evidence()
    labs = lab_evidence()
    rows: list[dict[str, str]] = []
    cache: dict[int, tuple[Path, list[MarkdownSection]]] = {}
    for competency in competencies:
        block = choose_block(competency.task, competency.text)
        if block not in cache:
            chapter = chapter_for(block)
            cache[block] = (
                chapter,
                markdown_sections(chapter),
            )
        chapter, chapter_sections = cache[block]
        theory_sections = [
            candidate for candidate in chapter_sections if is_theory_section(candidate)
        ]
        section = best_relevant_section(competency.text, theory_sections)
        comparisons = [
            candidate
            for candidate in chapter_sections
            if is_comparison_section(candidate)
        ]
        scenarios = [
            candidate
            for candidate in chapter_sections
            if is_scenario_section(candidate)
        ]
        comparison = best_relevant_section(competency.text, comparisons)
        scenario = best_relevant_section(competency.text, scenarios)
        lab_reference = select_lab(competency.text, block, labs)
        fundamental = select_question(competency.text, competency.task, questions, kind="fundamental")
        integrated = select_question(competency.text, competency.task, questions, kind="integrated")
        multi = select_question(competency.text, competency.task, questions, kind="multi")
        d2, d7 = review_values(block)

        theory = bool(section)
        # Aplicação pode ser demonstrada por comparação, cenário ou laboratório
        # pertinente. Nenhum desses campos recebe fallback genérico.
        application = bool(comparison or scenario or lab_reference)
        question_coverage = bool(fundamental or integrated or multi)
        review = bool(d2 and d7)
        missing: list[str] = []
        if not theory:
            missing.append("teoria pertinente")
        if not application:
            missing.append("aplicação pertinente")
        if not question_coverage:
            missing.append("questão pertinente")
        if not review:
            missing.append("revisão")
        status = "cobertura completa" if not missing else "cobertura parcial"
        rows.append(
            {
                "domínio": str(competency.domain),
                "peso": DOMAIN_WEIGHTS[competency.domain],
                "tarefa": competency.task,
                "knowledge ou skill": competency.kind,
                "competência": competency.text,
                "bloco": f"B{block:02d}",
                "capítulo": relative(chapter),
                "seção": section,
                "comparação": comparison,
                "cenário resolvido": scenario,
                "laboratório": lab_reference,
                "questão fundamental": fundamental,
                "questão integrada": integrated,
                "questão de múltipla resposta": multi,
                "D+2": d2,
                "D+7": d7,
                "referência oficial": DOMAIN_HTML_URLS[competency.domain],
                "data de validação": VALIDATION_DATE,
                "status": status,
                "lacuna": "; ".join(missing) if missing else "—",
            }
        )
    return rows


def render_csv(rows: list[dict[str, str]]) -> str:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=FIELDNAMES, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Compara a matriz atual com a fonte oficial.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    routing_failures = validate_routing_model()
    if routing_failures:
        print("FALHA: regressão no roteamento semântico:", file=sys.stderr)
        for failure in routing_failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    competencies: list[Competency] = []
    try:
        # As quatro páginas oficiais são independentes. A coleta paralela evita
        # multiplicar por quatro a latência do endpoint da documentação AWS.
        with ThreadPoolExecutor(max_workers=len(DOMAIN_URLS)) as executor:
            fetched = {
                domain: executor.submit(fetch_markdown, url)
                for domain, url in DOMAIN_URLS.items()
            }
            for domain in sorted(fetched):
                competencies.extend(
                    parse_competencies(domain, fetched[domain].result())
                )
    except (OSError, UnicodeError, urllib.error.URLError) as exc:
        print(f"FALHA: não foi possível obter o guia oficial: {exc}", file=sys.stderr)
        return 1
    tasks = {competency.task for competency in competencies}
    if tasks != EXPECTED_TASKS:
        print(
            f"FALHA: tarefas oficiais inesperadas: {sorted(tasks)}", file=sys.stderr
        )
        return 1
    rows = build_rows(competencies)
    rendered = render_csv(rows)
    if args.check:
        if not OUTPUT.is_file() or OUTPUT.read_text(encoding="utf-8-sig") != rendered:
            print("FALHA: matriz de competências está desatualizada.", file=sys.stderr)
            return 1
    else:
        OUTPUT.write_text(rendered, encoding="utf-8")
    status_counts: dict[str, int] = {}
    for row in rows:
        status_counts[row["status"]] = status_counts.get(row["status"], 0) + 1
    print(
        f"OK: {len(rows)} competências oficiais em {len(tasks)} tarefas; "
        + ", ".join(f"{status}={count}" for status, count in sorted(status_counts.items()))
        + "."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
