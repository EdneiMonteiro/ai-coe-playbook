# Critérios de pontuação do assessment

O assessment usa uma escala 0–4 por pergunta, agregada por dimensão e depois consolidada em nível geral.

## Escala por pergunta

| Pontuação | Significado | Critério prático |
|---|---|---|
| 0 | Inexistente | Não há prática, artefato ou evidência. |
| 1 | Ad hoc | Existe de forma informal, dependente de indivíduos ou aplicada apenas em casos isolados. |
| 2 | Definido parcialmente | Existe prática documentada, mas limitada ao CoE central, a pilotos ou a poucos times. |
| 3 | Padronizado | A prática é adotada de forma recorrente por múltiplos times, com owner e evidências consistentes. |
| 4 | Otimizado | A prática é medida, auditável, melhorada continuamente e integrada ao modelo operacional. |

## Cálculo por dimensão

Cada dimensão tem cinco perguntas.

```text
pontuação_da_dimensão = soma_das_perguntas_da_dimensão / 5
```

Mapeamento para nível:

| Média da dimensão | Nível |
|---|---|
| 0,00 a 1,49 | Nível 1 — Reativo |
| 1,50 a 2,49 | Nível 2 — Executor |
| 2,50 a 3,49 | Nível 3 — Habilitador |
| 3,50 a 4,00 | Nível 4 — Transformador |

## Cálculo do nível geral

Use a média simples das dez dimensões como ponto de partida:

```text
pontuação_geral = soma_das_médias_das_dimensões / 10
```

Depois aplique as regras de contenção abaixo. Elas evitam que uma organização seja classificada como madura quando possui lacunas críticas em risco, operação ou governança.

## Regras de contenção

| Regra | Efeito |
|---|---|
| Se Governança e risco < 2,0 | Nível geral máximo = 2 |
| Se Operação e melhoria contínua < 2,0 e houver soluções em produção | Nível geral máximo = 2 |
| Se Plataforma e arquitetura < 2,0 | Nível geral máximo = 2 |
| Se LLMOps/MLOps e evals < 2,0 para soluções generativas em produção | Nível geral máximo = 2 |
| Se não houver sponsor executivo claro | Nível geral máximo = 2 |
| Se houver casos de alto risco sem classificação formal | Nível geral máximo = 2 |
| Se Governança e risco < 3,0 | Nível geral máximo = 3 |
| Se Operação e melhoria contínua < 3,0 e houver produção crítica | Nível geral máximo = 3 |

## Pesos opcionais

A média simples é recomendada para a primeira aplicação. Em organizações reguladas, pode-se usar pesos maiores para governança, risco, operação e dados:

| Dimensão | Peso padrão | Peso para organização regulada |
|---|---:|---:|
| Estratégia e mandato | 10% | 10% |
| Modelo operacional | 10% | 10% |
| Governança e risco | 10% | 15% |
| Plataforma e arquitetura | 10% | 10% |
| Dados e conhecimento | 10% | 15% |
| LLMOps/MLOps e evals | 10% | 10% |
| Portfólio e valor | 10% | 10% |
| Capacitação e comunidade | 10% | 5% |
| FinOps e sustentabilidade | 10% | 5% |
| Operação e melhoria contínua | 10% | 10% |

## Evidência e confiança

Além da pontuação, registre o nível de confiança da evidência:

| Confiança | Descrição |
|---|---|
| Alta | Evidência documental, recente e usada em múltiplos casos. |
| Média | Evidência existe, mas é parcial, desatualizada ou restrita a poucos casos. |
| Baixa | Evidência baseada principalmente em entrevista ou intenção declarada. |

Uma dimensão com pontuação alta e confiança baixa deve ser marcada como **risco de validação**.

## Interpretação recomendada

| Nível geral | Interpretação | Próximo foco |
|---|---|---|
| Nível 1 — Reativo | A organização está experimentando IA sem sistema operacional claro. | Mandato, sponsor, triagem, padrões mínimos e controle de risco básico. |
| Nível 2 — Executor | O CoE existe e entrega, mas ainda concentra execução e conhecimento. | Minimum Viable Standards, plataforma inicial, handoff e capacitação. |
| Nível 3 — Habilitador | Adoção começa a escalar com padrões e governança distribuída. | Guardrails automatizados, evals contínuos, FinOps e comunidades. |
| Nível 4 — Transformador | IA opera como capacidade organizacional, com CoE consultivo. | Otimização contínua, inovação responsável e evolução do modelo operacional. |

