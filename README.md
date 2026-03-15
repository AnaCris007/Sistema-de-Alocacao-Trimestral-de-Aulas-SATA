# Sistema de Alocação Trimestral de Aulas (SATA)

Este projeto foi desenvolvido para resolver o desafio técnico descrito em [instrucoes.md](instrucoes.md): gerar uma grade trimestral de aulas (12 semanas), respeitando disponibilidade de professores, limites de carga horária e proporções por eixo.

A solução atual implementa uma abordagem gulosa (greedy) para montar uma alocação válida, priorizando:

- Eixos com maior déficit de horas no trimestre;
- Professores habilitados para o eixo;
- Disponibilidade no slot;
- Menor custo por aula entre os candidatos viáveis.

## Vídeo de explicação

A explicação do algoritmo está disponível em:
https://youtu.be/eAjglS_ksMI

## Estrutura do projeto
- main.py: implementação do algoritmo de alocação.
- exemplo.json: dados de entrada (semanas, slots e professores).
- instrucoes.md: enunciado completo do desafio.

## Como rodar

### Pré-requisito:

    Python 3.8+ instalado.

### Passos:

Abra o terminal na pasta do projeto e execute:

    python main.py

O programa irá:
- Ler os dados de entrada em exemplo.json;
- Gerar o plano trimestral;
- Exibir o resultado em JSON no terminal (incluindo grade por semana, horas por eixo, horas por professor e custo total).

### Observações
- Para testar outros cenários, edite o arquivo exemplo.json (professores, disponibilidade, custos, etc.).
- O algoritmo atual é uma solução base para o desafio, podendo ser evoluído para abordagens mais avançadas (ex.: ILP/MIP, Greedy + Repair).

