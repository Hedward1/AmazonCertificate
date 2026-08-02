# 99 - Ferramentas

Scripts executados a partir da raiz do projeto:

```powershell
python .\99_Ferramentas\scripts\extrair_inventario_udemy.py
python .\99_Ferramentas\scripts\gerar_matriz_cobertura.py
python .\99_Ferramentas\scripts\gerar_roteiro_diario_udemy.py
python .\99_Ferramentas\scripts\gerar_roteiro_diario_udemy.py --check
python .\99_Ferramentas\scripts\gerar_matriz_competencias_oficiais.py
python .\99_Ferramentas\scripts\gerar_matriz_competencias_oficiais.py --check
python .\99_Ferramentas\scripts\gerar_simulados_privados.py
python .\99_Ferramentas\scripts\gerar_simulados_privados.py --validate-only
python .\99_Ferramentas\scripts\validar_material_completo.py
python .\99_Ferramentas\scripts\validar_material_completo.py --require-private
```

O primeiro valida o HTML e recria o inventário com 425 itens. O segundo recria a
matriz de cobertura e a análise inicial. O terceiro recria o roteiro B01–B25 e
valida que todos os 425 itens tenham exatamente um destino, mantendo o practice
exam da Udemy reservado até a data planejada.

O gerador de competências consulta as quatro páginas oficiais do SAA-C03 e
mantém uma linha para cada Knowledge/Skill. O gerador de simulados valida e
renderiza os bancos privados ignorados pelo Git; ele atualiza no manifesto
público somente hashes e estado de validação.

O validador final confere o pacote editorial, formatos single/multi-answer,
distribuições, gabaritos e análises, similaridade semântica, as 189
competências, cápsulas prioritárias, conteúdo opcional, manifesto/simulados,
links locais e os 180 minutos de cada dia. Use `--require-private` na máquina
que contém os três bancos locais.

O HTML bruto da Udemy não faz parte do repositório. Para executar o primeiro
script, salve sua própria página autenticada localmente no caminho esperado pelo
script. Nunca faça commit da captura, dos assets baixados, de cookies ou de
dados de sessão.
