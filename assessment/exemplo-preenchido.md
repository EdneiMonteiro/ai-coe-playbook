# Exemplo preenchido: assessment da Meridional Seguros S.A.

> **Organização fictícia.** Este documento existe para mostrar, de ponta a ponta, como o assessment funciona na prática: notas com evidência, regras de contenção acionadas, vetos operacionais e a destilação para o board pack. Nomes, números e evidências são inventados. Os cálculos podem ser reproduzidos com a calculadora em [`calculadora/`](calculadora/), usando [`notas-exemplo.csv`](calculadora/notas-exemplo.csv) e [`contexto-exemplo.json`](calculadora/contexto-exemplo.json).

## 1. Identificação e escopo

| Campo | Valor |
|---|---|
| Organização avaliada | Meridional Seguros S.A. (fictícia; seguradora regulada, ~4.000 colaboradores) |
| Data | Agosto de 2026 |
| Sponsor executivo | CTO (sponsor do CoE de IA desde março de 2025) |
| Modo de aplicação | Auditoria/investimento (2 avaliadores, matriz de rastreabilidade completa) |
| Escopo organizacional | CoE de IA corporativo + unidades de Sinistros, Atendimento e Subscrição |
| Escopo técnico | GenAI, RAG, ML clássico; sem agentes com execução de ações |
| Amostra avaliada | 3 soluções em produção (todas as existentes) |

## 2. Amostra de soluções

| Solução | Tipo | Situação | Exposição |
|---|---|---|---|
| Assistente de Apólices | Chatbot RAG sobre condições gerais de apólice | Produção há 7 meses | **Externa** (segurados no portal) |
| Copiloto de Sinistros | GenAI de apoio à análise de sinistros | Produção há 4 meses | Interna (analistas) |
| Classificador de Fraude | ML clássico de priorização de investigação | Produção há 2 anos | Interna (decisão com humano no loop) |

Flags de contexto derivadas da amostra: produção sim; GenAI/RAG em produção sim; exposição externa sim; sponsor claro sim; FRIA/DPIA aplicável realizada (DPIA do Assistente de Apólices registrada em 2026-02); **red teaming nunca executado** e **incident response de IA não exercitado** (ver vetos).

## 3. Notas por dimensão (com evidência resumida)

A escala e as rubricas por pergunta estão em [`criterios-pontuacao.md`](criterios-pontuacao.md) e [`questionario-assessment.md`](questionario-assessment.md). Confiança: A = alta, M = média.

### Estratégia e mandato: 3,00 (Nível 3)

| ID | Nota | Evidência observada | Conf. |
|---|---:|---|---|
| E1 | 3 | Charter aprovado em ata do comitê executivo; papéis conhecidos em Sinistros e Atendimento | A |
| E2 | 3 | Roadmap 2026 conecta casos, plataforma e governança às metas da companhia | A |
| E3 | 3 | Critérios de centralizar × federar aplicados nas decisões de Sinistros e Subscrição | M |
| E4 | 3 | Funding recorrente aprovado; showback mensal por unidade | A |
| E5 | 3 | Dashboard executivo trimestral com valor, risco, adoção e custo | A |

### Modelo operacional: 3,00 (Nível 3)

| ID | Nota | Evidência observada | Conf. |
|---|---:|---|---|
| M1 | 3 | Intake padronizado com 23 casos triados em 2026; critérios de valor/risco/dados | A |
| M2 | 3 | RACI usado nos 3 casos em produção, accountability rastreável | A |
| M3 | 3 | DoD de transição aplicado no Classificador de Fraude e no Copiloto de Sinistros | A |
| M4 | 3 | Squad de Atendimento desenvolveu o Assistente de Apólices sob padrões do CoE | M |
| M5 | 3 | Comitê mensal com decisões registradas e owners | A |

### Governança e risco: 2,00 (Nível 2)

| ID | Nota | Evidência observada | Conf. |
|---|---:|---|---|
| G1 | 3 | Os 3 casos em produção têm classificação formal de risco com owner e aprovação | A |
| G2 | 2 | Gates definidos, mas aplicados manualmente; sem bloqueio automático de release | A |
| G3 | 3 | Jurídico, privacidade e segurança acionados por critério documentado | A |
| G4 | **1** | Red teaming discutido em ata, nunca executado; sem waiver formal | A |
| G5 | **1** | Runbook genérico de TI; nunca exercitado para incidente de IA; sem severidade específica | A |

### Plataforma e arquitetura: 3,00 (Nível 3)

| ID | Nota | Evidência observada | Conf. |
|---|---:|---|---|
| P1 | 3 | Arquitetura de referência RAG versionada, usada pelos 2 casos GenAI | A |
| P2 | 3 | Catálogo com modelos homologados, owner e ambiente permitido | A |
| P3 | 3 | Landing zone com RBAC, segregação e promoção controlada | A |
| P4 | 3 | Guardrails de acesso, quotas, filtro de conteúdo e validação de schema em pipeline | M |
| P5 | 3 | Plataforma expõe logs, traces, métricas e custo para as 3 soluções | A |

### Dados e conhecimento: 2,60 (Nível 3)

| ID | Nota | Evidência observada | Conf. |
|---|---:|---|---|
| D1 | 3 | Fontes com owner, classificação e acesso aprovado | A |
| D2 | 2 | Base legal e retenção registradas; controles por regime de dado ainda parciais (logs de interação sem expurgo automatizado) | A |
| D3 | 3 | Corpus e índice versionados com SLA de atualização quinzenal | A |
| D4 | 3 | Qualidade e lineage verificados antes de produção; golden dataset com hash | M |
| D5 | 2 | Reuso existe entre Sinistros e Atendimento, sem catálogo formal de ativos | M |

### LLMOps/MLOps e evals: 2,00 (Nível 2)

| ID | Nota | Evidência observada | Conf. |
|---|---:|---|---|
| L1 | 3 | Releases rastreáveis até modelo, prompt, corpus e índice | A |
| L2 | 2 | Evals de groundedness e qualidade em piloto; sem separação safety × security nem thresholds por risco | A |
| L3 | 2 | Regressão executada manualmente a cada troca de modelo; sem gate bloqueante | A |
| L4 | 2 | Monitoramento ativo no Assistente de Apólices; parcial nas demais | M |
| L5 | **1** | Rollback de release existe; **sem kill switch ou fallback testado** para os casos GenAI | A |

### Portfólio e valor: 2,60 (Nível 3)

| ID | Nota | Evidência observada | Conf. |
|---|---:|---|---|
| V1 | 3 | Scorecard valor × risco × viabilidade no comitê mensal | A |
| V2 | 3 | Os 3 casos têm baseline e métrica de sucesso | A |
| V3 | 2 | Kill criteria definidos, aplicados uma única vez | M |
| V4 | 3 | Benefícios revisados por trimestre (deflexão de chamados, tempo de análise) | A |
| V5 | 2 | Mix existe, mas capacidade não é gerida por categoria | M |

### Capacitação e comunidade: 2,60 (Nível 3)

| ID | Nota | Evidência observada | Conf. |
|---|---:|---|---|
| C1 | 3 | AI literacy segmentado: operação, líderes e jurídico | A |
| C2 | 3 | Trilhas técnicas para engenharia e dados conectadas aos padrões | M |
| C3 | 3 | Champions ativos em 3 unidades com agenda mensal | A |
| C4 | 2 | Templates publicados, sem canal formal de feedback | A |
| C5 | 2 | Participação medida; aplicação prática ainda não | A |

### FinOps e sustentabilidade: 2,00 (Nível 2)

| ID | Nota | Evidência observada | Conf. |
|---|---:|---|---|
| F1 | 2 | Custo visível por ambiente; alocação por produto parcial | A |
| F2 | 2 | Budgets e alertas existem; sem circuit breaker automático | A |
| F3 | 3 | Ciclo de otimização trimestral com savings documentados (troca para modelo menor no Copiloto) | A |
| F4 | 2 | Custo por interação medido no Assistente de Apólices apenas | M |
| F5 | 1 | Sustentabilidade citada em princípios, sem critério aplicado | A |

### Operação e melhoria contínua: 2,40 (Nível 2)

| ID | Nota | Evidência observada | Conf. |
|---|---:|---|---|
| O1 | 3 | Toda produção tem owner operacional e escalação pós-handoff | A |
| O2 | 2 | SLO e runbook existem para o Classificador de Fraude; parciais nos casos GenAI | A |
| O3 | 3 | Postmortems com RCA e ações corretivas (2 incidentes de infraestrutura) | A |
| O4 | 2 | Revisão de padrões ocorre, sem cadência fixa | M |
| O5 | 2 | Feedback coletado; backlog de melhoria não priorizado por métricas | M |

## 4. Resultado consolidado

Saída da calculadora (`python calculadora-assessment.py notas-exemplo.csv contexto-exemplo.json`):

| Métrica | Resultado |
|---|---|
| Pontuação geral bruta (média simples) | **2,52** |
| Nível bruto | **Nível 3 (Habilitador)** |
| Contenções acionadas | 5 |
| **Nível final após contenções** | **Nível 2 (Executor)** |
| Vetos operacionais abertos | 2 |
| Confiança geral | Alta (evidência documental na maioria das perguntas) |

### Contenções acionadas

| Regra | Efeito |
|---|---|
| Produção/expansão sem incident response IA (G5 = 1) | Máximo nível 2 + **veto operacional** |
| Exposição externa sem AI red teaming ou waiver (G4 = 1) | Máximo nível 2 + **veto operacional** |
| L5 < 2 com GenAI/RAG em produção (sem kill switch/fallback testado) | Máximo nível 2 |
| Governança e risco < 3,0 | Máximo nível 3 |
| Operação e melhoria contínua < 3,0 com produção crítica | Máximo nível 3 |

### Vetos operacionais por caso

| Caso | Veto | Remediação exigida |
|---|---|---|
| Assistente de Apólices | Exposição externa sem red teaming | Red team cobrindo no mínimo LLM01, LLM02 e LLM06 (OWASP LLM Top 10) ou waiver formal aprovado por Segurança/Risco; kill switch testado |
| Copiloto de Sinistros | Produção sem incident response de IA | Runbook específico de IA com severidades, canal, owner de resposta e simulação executada |

**Expansões bloqueadas até remediação.** O nível 2 não impede a operação atual dos casos aprovados; impede novas produções e expansões dos casos vetados.

### Trava anti-gaming

Perguntas críticas com nota < 2: **G4, G5, L5.** Nenhuma pode ficar invisível na destilação executiva. Decisão registrada: os dois vetos acima cobrem G4 e G5; para L5, a permanência em produção foi aceita pelo CTO com prazo de 45 dias para kill switch testado, registrada em ata (condição de "aprovado com restrições" para os 3 casos).

### Alerta de consistência cruzada

P5 ≥ 3 com L4 ≤ 2: a plataforma oferece observabilidade, mas as soluções não a instrumentam por completo ("plataforma sem adoção"). Ação registrada: amostragem de logs/traces das 3 soluções confirmou instrumentação plena apenas no Assistente de Apólices.

## 5. Board pack resultante (resumo)

A versão completa segue o [`board-pack-template.md`](board-pack-template.md).

**Mensagem única:** "Somos nível 2 com dois vetos abertos; pedimos R$ 1,2 mi e 90 dias para destravar red teaming, incident response e kill switch antes de qualquer expansão."

| Decisão pedida | Prazo | Owner executivo |
|---|---|---|
| Aprovar investimento de remediação e congelar expansões até fechar os 2 vetos | 15 dias | CTO |

**Racional:** a média 2,52 esconderia lacunas críticas; as contenções mostram que a base de governança operacional (incidente, red team, kill switch) não acompanhou a velocidade de entrada em produção. O custo de remediação é uma fração do custo de inação.

| Horizonte | Consequência provável se nada mudar | Proxy usado |
|---|---|---|
| 30 dias | Expansão do Assistente a novos produtos bloqueada; meta de deflexão de chamados do trimestre comprometida | Custo de oportunidade (R$ 180 mil/trimestre) |
| 90 dias | Incidente de IA sem resposta estruturada em canal externo; exposição LGPD com dados de segurados | Multa dimensionada pelo Art. 52 (teto de R$ 50 mi por infração) + remediação |
| 180 dias | Perda de credibilidade do CoE junto às unidades; retorno ao shadow AI | Churn interno de demanda + retrabalho |

**Próximos 30 dias:** (1) contratar red team externo para o Assistente de Apólices, owner: Segurança, bloqueio removido: veto 1; (2) escrever e simular runbook de incidente de IA, owner: CoE + SRE, bloqueio: veto 2; (3) implementar e testar kill switch nos 2 casos GenAI, owner: Plataforma, bloqueio: condição L5.

## 6. Como reproduzir

```bash
cd assessment/calculadora
python calculadora-assessment.py notas-exemplo.csv contexto-exemplo.json
python calculadora-assessment.py notas-exemplo.csv contexto-exemplo.json --pesos regulado
```

Para usar na sua organização, copie os dois arquivos de exemplo, substitua as notas e as flags de contexto pela sua realidade e rode a calculadora. O resultado numérico não substitui o relatório auditável ([`relatorio-template.md`](relatorio-template.md)): a trilha pergunta, evidência, nota e confiança continua obrigatória.
