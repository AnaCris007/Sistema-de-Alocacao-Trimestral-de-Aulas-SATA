DESAFIO TÉCNICO: SISTEMA DE ALOCAÇÃO TRIMESTRAL DE AULAS (SATA)


Contexto
Você precisa montar a grade de um módulo trimestral (12 semanas). As aulas são distribuídas em 5 eixos:
1. Computação
2. Orientação
3. UX
4. Matemática
5. Negócios & Liderança


Regra pedagógica: Orientação e Computação devem ter maior participação no trimestre do que os demais eixos.
Os professores não têm dia fixo: eles informam disponibilidade por janelas de datas e blocos de horário, podendo variar semana a semana.


---


Entradas (Modelagem)


1) Estrutura do trimestre:
- weeks = 12
- Slots de aula por semana (exemplo): Mon..Fri, 08-10, 10-12, 14-16, 16-18 (conjunto fixo de slots).


2) Eixos e proporções (Target trimestral padrão):
- Orientação: 30%
- Computação: 30%
- UX: 15%
- Matemática: 15%
- Negócios & Liderança: 10%
Total = 100%


3) Professores (Cada professor p possui):
- eixos_habilitados (1..5)
- custo_hora
- max_horas_por_semana
- disponibilidade: lista de slots disponíveis por semana
- min_horas_trimestre (opcional)
- preferencias (opcional): ex. evitar manhã, preferir 2h seguidas, etc.


---


Saída Esperada
Um plano trimestral contendo:
- Para cada semana w: lista de aulas alocadas (slot, eixo, professor).
- Total de horas por eixo no trimestre.
- Total de horas por professor por semana e no trimestre.
- Custo total do período.


---


Restrições (Hard Constraints)
1. Um slot recebe no máximo 1 aula.
2. Professor só pode ser alocado em slots em que está disponível.
3. Professor não pode exceder max_horas_por_semana.
4. Cada aula pertence a exatamente 1 eixo.
5. Proporções trimestrais devem ser atingidas com tolerância (ex.: ±2% por eixo).
6. Orientação + Computação devem ser os eixos majoritários.


---


Função Objetivo (Otimização)
Minimizar uma combinação ponderada de:
1. Custo total (Principal).
2. Penalidade por desvio das proporções por eixo.
3. Penalidade por “fragmentação” (ex.: professor com aulas espalhadas em slots isolados).
4. Penalidade por “instabilidade” (ex.: eixo sem cobertura em várias semanas seguidas).


---


Tarefas do Candidato


Parte A — Solução Base (Obrigatória)
- Criar um algoritmo inicial (greedy ou heurística simples) que gere uma alocação válida.
- Explicar o funcionamento e a complexidade.


Parte B — Análise de Complexidade (Obrigatória)
No vídeo, responder:
- Tempo e espaço em função de: P (professores), S (slots/semana), W (12 semanas), E (5 eixos).
- Onde está o gargalo?
- Como escala para (P=200, S=100) e para (P=2000, S=400)?


Parte C — Otimização (Obrigatória)
Propor uma solução avançada (ex: ILP/MIP, Min-cost flow, Simulated Annealing ou Greedy + Repair).
Deve demonstrar no desenho:
- Variáveis de decisão e restrições.
- Como mede e corrige o erro de proporção.


Parte D — Cenário de Produção (Obrigatória)
Como lidar com mudanças (alteração de disponibilidade, novo professor, mudança de proporção)?
- Abordar: reotimização incremental, cache de viabilidade ou particionamento.


---


Entrega (Vídeo + Arquivos)
1. Vídeo (até 20 min): Explicação da modelagem, análise Big-O e estratégia de otimização (usando Excalidraw ou similar).
2. Código: Implementação em qualquer linguagem + README com instruções de execução.
3. Dados: Arquivo de entrada de exemplo (JSON ou CSV).


Diferenciais:
- Suavização semanal das proporções (não apenas trimestral).
- Estratégia de "Repair" para conflitos insolúveis.
- Métrica de Fairness entre professores habilitados no mesmo eixo.


