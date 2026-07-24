#!/usr/bin/env python3
"""Gera uma matriz inicial de cobertura SAA-C03 a partir do inventário da Udemy.

O mapeamento é deliberadamente conservador: usa a seção, o título e regras
semânticas reproduzíveis. A matriz é uma primeira classificação auditável, não
uma alegação de que o conteúdo real de uma aula foi inspecionado.
"""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path


WORKSPACE = Path(__file__).resolve().parents[2]
INPUT = (
    WORKSPACE
    / "01_Fontes"
    / "Udemy"
    / "Inventario_Curso_Udemy_SAA-C03.csv"
)
OUTPUT = WORKSPACE / "02_Planejamento" / "Matriz_Cobertura_SAA-C03.csv"
SUMMARY = (
    WORKSPACE / "02_Planejamento" / "Analise_Inicial_Cobertura_SAA-C03.md"
)


TASKS = {
    "1.1": (
        "1",
        "Design Secure Architectures",
        "Design secure access to AWS resources",
    ),
    "1.2": (
        "1",
        "Design Secure Architectures",
        "Design secure workloads and applications",
    ),
    "1.3": (
        "1",
        "Design Secure Architectures",
        "Determine appropriate data security controls",
    ),
    "2.1": (
        "2",
        "Design Resilient Architectures",
        "Design scalable and loosely coupled architectures",
    ),
    "2.2": (
        "2",
        "Design Resilient Architectures",
        "Design highly available and/or fault-tolerant architectures",
    ),
    "3.1": (
        "3",
        "Design High-Performing Architectures",
        "Determine high-performing and/or scalable storage solutions",
    ),
    "3.2": (
        "3",
        "Design High-Performing Architectures",
        "Design high-performing and elastic compute solutions",
    ),
    "3.3": (
        "3",
        "Design High-Performing Architectures",
        "Determine high-performing database solutions",
    ),
    "3.4": (
        "3",
        "Design High-Performing Architectures",
        "Determine high-performing and/or scalable network architectures",
    ),
    "3.5": (
        "3",
        "Design High-Performing Architectures",
        "Determine high-performing data ingestion and transformation solutions",
    ),
    "4.1": (
        "4",
        "Design Cost-Optimized Architectures",
        "Design cost-optimized storage solutions",
    ),
    "4.2": (
        "4",
        "Design Cost-Optimized Architectures",
        "Design cost-optimized compute solutions",
    ),
    "4.3": (
        "4",
        "Design Cost-Optimized Architectures",
        "Design cost-optimized database solutions",
    ),
    "4.4": (
        "4",
        "Design Cost-Optimized Architectures",
        "Design cost-optimized network architectures",
    ),
}

DOMAIN_URLS = {
    "1": "https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain1.html",
    "2": "https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain2.html",
    "3": "https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain3.html",
    "4": "https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain4.html",
}

# (tarefa principal, tarefas secundárias, conceito dominante)
SECTION_DEFAULTS = {
    1: ("", [], "Orientação e criação da conta"),
    2: ("", [], "Materiais do curso"),
    3: ("2.2", ["1.1"], "Infraestrutura global e console AWS"),
    4: ("1.1", ["1.2"], "Identity and Access Management"),
    5: ("3.2", ["4.2", "1.2"], "Amazon EC2 e opções de computação"),
    6: ("3.2", ["3.4", "2.2", "4.2"], "EC2 avançado e rede de instâncias"),
    7: ("3.1", ["4.1", "2.2", "1.3"], "Armazenamento de instâncias"),
    8: ("2.2", ["3.2", "3.4", "4.2"], "Alta disponibilidade e escalabilidade"),
    9: ("3.3", ["2.2", "4.3", "1.3"], "Bancos relacionais e cache"),
    10: ("3.4", ["2.2", "4.4"], "DNS, roteamento e failover"),
    11: ("2.1", ["2.2", "3.2", "3.4", "4.2"], "Arquiteturas clássicas"),
    12: ("3.1", ["4.1", "1.3", "2.2"], "Amazon S3"),
    13: ("4.1", ["3.1", "2.1", "3.5"], "S3 avançado"),
    14: ("1.3", ["1.1", "1.2"], "Segurança de dados no S3"),
    15: ("3.4", ["4.4", "2.2", "1.2"], "Edge e entrega global"),
    16: ("3.1", ["4.1", "3.5", "2.2"], "Serviços de armazenamento"),
    17: ("2.1", ["3.5", "3.2"], "Mensageria e desacoplamento"),
    18: ("3.2", ["2.1", "4.2"], "Contêineres"),
    19: ("2.1", ["3.2", "3.3", "4.2", "4.3", "1.2"], "Serverless"),
    20: ("2.1", ["2.2", "3.2", "3.3"], "Arquiteturas serverless"),
    21: ("3.3", ["4.3", "2.2"], "Escolha de bancos de dados"),
    22: ("3.5", ["3.3", "4.3", "1.3"], "Dados e analytics"),
    23: ("3.5", ["2.2"], "Machine Learning gerenciado"),
    24: ("2.2", ["1.2", "1.3", "2.1"], "Observabilidade e auditoria"),
    25: ("1.1", ["1.2"], "IAM avançado e múltiplas contas"),
    26: ("1.3", ["1.2", "1.1"], "Criptografia e proteção de aplicações"),
    27: ("3.4", ["1.2", "2.2", "4.4"], "VPC e conectividade"),
    28: ("2.2", ["3.5", "4.1", "4.3"], "Disaster Recovery e migração"),
    29: ("2.2", ["2.1", "3.2", "3.3", "3.4"], "Arquiteturas integradas"),
    30: ("2.2", ["3.2", "3.5", "4.2"], "Serviços complementares"),
    31: ("2.2", ["1.1", "1.2", "1.3", "2.1", "3.1", "3.2", "3.3", "3.4", "3.5", "4.1", "4.2", "4.3", "4.4"], "Well-Architected e revisão"),
    32: ("", [], "Preparação para o exame"),
    33: ("", [], "Encerramento do curso"),
}

# Refinamentos confirmados durante a produção do B04. A tarefa 4.2 cita
# explicitamente hibernation/EC2 hibernation; AMI se liga principalmente a
# infraestrutura imutável e recuperação em 2.2. As demais aulas recebem somente
# os vínculos secundários efetivamente tratados no bloco.
LECTURE_TASK_OVERRIDES = {
    47: ("3.4", ["4.4"]),
    48: ("3.4", ["4.4"]),
    49: ("3.2", ["2.2"]),
    50: ("3.2", ["2.2"]),
    51: ("3.4", ["2.2"]),
    52: ("3.4", ["2.2"]),
    53: ("3.4", ["2.2"]),
    54: ("4.2", ["3.2"]),
    55: ("4.2", ["3.2"]),
    56: ("3.1", ["4.1"]),
    57: ("3.1", ["4.1"]),
    58: ("2.2", ["4.1"]),
    59: ("2.2", ["4.1"]),
    60: ("2.2", ["3.2"]),
}

WEEKS = {
    **{section: "Semana 1 - 25/07 a 01/08" for section in range(1, 9)},
    **{section: "Semana 2 - 03/08 a 08/08" for section in range(9, 17)},
    **{section: "Semana 3 - 10/08 a 15/08" for section in range(17, 22)},
    **{section: "Semana 4 - 17/08 a 22/08" for section in range(22, 28)},
    **{section: "Semana 5 - 24/08 a 27/08" for section in range(28, 32)},
    32: "Fase final - 28/08 a 31/08",
    33: "Fase final - 28/08 a 31/08",
}

# Serviços explicitamente fora do escopo e presentes no currículo.
OUT_OF_SCOPE_PATTERNS = {
    r"\bcloudshell\b": "AWS CloudShell",
    r"\bpersonalize\b": "Amazon Personalize",
}

# Itens que misturam conteúdo em escopo e fora do escopo.
MIXED_SCOPE_LECTURES = {
    18: "A aula combina access keys/AWS CLI (relevantes) com AWS SDKs (explicitamente fora do escopo).",
}

SERVICE_PATTERNS = [
    (r"\biam identity center\b|\bidentity center\b", "AWS IAM Identity Center"),
    (r"\biam\b", "AWS IAM"),
    (r"\baws cli\b|\bcli\b", "AWS CLI"),
    (r"\bcloudshell\b", "AWS CloudShell"),
    (r"\bec2 instance connect\b", "EC2 Instance Connect"),
    (r"\bec2\b|\bami\b|\binstance store\b", "Amazon EC2"),
    (r"\bebs\b", "Amazon EBS"),
    (r"\befs\b", "Amazon EFS"),
    (r"\bapplication load balancer\b|\balb\b", "Application Load Balancer"),
    (r"\bnetwork load balancer\b|\bnlb\b", "Network Load Balancer"),
    (r"\bgateway load balancer\b|\bgwlb\b", "Gateway Load Balancer"),
    (r"\belastic load balanc|\belb\b", "Elastic Load Balancing"),
    (r"\bauto scaling\b|\basg\b", "Amazon EC2 Auto Scaling"),
    (r"\brds proxy\b", "Amazon RDS Proxy"),
    (r"\brds\b", "Amazon RDS"),
    (r"\baurora\b", "Amazon Aurora"),
    (r"\belasticache\b", "Amazon ElastiCache"),
    (r"\broute 53\b", "Amazon Route 53"),
    (r"\bbeanstalk\b", "AWS Elastic Beanstalk"),
    (r"\bs3\b|\bglacier\b", "Amazon S3"),
    (r"\bcloudfront\b", "Amazon CloudFront"),
    (r"\bglobal accelerator\b", "AWS Global Accelerator"),
    (r"\bsnow\b", "AWS Snow Family"),
    (r"\bfsx\b", "Amazon FSx"),
    (r"\bstorage gateway\b", "AWS Storage Gateway"),
    (r"\btransfer family\b", "AWS Transfer Family"),
    (r"\bdatasync\b", "AWS DataSync"),
    (r"\bsqs\b", "Amazon SQS"),
    (r"\bsns\b", "Amazon SNS"),
    (r"\bdata firehose\b|\bfirehose\b", "Amazon Data Firehose"),
    (r"\bkinesis\b", "Amazon Kinesis"),
    (r"\bamazon mq\b", "Amazon MQ"),
    (r"\becr\b", "Amazon ECR"),
    (r"\becs\b", "Amazon ECS"),
    (r"\beks\b", "Amazon EKS"),
    (r"\bfargate\b", "AWS Fargate"),
    (r"\blambda\b", "AWS Lambda"),
    (r"\bdynamodb\b", "Amazon DynamoDB"),
    (r"\bapi gateway\b", "Amazon API Gateway"),
    (r"\bstep functions?\b", "AWS Step Functions"),
    (r"\bcognito\b", "Amazon Cognito"),
    (r"\bdocumentdb\b", "Amazon DocumentDB"),
    (r"\bneptune\b", "Amazon Neptune"),
    (r"\bkeyspaces\b", "Amazon Keyspaces"),
    (r"\btimestream\b", "Amazon Timestream"),
    (r"\bathena\b", "Amazon Athena"),
    (r"\bredshift\b", "Amazon Redshift"),
    (r"\bopensearch\b", "Amazon OpenSearch Service"),
    (r"\bemr\b", "Amazon EMR"),
    (r"\bquicksight\b|\bquicksuite\b", "Amazon QuickSight / Amazon QuickSuite"),
    (r"\bglue\b", "AWS Glue"),
    (r"\blake formation\b", "AWS Lake Formation"),
    (r"\bflink\b", "Amazon Managed Service for Apache Flink"),
    (r"\bmsk\b|\bkafka\b", "Amazon MSK"),
    (r"\brekognition\b", "Amazon Rekognition"),
    (r"\btranscribe\b", "Amazon Transcribe"),
    (r"\bpolly\b", "Amazon Polly"),
    (r"\btranslate\b", "Amazon Translate"),
    (r"\blex\b", "Amazon Lex"),
    (r"\bamazon connect\b|\blex \+ connect\b", "Amazon Connect"),
    (r"\bcomprehend\b", "Amazon Comprehend"),
    (r"\bsagemaker\b", "Amazon SageMaker AI"),
    (r"\bkendra\b", "Amazon Kendra"),
    (r"\bpersonalize\b", "Amazon Personalize"),
    (r"\btextract\b", "Amazon Textract"),
    (r"\bcloudwatch\b", "Amazon CloudWatch"),
    (r"\beventbridge\b", "Amazon EventBridge"),
    (r"\bcloudtrail\b", "AWS CloudTrail"),
    (r"\baws config\b|\bconfig\b", "AWS Config"),
    (r"\borganizations?\b", "AWS Organizations"),
    (r"\bdirectory services?\b", "AWS Directory Service"),
    (r"\bcontrol tower\b", "AWS Control Tower"),
    (r"\bkms\b", "AWS KMS"),
    (r"\bparameter store\b", "AWS Systems Manager Parameter Store"),
    (r"\bsecrets manager\b", "AWS Secrets Manager"),
    (r"\bcertificate manager\b|\bacm\b", "AWS Certificate Manager"),
    (r"\bcloudhsm\b", "AWS CloudHSM"),
    (r"\bwaf\b", "AWS WAF"),
    (r"\bshield\b", "AWS Shield"),
    (r"\bfirewall manager\b", "AWS Firewall Manager"),
    (r"\bguardduty\b", "Amazon GuardDuty"),
    (r"\binspector\b", "Amazon Inspector"),
    (r"\bmacie\b", "Amazon Macie"),
    (r"\bnetwork firewall\b", "AWS Network Firewall"),
    (r"\bvpc\b", "Amazon VPC"),
    (r"\bnat gateway\b|\bnat instance\b", "NAT Gateway / NAT Instance"),
    (r"\bnacl\b", "Network ACL"),
    (r"\bsite to site vpn\b|\bvpn\b", "AWS Site-to-Site VPN"),
    (r"\bdirect connect\b", "AWS Direct Connect"),
    (r"\btransit gateway\b", "AWS Transit Gateway"),
    (r"\bdatabase migration service\b|\bdms\b", "AWS Database Migration Service"),
    (r"\baws backup\b", "AWS Backup"),
    (r"\bapplication migration service\b|\bmgn\b", "AWS Application Migration Service"),
    (r"\bvmware cloud\b", "VMware Cloud on AWS"),
    (r"\bcloudformation\b", "AWS CloudFormation"),
    (r"\bses\b", "Amazon SES"),
    (r"\bpinpoint\b", "Amazon Pinpoint"),
    (r"\bsession manager\b|\bssm\b", "AWS Systems Manager"),
    (r"\bcost explorer\b", "AWS Cost Explorer"),
    (r"\boutposts\b", "AWS Outposts"),
    (r"\bbatch\b", "AWS Batch"),
    (r"\bappflow\b", "Amazon AppFlow"),
    (r"\bamplify\b", "AWS Amplify"),
    (r"\bwell.architected\b", "AWS Well-Architected Tool"),
    (r"\btrusted advisor\b", "AWS Trusted Advisor"),
]


def normal(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip()).lower()


def add_unique(values: list[str], value: str) -> None:
    if value and value not in values:
        values.append(value)


def service_names(title: str) -> list[str]:
    lowered = normal(title)
    found: list[str] = []
    for pattern, service in SERVICE_PATTERNS:
        if re.search(pattern, lowered, flags=re.I):
            add_unique(found, service)
    return found


def nature(item_type: str, title: str) -> str:
    lowered = normal(title)
    if item_type == "quiz":
        return "Avaliação por seção"
    if item_type == "simulado":
        return "Simulado"
    if "hands on" in lowered or "hands-on" in lowered:
        return "Laboratório/demonstração"
    if "cleanup" in lowered or "clean up" in lowered:
        return "Limpeza de laboratório"
    if "architecture" in lowered or "architectures" in lowered or "discussion" in lowered:
        return "Cenário arquitetural"
    if any(
        token in lowered
        for token in (
            "course introduction",
            "important message",
            "about your instructor",
            "slides and code",
            "section introduction",
            "exam preparation",
            "exam walkthrough",
            "exam cost",
            "extra 30 minutes",
            "how does the exam work",
            "congratulations",
            "bonus lecture",
            "certification paths",
        )
    ):
        return "Administrativo/orientação"
    return "Teoria"


def cost_override(section: int, title: str) -> str | None:
    lowered = normal(title)
    if not re.search(
        r"\bcosts?\b|\bbudget\b|\bpurchas|\bspot\b|\bsavings?\b|"
        r"\bstorage class|\blifecycle|\brequester pays|\binstance scheduler",
        lowered,
    ):
        return None
    if section in {7, 12, 13, 16}:
        return "4.1"
    if section in {9, 19, 21}:
        return "4.3"
    if section in {10, 15, 27}:
        return "4.4"
    return "4.2"


def keyword_override(section: int, title: str, default: str) -> str:
    lowered = normal(title)

    # The course labels purchasing models as "launch types" in lesson 46.
    # Map that hands-on to cost optimization even though the title omits
    # keywords such as "purchasing", "Spot", or "Savings".
    if section == 5 and "instances launch types" in lowered:
        return "4.2"

    # SSH and EC2 Instance Connect are secure application-access controls:
    # ports, protocols, network path, and authorized administrative access.
    if section == 5 and re.search(r"\bssh\b|\bec2 instance connect\b", lowered):
        return "1.2"

    cost = cost_override(section, title)
    if cost:
        return cost

    if section == 21 and "choosing the right database" in lowered:
        return "4.3"

    if re.search(
        r"\biam\b|\bmfa\b|\borganizations?\b|\bidentity center\b|"
        r"\bdirectory services?\b|\bcontrol tower\b",
        lowered,
    ):
        return "1.1"

    if section == 4 and re.search(
        r"\busers?\b|\bgroups?\b|\broles?\b|\bpolic(?:y|ies)\b|\baccess keys?\b",
        lowered,
    ):
        return "1.1"

    if "instance roles" in lowered:
        return "1.1"

    if section in {4, 25} and re.search(r"\bpolic(?:y|ies)\b", lowered):
        return "1.1"

    if section in {12, 14} and "bucket policy" in lowered:
        return "1.1"

    if section == 24 and re.search(r"\bcloudtrail\b|\baws config\b", lowered):
        return "1.2"

    if re.search(
        r"\bsecurity groups?\b|\bnacl\b|\bbastion\b|\bwaf\b|\bshield\b|"
        r"\bddos\b|\bfirewall\b|\bguardduty\b|\binspector\b|\bmacie\b|"
        r"\bcognito\b|\bsecrets manager\b|\bparameter store\b|"
        r"\bsession manager\b|\bblocking an ip\b",
        lowered,
    ):
        return "1.2"

    if re.search(
        r"\bencrypt|\bkms\b|\bcloudhsm\b|\bcertificate manager\b|\bacm\b|"
        r"\bobject lock\b|\bvault lock\b|\bmfa delete\b|\baccess logs?\b|"
        r"\bpre-signed\b|\bdata security\b",
        lowered,
    ):
        return "1.3"

    if re.search(
        r"\bdisaster recovery\b|\bdrs\b|\bhigh availability\b|\bfailover\b|"
        r"\bmulti.?az\b|\bhealth checks?\b|\breplication\b|\bbackups?\b|"
        r"\bsnapshots?\b|\bversioning\b|\binstance high availability\b",
        lowered,
    ):
        return "2.2"

    if re.search(
        r"\bsqs\b|\bsns\b|\beventbridge\b|\bamazon mq\b|\bmicroservices?\b|"
        r"\bserverless\b|\bstep functions?\b|\bevent processing\b|"
        r"\bmessage visibility\b|\blong polling\b|\bfan out\b",
        lowered,
    ):
        return "2.1"

    if section in {7, 12, 13, 16} and re.search(
        r"\bebs\b|\befs\b|\bs3\b|\bfsx\b|\bstorage\b|\bsnow\b|\bglacier\b",
        lowered,
    ):
        return "3.1"

    if section in {5, 6, 8, 18, 19, 29, 30} and re.search(
        r"\bec2\b|\bplacement\b|\bauto scaling\b|\basg\b|\blambda\b|"
        r"\becs\b|\beks\b|\bfargate\b|\bbatch\b|\bcompute\b|\bhpc\b",
        lowered,
    ):
        return "3.2"

    if section in {9, 19, 21, 29} and re.search(
        r"\brds\b|\baurora\b|\bdynamodb\b|\belasticache\b|\bdatabase\b|"
        r"\bdocumentdb\b|\bneptune\b|\bkeyspaces\b|\btimestream\b|\bcaching\b",
        lowered,
    ):
        return "3.3"

    if section in {6, 8, 10, 15, 27, 29} and re.search(
        r"\bip\b|\beni\b|\belastic load balanc|\balb\b|\bnlb\b|\bgwlb\b|"
        r"\broute 53\b|\bdns\b|\bcloudfront\b|\bglobal accelerator\b|"
        r"\bvpc\b|\bsubnet\b|\binternet gateway\b|\bnat\b|\bpeering\b|"
        r"\bendpoints?\b|\bvpn\b|\bdirect connect\b|\btransit gateway\b|"
        r"\bipv6\b|\bnetwork\b",
        lowered,
    ):
        return "3.4"

    if section in {16, 17, 22, 23, 28, 30} and re.search(
        r"\bathena\b|\bredshift\b|\bopensearch\b|\bemr\b|\bquicksight\b|"
        r"\bglue\b|\blake formation\b|\bflink\b|\bmsk\b|\bkinesis\b|"
        r"\bfirehose\b|\bingestion\b|\bdatasync\b|\btransfer\b|\bsnow\b|"
        r"\bappflow\b|\bmigration\b",
        lowered,
    ):
        return "3.5"

    return default


def category(
    section: int,
    lecture_number: int | None,
    item_type: str,
    title: str,
    item_nature: str,
) -> tuple[str, str, str]:
    lowered = normal(title)

    for pattern, service in OUT_OF_SCOPE_PATTERNS.items():
        if re.search(pattern, lowered, flags=re.I):
            return (
                "Fora do escopo",
                "Pular para a prova; opcional para prática profissional",
                f"{service} consta explicitamente na lista oficial de serviços fora do escopo.",
            )

    if item_type in {"quiz", "simulado"}:
        return (
            "Avaliação pendente",
            "Classificar quando as questões forem disponibilizadas",
            "O título foi capturado, mas o conteúdo das questões não está disponível.",
        )

    if lecture_number in MIXED_SCOPE_LECTURES:
        return (
            "Complementar",
            "Estudar access keys e AWS CLI; tratar SDK apenas como contexto",
            MIXED_SCOPE_LECTURES[lecture_number],
        )

    if item_nature in {"Laboratório/demonstração", "Limpeza de laboratório"}:
        return (
            "Operacional",
            "Executar seletivamente, validar resultado, custo e limpeza",
            "O foco principal é execução prática de conteúdo relacionado ao blueprint.",
        )

    if section in {1, 2, 3, 32, 33}:
        return (
            "Complementar",
            "Consumir rapidamente e registrar apenas decisões úteis",
            "Conteúdo de orientação, fundamento ou preparação, sem tarefa única dominante.",
        )

    if re.search(
        r"\brds custom\b|\btimestream\b|\bmanaged service for apache flink\b|"
        r"\bcomprehend medical\b|\blex \+ connect\b|\btraffic mirroring\b|"
        r"\blive tail\b|\bnetwork synthetic monitor\b|\bamazon ses\b|"
        r"\bpinpoint\b|\bcost anomaly detection\b|\binstance scheduler\b|"
        r"\bs3 object lambda\b",
        lowered,
    ):
        return (
            "Complementar",
            "Aprender o caso de uso e a relação com serviços centrais; revisão reduzida",
            "Conteúdo útil ou relacionado ao blueprint, mas sem prioridade central explícita.",
        )

    if section == 23:
        return (
            "Complementar",
            "Aprender casos de uso e diferenças; revisão de baixa intensidade",
            "Serviços gerenciados em escopo, mas com contribuição secundária às decisões centrais.",
        )

    if any(
        token in lowered
        for token in (
            "extra reading",
            "region availability",
            "troubleshooting",
            "section summary",
            "section introduction",
            "overview from a solution architect perspective",
        )
    ):
        return (
            "Complementar",
            "Acelerar ou ler resumo",
            "Contexto útil, mas com ligação indireta ou profundidade secundária.",
        )

    return (
        "Essencial",
        "Estudar integralmente; notas de decisão; revisão D+2 e D+7",
        "O título corresponde diretamente a conhecimento ou habilidade do blueprint.",
    )


def merge_tasks(primary: str, defaults: list[str]) -> list[str]:
    result: list[str] = []
    for task in defaults:
        if task and task != primary and task in TASKS:
            add_unique(result, task)
    return result


def main() -> None:
    if not INPUT.exists():
        raise SystemExit(f"Inventário não encontrado: {INPUT}")

    with INPUT.open("r", encoding="utf-8-sig", newline="") as handle:
        source_rows = list(csv.DictReader(handle))

    rows: list[dict[str, str]] = []
    for source in source_rows:
        section = int(source["secao"])
        lecture_number = (
            int(source["numero_aula"]) if source["numero_aula"].strip() else None
        )
        title = source["titulo"]
        item_type = source["tipo"]
        default_task, default_secondary, concept = SECTION_DEFAULTS[section]
        item_nature = nature(item_type, title)
        if lecture_number in LECTURE_TASK_OVERRIDES:
            primary, refined_secondary = LECTURE_TASK_OVERRIDES[lecture_number]
            secondary = merge_tasks(primary, refined_secondary)
        else:
            primary = (
                keyword_override(section, title, default_task) if default_task else ""
            )
            secondary = merge_tasks(primary, default_secondary)
        item_category, action, reason = category(
            section, lecture_number, item_type, title, item_nature
        )

        # Itens explicitamente fora do escopo não comprovam uma tarefa oficial.
        if item_category == "Fora do escopo":
            primary = ""
            secondary = []

        if primary:
            domain, domain_name, task_name = TASKS[primary]
            source_url = DOMAIN_URLS[domain]
        else:
            domain = ""
            domain_name = ""
            task_name = ""
            source_url = (
                "https://docs.aws.amazon.com/aws-certification/latest/"
                "solutions-architect-associate-03/solutions-architect-associate-03.html"
            )

        if item_category in {"Essencial", "Operacional"} and primary:
            reason = f"{reason} Correspondência principal: tarefa {primary}."

        rows.append(
            {
                **source,
                "natureza": item_nature,
                "servicos_topicos": "; ".join(service_names(title)) or concept,
                "dominio_primario": domain,
                "nome_dominio": domain_name,
                "tarefa_primaria": primary,
                "nome_tarefa": task_name,
                "tarefas_secundarias": "; ".join(secondary),
                "categoria": item_category,
                "justificativa_inicial": reason,
                "acao_de_estudo": action,
                "semana_planejada": WEEKS[section],
                "fonte_oficial_base": source_url,
                "status_aprendizagem": "não iniciado",
                "confianca_mapeamento": (
                    "pendente"
                    if item_category == "Avaliação pendente"
                    else "média"
                    if item_category in {"Complementar", "Operacional"}
                    else "alta"
                ),
            }
        )

    fieldnames = list(rows[0].keys())
    with OUTPUT.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    category_counts = Counter(row["categoria"] for row in rows)
    task_counts = Counter(
        row["tarefa_primaria"] for row in rows if row["tarefa_primaria"]
    )
    outside = [row for row in rows if row["categoria"] == "Fora do escopo"]
    unmapped = [
        row
        for row in rows
        if not row["tarefa_primaria"]
        and row["categoria"] not in {"Fora do escopo", "Avaliação pendente"}
    ]

    lines = [
        "# Análise inicial de cobertura - AWS SAA-C03",
        "",
        "**Gerado em:** 24/07/2026  ",
        "**Base:** títulos e metadados dos 425 itens da Udemy + guia oficial vigente.",
        "",
        "> A base continua sendo uma classificação inicial pelos títulos. Refinamentos",
        "> confirmados durante os blocos já produzidos são incorporados ao gerador; os",
        "> demais itens serão revisados com o conteúdo e a documentação oficial.",
        "",
        "## Integridade",
        "",
        f"- Linhas na matriz: **{len(rows)}**.",
        f"- Aulas numeradas: **{sum(1 for row in rows if row['numero_aula'])}**.",
        f"- Itens concluídos na Udemy: **{sum(1 for row in rows if row['concluido'] == 'sim')}**.",
        "",
        "## Categorias iniciais",
        "",
        "| Categoria | Itens |",
        "|---|---:|",
    ]
    for name in (
        "Essencial",
        "Complementar",
        "Operacional",
        "Fora do escopo",
        "Avaliação pendente",
    ):
        lines.append(f"| {name} | {category_counts.get(name, 0)} |")

    lines.extend(
        [
            "",
            "## Cobertura por tarefa principal",
            "",
            "| Tarefa | Nome | Itens com mapeamento principal |",
            "|---|---|---:|",
        ]
    )
    for code in TASKS:
        lines.append(f"| {code} | {TASKS[code][2]} | {task_counts.get(code, 0)} |")

    lines.extend(
        [
            "",
            "## Itens explicitamente fora do escopo",
            "",
        ]
    )
    for row in outside:
        number = row["numero_aula"] or row["indice_item"]
        lines.append(f"- **{number}. {row['titulo']}** - {row['justificativa_inicial']}")

    lines.extend(
        [
            "",
            "## Itens sem tarefa principal",
            "",
            f"Há **{len(unmapped)}** itens administrativos ou introdutórios sem tarefa",
            "principal. Isso é esperado e não representa, por si só, uma lacuna.",
            "",
            "## Limitações e próxima auditoria",
            "",
            "- Quizzes e o simulado aguardam o conteúdo das questões.",
            "- A classificação de hands-on como Operacional não reduz a relevância do",
            "  conceito associado; ela define a forma de estudo.",
            "- Serviços ausentes das listas oficiais não foram automaticamente tratados",
            "  como fora do escopo.",
            "- A matriz deverá ser revisada capítulo a capítulo durante a produção do Guia.",
            "- A cobertura secundária deve ser considerada ao avaliar equilíbrio entre",
            "  domínios; a contagem principal não é uma previsão de incidência na prova.",
            "",
        ]
    )
    SUMMARY.write_text("\n".join(lines), encoding="utf-8")

    if len(rows) != 425:
        raise SystemExit(f"Falha: esperadas 425 linhas, obtidas {len(rows)}")
    missing_tasks = sorted(set(TASKS) - set(task_counts))
    if missing_tasks:
        raise SystemExit(f"Falha: tarefas sem cobertura principal: {missing_tasks}")

    print(f"Matriz criada: {OUTPUT}")
    print(f"Resumo criado: {SUMMARY}")
    print(f"Linhas: {len(rows)}")
    print("Categorias:", dict(category_counts))
    print("Tarefas:", dict(sorted(task_counts.items())))


if __name__ == "__main__":
    main()
