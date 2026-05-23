# Critérios de pontuação do assessment

O assessment separa duas decisões que não devem ser misturadas:

1. **Maturidade do CoE de IA** — nota 0–4 por pergunta, dimensão e nível geral.
2. **Go/no-go operacional por caso de uso** — decisão de permitir, restringir, pausar ou bloquear produção/expansão.

Uma organização pode ter maturidade razoável e, ainda assim, ter **veto operacional** em um caso específico. A pontuação mede capacidade organizacional; os gates protegem produção, clientes, usuários, dados, conformidade e operação.

Este assessment não certifica conformidade regulatória, não substitui auditoria jurídica, não substitui auditoria de sistema de gestão e não constitui parecer formal de aderência a ISO/IEC 42001, EU AI Act, LGPD, GDPR ou regulações setoriais. Referências normativas são usadas como heurística de medição, rastreabilidade e organização de evidências.

## Glossário operacional

| Termo | Definição | Efeito no assessment |
|---|---|---|
| PoC | Experimento controlado para testar viabilidade, sem dependência operacional, sem decisão real automatizada e sem exposição ampla. | Pode operar com controles simplificados, desde que dados reais/sensíveis tenham aprovação explícita. |
| MVP | Piloto limitado, com usuários controlados, owner de negócio/técnico, critérios de sucesso e plano de encerramento ou evolução. | Exige classificação de risco, owner, avaliação de dados e critérios de monitoramento. |
| Produção | Uso por usuários reais, tráfego real, decisão real, processo operacional ou integração que afete serviço, cliente, cidadão, colaborador, receita, custo ou compliance. | Ativa gates operacionais mínimos. |
| Produção crítica | Produção com impacto material em cliente/cidadão/colaborador, receita, compliance, segurança, dados sensíveis/regulados, processo crítico ou operação de alto volume. | Ativa gates reforçados e pode acionar contenções de maturidade. |
| Exposição externa | Uso por clientes, cidadãos, parceiros, fornecedores, público geral ou qualquer usuário fora do time operador/controlado. | Eleva exigência de transparência, red teaming, monitoramento, incident response e fallback. |
| Expansão | Aumento material de usuários, países, dados, ferramentas, autonomia, integrações, canais ou criticidade de um caso existente. | Deve ser tratado como nova decisão go/no-go. |
| Alto risco | Caso com dados sensíveis/regulados, decisão relevante, agente com ferramentas, exposição externa, impacto legal/financeiro/social ou enquadramento setorial/regulatório relevante. | Exige controles reforçados, aprovação formal e, quando aplicável, FRIA/DPIA. |
| FRIA/DPIA | Avaliação formal de impacto em direitos fundamentais, privacidade ou proteção de dados, quando exigida por regulação, política interna ou natureza do caso. | Ausência quando aplicável gera veto operacional. |

## Escala por pergunta

Use a escala 0–4, com evidência verificável. Não arredonde notas usadas em contenções.

| Pontuação | Significado | Critério prático |
|---|---|---|
| 0 | Inexistente | Não há prática, artefato ou evidência verificável. |
| 1 | Ad hoc | Existe informalmente, depende de indivíduos ou aparece em caso isolado. |
| 2 | Definido parcialmente | Existe prática documentada, mas restrita ao CoE central, a pilotos ou a poucos times. |
| 3 | Padronizado | A prática é adotada de forma recorrente em pelo menos dois domínios/BUs ou em múltiplas soluções relevantes, com owner e evidência de uso. |
| 4 | Otimizado | A prática é medida, auditável, revisada periodicamente e melhorada com base em métricas, incidentes, custo, risco ou feedback. |

O arquivo [`questionario-assessment.md`](questionario-assessment.md) detalha, por pergunta, o que caracteriza evidência mínima para notas 2, 3 e 4. As notas 0 e 1 seguem a régua geral acima.

## Gates de go/no-go operacional

Os gates abaixo não são apenas tetos de maturidade. Eles podem bloquear produção ou expansão até remediação.

| Gate | Quando se aplica | Veto operacional |
|---|---|---|
| Classificação formal de risco | Qualquer MVP, produção ou expansão com dados reais, usuários reais ou decisão real | Sem classificação formal e owner de risco, não avança. |
| Avaliação de dados e privacidade | Qualquer uso de dados pessoais, sensíveis, regulados, confidenciais, logs de interação, corpus RAG ou índice vetorial | Sem base legal/finalidade/retenção/acesso/expurgo quando aplicável, não avança para produção. |
| FRIA/DPIA ou avaliação equivalente | Quando exigido por regulação, política interna, setor, dados, impacto em pessoas ou classificação de alto risco | Sem avaliação ou dispensa formal justificada, não avança. |
| AI red teaming | Produção crítica, exposição externa, agentes com ferramentas, casos de alto risco ou sistemas generativos com impacto material | Sem red team, waiver formal ou controles compensatórios aprovados, não avança. |
| Incident response IA | Qualquer produção ou expansão relevante | Sem runbook, canal de incidente, owner de resposta e critério de escalação, não avança. |
| Evals e regressão | Sistemas generativos, RAG, agentes, copilots e automação decisória | Sem thresholds mínimos e regressão para mudanças relevantes, não avança para produção. |
| Fallback, rollback ou kill switch | Qualquer produção; obrigatório reforçado para agentes, alto risco ou exposição externa | Sem mecanismo testado de interrupção/reversão, não avança. |
| Controles de agentes | Agentes ou fluxos com uso de ferramentas, APIs, execução de ações ou multi-agent | Sem least privilege, allowlist de ferramentas, trilha de auditoria, limites de autonomia e aprovação humana para ações irreversíveis, não avança. |

Status permitidos para cada caso avaliado:

| Status | Significado |
|---|---|
| Aprovado | Gates atendidos e risco residual aceito pelo papel accountable. |
| Aprovado com restrições | Pode avançar com prazo, escopo ou controles compensatórios explícitos. |
| Veto operacional aberto | Produção/expansão bloqueada até remediação. |
| Bloqueado | Caso vedado por lei, política, risco inaceitável ou ausência de controle essencial. |

## Cálculo por dimensão

Cada dimensão tem cinco perguntas.

```text
pontuação_da_dimensão = soma_das_perguntas_da_dimensão / 5
```

Mapeamento para nível:

| Média exata da dimensão | Nível |
|---|---|
| 0,00 a 1,49 | Nível 1 — Reativo |
| 1,50 a 2,49 | Nível 2 — Executor |
| 2,50 a 3,49 | Nível 3 — Habilitador |
| 3,50 a 4,00 | Nível 4 — Transformador |

Não arredonde médias para ativar ou desativar contenções. Uma dimensão com 1,99 continua abaixo de 2,0.

## Cálculo do nível geral

Use a média simples das dez dimensões como ponto de partida:

```text
pontuação_geral = soma_das_médias_das_dimensões / 10
```

Depois aplique regras de contenção, gates operacionais e regras de consistência cruzada.

## Regras de contenção de maturidade

| Regra | Efeito |
|---|---|
| Governança e risco < 2,0 | Nível geral máximo = 2 |
| Plataforma e arquitetura < 2,0 | Nível geral máximo = 2 |
| LLMOps/MLOps e evals < 2,0 para GenAI/RAG/agentes em produção | Nível geral máximo = 2 |
| Operação e melhoria contínua < 2,0 com qualquer solução em produção | Nível geral máximo = 2 |
| Não há sponsor executivo claro | Nível geral máximo = 2 |
| Há caso de alto risco sem classificação formal | Nível geral máximo = 2 e veto operacional no caso |
| Há produção/expansão sem incident response IA | Nível geral máximo = 2 e veto operacional no caso |
| Há produção crítica ou exposição externa sem AI red teaming ou waiver formal | Nível geral máximo = 2 e veto operacional no caso |
| FRIA/DPIA aplicável ausente | Nível geral máximo = 2 e veto operacional no caso |
| L3 < 2 para GenAI/RAG/agentes em produção | Nível geral máximo = 2 |
| L5 < 2 para GenAI/RAG/agentes em produção | Nível geral máximo = 2 |
| L5 < 3 para agentes externos, agentes de alto risco ou agentes com ação irreversível | Nível geral máximo = 2 e veto operacional no caso |
| Governança e risco < 3,0 | Nível geral máximo = 3 |
| Operação e melhoria contínua < 3,0 com produção crítica | Nível geral máximo = 3 |

### Trava genérica anti-gaming para perguntas críticas

| Regra | Efeito |
|---|---|
| Qualquer pergunta marcada como **crítica** (em qualquer dimensão) com nota < 2 e sem gate operacional/contenção específica declarada | Acionar gate de revisão obrigatória: o relatório deve declarar explicitamente (a) por que o caso de uso pode permanecer em produção apesar da nota baixa, **OU** (b) registrar veto operacional aberto até remediação. O board pack deve refletir essa decisão; nota crítica < 2 não pode ser invisibilizada na destilação executiva. |

Esta trava genérica evita que uma pergunta crítica receba nota baixa sem consequência operacional ou executiva, mesmo quando não há contenção específica nominada nas regras acima. Não substitui as contenções nomeadas; complementa-as como rede de segurança.

## Regras de consistência cruzada

| Regra | Interpretação | Ação obrigatória |
|---|---|---|
| P5 alto e L4 baixo | Plataforma oferece observabilidade, mas soluções não instrumentam/operam essa capacidade. | Se P5 ≥ 3 e L4 ≤ 2, registrar risco "plataforma sem adoção" e amostrar logs/traces de pelo menos três soluções em produção, ou todas se houver menos de três. |
| P5 e L4 usam a mesma evidência | A mesma evidência não prova capacidade de plataforma e uso ativo por solução. | P5 pontua telemetria oferecida pela plataforma; L4 pontua instrumentação ativa por solução. Nota ≥ 3 em ambas exige evidência distinta ou rastreada por aplicação. |
| P5 alto e F1/F4 baixo | Telemetria existe, mas custo não está conectado à operação. | Registrar lacuna FinOps e revisar se dashboards capturam custo unitário por produto/caso. |
| G1/G3 alto e D2 baixo | Processo de governança existe, mas controles de dados não sustentam a aprovação. | Registrar risco de compliance de dados e revisar evidência de base legal, retenção, acesso e expurgo. |
| M3 alto e O1 baixo | Handoff declarado, mas ownership operacional não existe. | Registrar dívida de transição: produto preso no CoE ou sem owner de produção. |

## Pesos opcionais

A média simples é recomendada para a primeira aplicação. Pesos alternativos só podem ser usados quando o relatório registrar: regulação aplicável, racional de cada alteração, comparação com o peso padrão 10% por dimensão e análise de sensibilidade mostrando se o nível final mudaria com a média simples. Se esse racional não for documentado, use 10% por dimensão.

Em organizações reguladas, pode-se usar pesos maiores para governança, risco, operação e dados:

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

### Definição de "dimensão crítica"

Para efeito de análise de sensibilidade, regras de contenção e perguntas marcadas como críticas, considera-se **dimensão crítica** aquela que atende a pelo menos um dos critérios abaixo:

- **(a) Peso nominal ≥ 15%** no esquema de pesos aplicado.
- **(b) Dimensão diretamente referenciada por exposição regulatória material** ao escopo avaliado (ex.: Governança e risco e Dados e conhecimento quando a organização opera sob LGPD, GDPR, EU AI Act ou regulação setorial).
- **(c) Dimensão técnica de produção** quando o escopo inclui sistemas generativos, RAG ou agentes (em particular: Plataforma e arquitetura, Dados e conhecimento, LLMOps/MLOps e evals, Operação e melhoria contínua).

A classificação de dimensões críticas deve ser registrada no relatório antes de aplicar análise de sensibilidade, regras de contenção e gates operacionais.

### Registro obrigatório quando pesos alternativos forem usados

| Item | Deve constar no relatório |
|---|---|
| Regulação ou contexto que justifica pesos | Ex.: setor financeiro regulado, saúde, infraestrutura crítica, exigência interna de risco. |
| Racional por dimensão alterada | Por que o peso foi elevado ou reduzido. |
| Comparação com peso padrão | Pontuação e nível com 10% por dimensão versus pontuação ponderada. |
| Análise de sensibilidade | Variação obrigatória de ±2pp por dimensão crítica e três cenários (worst/expected/best); registrar se decisão muda entre cenários. |
| Aprovação | Owner metodológico nominado; em modo auditoria/investimento, aprovador dos pesos deve ser **avaliador independente diferente do sponsor avaliado**; em modo diagnóstico interno, declarar explicitamente no board pack quando os pesos foram aprovados pelo próprio sponsor avaliado. |

## Evidência, amostragem e confiança

O assessment deve avaliar evidência operacional, não intenção. Registre evidência positiva e negativa.

| Confiança | Descrição | Efeito |
|---|---|---|
| Alta | Evidência documental, recente, rastreável e usada em múltiplos casos. | Nota mantida. |
| Média | Evidência existe, mas é parcial, desatualizada ou restrita a poucos casos. | Nota mantida com ressalva. |
| Baixa | Evidência baseada principalmente em entrevista, intenção declarada ou artefato não observado. | Em modo auditoria/investimento, reduzir a nota da pergunta em 0,5 ou marcar inconclusivo. |
| Inconclusiva | Evidência insuficiente para pontuar defensavelmente. | Não usar para afirmar maturidade; tratar como lacuna até validação. |

### Amostragem mínima

- Se houver soluções em produção, amostrar pelo menos **três soluções** por dimensão operacionalmente relevante; se houver menos de três, avaliar todas.
- Para produção crítica, exposição externa ou alto risco, incluir pelo menos um caso crítico na amostra.
- Para LLMOps/MLOps, a amostra deve incluir versões de modelo/prompt/corpus, histórico de evals, incidentes e evidência de rollback/fallback quando aplicável.
- Para dados/RAG, a amostra deve incluir corpus, índice vetorial, política de recuperação, retenção, acesso e expurgo quando aplicável.

### Matriz de rastreabilidade obrigatória

Para cada pergunta, o relatório deve registrar:

```text
ID da pergunta → evidência observada → evidência negativa → nota → confiança → avaliador → ressalvas → ação recomendada
```

### Divergência entre avaliadores

- Diferença maior que 1 ponto em qualquer pergunta exige reconciliação documentada.
- Se a divergência persistir, acionar terceiro avaliador ou marcar a pergunta como inconclusiva.
- Em modo auditoria/investimento, perguntas críticas inconclusivas não podem sustentar nível 3 ou 4.

## Modo diagnóstico vs modo auditoria/investimento

| Modo | Uso | Rigor mínimo |
|---|---|---|
| Diagnóstico interno | Baseline, melhoria interna, priorização inicial | Um avaliador, evidências principais, amostragem proporcional e ressalvas explícitas. |
| Auditoria/investimento | Board pack, decisão de funding, aplicação em cliente, organização regulada ou produção crítica | Dois avaliadores, amostragem mínima, matriz de rastreabilidade completa, tratamento formal de divergência e gates go/no-go. |

## Interpretação recomendada

| Nível geral | Interpretação | Próximo foco |
|---|---|---|
| Nível 1 — Reativo | A organização está experimentando IA sem sistema operacional claro. | Mandato, sponsor, triagem, padrões mínimos e controle de risco básico. |
| Nível 2 — Executor | O CoE existe e entrega, mas ainda concentra execução e conhecimento. | Minimum Viable Standards, plataforma inicial, handoff e capacitação. |
| Nível 3 — Habilitador | Adoção começa a escalar com padrões e governança distribuída. | Guardrails automatizados, evals contínuos, FinOps, handoff e comunidades. |
| Nível 4 — Transformador | IA opera como capacidade organizacional, com CoE consultivo. | Otimização contínua, inovação responsável e evolução do modelo operacional. |
