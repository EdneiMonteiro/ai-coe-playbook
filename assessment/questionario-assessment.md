# Questionário de assessment de maturidade do CoE de IA

Use a escala definida em [`criterios-pontuacao.md`](criterios-pontuacao.md):

- **0** — inexistente ou não evidenciado.
- **1** — ad hoc, informal, dependente de indivíduos.
- **2** — definido parcialmente, usado em pilotos ou pelo CoE central.
- **3** — padronizado, adotado por múltiplos times, com evidência recorrente.
- **4** — medido, otimizado, auditável e continuamente melhorado.

Cada resposta deve citar evidências: documentos, links, atas, repositórios, dashboards, exemplos de projetos, políticas, runbooks, logs ou registros de decisão.

## 1. Estratégia e mandato

| ID | Pergunta | Evidências esperadas |
|---|---|---|
| E1 | Existe charter formal do CoE de IA com missão, escopo, fora de escopo e sponsor? | Charter aprovado, ata de aprovação, sponsor definido. |
| E2 | O CoE possui roadmap conectado à estratégia de negócio e tecnologia? | Roadmap, OKRs, plano anual, estratégia corporativa. |
| E3 | Há critérios explícitos para decidir o que o CoE centraliza e o que federa? | Modelo operacional, direitos de decisão, RACI. |
| E4 | O funding do CoE e das iniciativas de IA é claro e recorrente? | Orçamento, modelo de chargeback/showback, plano de capacidade. |
| E5 | Existem métricas executivas de valor, risco, adoção, custo e qualidade? | Dashboard executivo, KPIs, reports periódicos. |

## 2. Modelo operacional

| ID | Pergunta | Evidências esperadas |
|---|---|---|
| M1 | Existe processo de intake para novos casos de uso de IA? | Formulário, workflow, backlog, critérios de triagem. |
| M2 | Os papéis de CoE, produto, plataforma, dados e risco/compliance estão definidos? | RACI, operating model, organograma, comunidades. |
| M3 | Há critérios de handoff de PoC/MVP para squad de produto? | Definition of Done, checklist de transição, ownership formal. |
| M4 | O CoE atua como habilitador, não apenas como fábrica de software? | Templates, consultorias, office hours, squads autônomos. |
| M5 | Existem fóruns regulares para priorização, governança e revisão de portfólio? | Atas, calendário, comitês, decisões registradas. |

## 3. Governança e risco

| ID | Pergunta | Evidências esperadas |
|---|---|---|
| G1 | Casos de uso são classificados por risco antes de desenvolvimento com dados reais? | Template de avaliação, registros de classificação, aprovações. |
| G2 | Existem gates proporcionais ao risco para PoC, MVP e produção? | Workflow de aprovação, policy-as-code, evidências de gate. |
| G3 | Segurança, privacidade, jurídico, risco e compliance participam dos casos relevantes? | Atas, pareceres, aprovações, exceções registradas. |
| G4 | Há prática de AI red teaming para casos de alto risco, agentes ou exposição externa? | Relatórios de red teaming, backlog de remediação, retestes. |
| G5 | Existe processo de incidente para falhas, abuso, vazamento, alucinações críticas ou uso indevido? | Runbook, canal de incidente, simulações, postmortems. |

## 4. Plataforma e arquitetura

| ID | Pergunta | Evidências esperadas |
|---|---|---|
| P1 | Há arquitetura de referência para RAG, agentes, copilots e ML clássico? | Diagramas, ADRs, blueprints, repositórios-modelo. |
| P2 | Existe catálogo de modelos, ferramentas, frameworks e serviços aprovados? | Catálogo, critérios de homologação, owners. |
| P3 | Ambientes de desenvolvimento, teste e produção têm segregação e controles consistentes? | Landing zone, IaC, RBAC, redes, políticas. |
| P4 | Guardrails técnicos são automatizados sempre que possível? | Policies, CI/CD checks, secrets scanning, filtros, quotas. |
| P5 | A plataforma oferece observabilidade de qualidade, custo, latência, uso e risco? | Dashboards, logs, traces, métricas de modelos e aplicações. |

## 5. Dados e conhecimento

| ID | Pergunta | Evidências esperadas |
|---|---|---|
| D1 | Fontes de dados usadas por IA possuem owner, classificação e política de acesso? | Catálogo de dados, data owners, matriz de acesso. |
| D2 | Dados pessoais, sensíveis, regulados ou confidenciais são tratados com controles específicos? | DPIA/LIA quando aplicável, mascaramento, retenção, consentimento/base legal. |
| D3 | Bases de conhecimento para RAG têm curadoria, versionamento e ciclo de atualização? | Pipeline de ingestão, versionamento, owner, SLAs de atualização. |
| D4 | Há critérios de qualidade, relevância e validade para documentos e datasets? | Regras de qualidade, validações, lineage, testes de recuperação. |
| D5 | A organização evita duplicação de bases e reutiliza ativos de conhecimento? | Catálogo, reutilização entre produtos, métricas de duplicidade. |

## 6. LLMOps/MLOps e evals

| ID | Pergunta | Evidências esperadas |
|---|---|---|
| L1 | Prompts, modelos, embeddings, datasets e configurações são versionados? | Repositórios, tags, model registry, prompt registry. |
| L2 | Existem evals mínimos para qualidade, segurança, groundedness, viés, custo e latência? | Suites de eval, relatórios, thresholds, critérios de aceite. |
| L3 | Mudanças de modelo, prompt, ferramenta ou política de recuperação disparam regressão? | Golden datasets, pipeline de regressão, histórico de resultados. |
| L4 | Há monitoramento em produção para drift, degradação, alucinação e incidentes? | Dashboards, alertas, amostragem, revisão humana. |
| L5 | Existem mecanismos de fallback, rollback e desligamento controlado? | Runbooks, feature flags, rollback plan, kill switch. |

## 7. Portfólio e valor

| ID | Pergunta | Evidências esperadas |
|---|---|---|
| V1 | Casos de uso são priorizados por valor, risco, viabilidade e alinhamento estratégico? | Scorecard, comitê de portfólio, matriz valor/risco. |
| V2 | Cada iniciativa possui business case ou hipótese de valor mensurável? | Business case, OKRs, métricas de sucesso, baseline. |
| V3 | Há critérios para encerrar PoCs sem valor ou com risco/custo desproporcional? | Kill criteria, decisões de descontinuação, lessons learned. |
| V4 | Benefícios prometidos são acompanhados após entrada em produção? | Realização de benefícios, dashboard, revisão pós-implantação. |
| V5 | O portfólio equilibra quick wins, fundações de plataforma e casos estratégicos? | Roadmap, capacidade alocada, categorias de investimento. |

## 8. Capacitação e comunidade

| ID | Pergunta | Evidências esperadas |
|---|---|---|
| C1 | Existe programa de AI literacy para usuários, líderes e áreas de negócio? | Conteúdo, trilhas, presença, avaliações. |
| C2 | Existem trilhas técnicas para engenharia, dados, segurança, arquitetura e produto? | Currículos, bootcamps, certificações, labs. |
| C3 | Há comunidade de prática ou rede de champions ativa? | Agenda, participação, backlog, contribuições. |
| C4 | O CoE publica templates, guias e exemplos reutilizáveis? | Repositórios, documentação, playbooks, blueprints. |
| C5 | A organização mede adoção e efetividade da capacitação? | Métricas de participação, proficiência, NPS, aplicação prática. |

## 9. FinOps e sustentabilidade

| ID | Pergunta | Evidências esperadas |
|---|---|---|
| F1 | Custos de IA são rastreados por produto, área, ambiente e modelo? | Dashboards, tags, billing export, showback/chargeback. |
| F2 | Há budgets, alertas e limites de consumo para workloads de IA? | Budgets, quotas, alertas, políticas de consumo. |
| F3 | Existe otimização recorrente de modelo, prompt, cache, batching e infraestrutura? | Relatórios de otimização, ADRs, experimentos, savings. |
| F4 | Custo por interação, por documento, por caso ou por decisão é acompanhado? | Métricas unitárias, baseline, tendência. |
| F5 | Sustentabilidade é considerada em escolhas de modelo, região, treinamento e inferência? | Critérios arquiteturais, documentação, métricas ambientais quando disponíveis. |

## 10. Operação e melhoria contínua

| ID | Pergunta | Evidências esperadas |
|---|---|---|
| O1 | Soluções de IA em produção têm owner operacional claro? | Owner, RACI, suporte, escalação. |
| O2 | Existem SLOs/SLAs e runbooks para aplicações críticas de IA? | SLOs, runbooks, planos de suporte, on-call quando aplicável. |
| O3 | Incidentes e problemas são analisados com postmortems e ações corretivas? | Postmortems, RCA, backlog de remediação. |
| O4 | O CoE revisa periodicamente padrões, ferramentas, modelos e riscos emergentes? | Revisões trimestrais, ADRs, changelog de padrões. |
| O5 | Há processo de melhoria contínua baseado em métricas e feedback dos times? | Pesquisas, métricas de adoção, backlog de melhoria, releases do playbook. |

