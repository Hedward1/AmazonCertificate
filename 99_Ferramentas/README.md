# 99 - Ferramentas

Scripts executados a partir da raiz do projeto:

```powershell
python .\99_Ferramentas\scripts\extrair_inventario_udemy.py
python .\99_Ferramentas\scripts\gerar_matriz_cobertura.py
python .\99_Ferramentas\scripts\gerar_roteiro_diario_udemy.py
python .\99_Ferramentas\scripts\gerar_roteiro_diario_udemy.py --check
```

O primeiro valida o HTML e recria o inventário com 425 itens. O segundo recria a
matriz de cobertura e a análise inicial. O terceiro recria o roteiro B01–B25 e
valida que todos os 425 itens tenham exatamente um destino, incluindo o
practice exam reservado ao SIM B.

O HTML bruto da Udemy não faz parte do repositório. Para executar o primeiro
script, salve sua própria página autenticada localmente no caminho esperado pelo
script. Nunca faça commit da captura, dos assets baixados, de cookies ou de
dados de sessão.
