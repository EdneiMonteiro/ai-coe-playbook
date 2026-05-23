# Modelo de maturidade do CoE de IA

Este modelo operacionaliza os quatro níveis descritos no artigo principal. Ele é inspirado em lógica de maturidade tipo CMMI, mas adaptado para CoEs de IA, IA generativa, RAG, agentes, governança, plataforma e LLMOps/MLOps.

## Níveis

| Nível | Nome | Característica dominante | Resultado esperado |
|---|---|---|---|
| 1 | Reativo | Experimentos isolados e sem coordenação | Reconhecer lacunas, definir mandato e obter patrocínio executivo. |
| 2 | Executor | CoE centralizado entrega primeiros PoCs/MVPs | Criar padrões mínimos, demonstrar valor e formar capacidades básicas. |
| 3 | Habilitador | Plataforma, padrões e guardrails permitem execução distribuída | Escalar com governança, transferir ownership e reduzir gargalos do CoE. |
| 4 | Transformador | CoE consultivo, IA integrada à estratégia e operação | Melhorar continuamente, medir valor e operar IA como capacidade organizacional. |

## Dimensões avaliadas

| Dimensão | O que avalia | Sinais de maturidade |
|---|---|---|
| 1. Estratégia e mandato | Clareza de propósito, patrocínio, escopo e direitos de decisão | Charter aprovado, sponsor ativo, roadmap e funding alinhados à estratégia. |
| 2. Modelo operacional | Forma de atuação centralizada, federada ou consultiva | RACI, intake, fóruns, handoff, papéis de produto/plataforma/dados/risco. |
| 3. Governança e risco | Gestão de risco, IA responsável, compliance, segurança e privacidade | Classificação de risco, gates, red teaming, auditoria, incident response. |
| 4. Plataforma e arquitetura | Capacidade técnica comum para construir e operar IA | Landing zone, ambientes, catálogo de modelos, guardrails, observabilidade. |
| 5. Dados e conhecimento | Governança de dados, qualidade, acesso, lineage e bases para RAG | Data owners, catálogo, qualidade, sensibilidade, curadoria e ciclo de vida. |
| 6. LLMOps/MLOps e evals | Ciclo de vida, versionamento, testes e avaliação contínua | Evals, golden datasets, regressão, monitoramento, rollback e drift. |
| 7. Portfólio e valor | Priorização, business case, métricas e realização de benefícios | Funil de casos, KPIs de valor, revisão de benefícios, kill criteria. |
| 8. Capacitação e comunidade | AI literacy, trilhas técnicas, champions e comunidade de prática | Treinamento, certificação, comunidades, templates e suporte consultivo. |
| 9. FinOps e sustentabilidade | Custo, consumo, eficiência e impacto ambiental | Dashboards, budgets, otimização de modelos, custo por interação. |
| 10. Operação e melhoria contínua | Sustentação, incidentes, SLOs, ownership e evolução | Runbooks, SLOs, owners, suporte, revisão periódica e melhoria contínua. |

## Perfil por nível

| Dimensão | Nível 1 — Reativo | Nível 2 — Executor | Nível 3 — Habilitador | Nível 4 — Transformador |
|---|---|---|---|---|
| Estratégia e mandato | Iniciativas dispersas, sem sponsor claro | CoE formalizado e patrocinado | Estratégia conectada a portfólio e funding | IA integrada à estratégia corporativa |
| Modelo operacional | Papéis ambíguos | CoE central executa | Modelo federado com handoff | CoE consultivo e comunidades autônomas |
| Governança e risco | Avaliação informal | Controles mínimos por projeto | Gates, padrões e trilhas auditáveis | Gestão de risco contínua e preditiva |
| Plataforma e arquitetura | Ferramentas ad hoc | Ambientes controlados pelo CoE | Plataforma self-service governada | Plataforma otimizada e evolutiva |
| Dados e conhecimento | Dados usados caso a caso | Curadoria inicial para PoCs | Catálogo, qualidade e acesso governado | Dados como produto e conhecimento reutilizável |
| LLMOps/MLOps e evals | Testes manuais | Evals iniciais por projeto | Evals automatizados e regressão | Observabilidade contínua e aprendizado sistemático |
| Portfólio e valor | Ideias oportunistas | PoCs com valor demonstrável | Portfólio priorizado por valor/risco | Valor medido e otimizado continuamente |
| Capacitação e comunidade | Conhecimento em poucos especialistas | Treinamentos básicos | Champions e comunidade ativa | Cultura de IA responsável disseminada |
| FinOps e sustentabilidade | Custo invisível | Budgets iniciais | Dashboards e otimização recorrente | Custo, valor e sustentabilidade integrados |
| Operação e melhoria contínua | Sem owner claro em produção | Suporte dependente do CoE | Owners, runbooks e SLOs | Melhoria contínua e revisão executiva |

## Resultado do assessment

O assessment deve produzir:

- nível por dimensão;
- nível geral do CoE;
- lacunas críticas;
- evidências usadas;
- riscos de maturidade;
- recomendações de evolução;
- roadmap 30/60/90 dias.

