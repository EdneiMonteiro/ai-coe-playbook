# Leituras complementares

Fontes consultadas durante as revisões do playbook (artigo principal + assessment + artefatos) que **não entraram na bibliografia do artigo**, mas alimentaram recomendações específicas, validaram nomenclatura ou foram usadas como base de comparação. Ficam registradas aqui para:

- evitar que a próxima revisão aponte essas fontes como "lacuna" desconhecida;
- preservar a trilha de fontes consultadas para futuras versões;
- separar uso operacional (técnico) de uso narrativo (no artigo).

> **Política.** Esta lista **não é bibliografia citável** do artigo. Para citações formais, use [`bibliografia.bib`](bibliografia.bib) ou [`bibliografia.json`](bibliografia.json).

## Segurança e red teaming

| Fonte | Versão / data | Uso operacional |
|---|---|---|
| OWASP Top 10 for LLM Applications | v2.0 (2024-11-18) | Taxonomia mínima de cobertura de red team (LLM01 Prompt Injection, LLM02 Sensitive Information Disclosure, LLM03 Supply Chain, LLM04 Data and Model Poisoning, LLM06 Excessive Agency, LLM10 Unbounded Consumption). Citada em `artefatos/template-avaliacao-risco-ia.md` (campo Red teaming) e `assessment/questionario-assessment.md` (L2). |
| MITRE ATLAS | versão corrente | Mapa de táticas adversariais contra ML/IA. Referência alternativa para ampliar cobertura quando o OWASP LLM Top 10 não cobrir o caso (ex.: ataques específicos a ML clássico). |

## FinOps de IA

| Fonte | Versão / data | Uso operacional |
|---|---|---|
| FinOps Framework (FinOps Foundation) | release corrente | Disciplina FinOps aplicada a workloads de IA: showback/chargeback, budgets, alertas, otimização, sustentabilidade. Citada em `artigos/coe-ia-playbook.md` §5.4 sem citação direta na bibliografia. |
| State of FinOps for AI (FinOps Foundation) | edição 2025 | Estado da arte de FinOps aplicado a IA generativa e agentes. Conteúdo absorvido em recomendações de FinOps no artigo e no assessment. |
| FOCUS — FinOps Open Cost & Usage Specification | v1.3 | Especificação aberta para taxonomia de custo. Linha de base para alinhar billing de provedores. |

## Governança executiva e board

| Fonte | Versão / data | Uso operacional |
|---|---|---|
| NACD — AI Oversight Guidance (4-Pillar) | 2024 | Pilares de supervisão executiva: estratégia, talento, risco e ética. Usado para informar §10 (Decisões executivas) do `assessment/relatorio-template.md`. |
| WEF — AI Governance Alliance / Toolkits | 2024–2025 | Referência cruzada para princípios de governança em conselhos de administração. |

## Privacidade e transferência internacional de dados

| Fonte | Versão / data | Uso operacional |
|---|---|---|
| ANPD — Resolução CD/ANPD nº 19/2024 (CCPs) | 2024-08-23 (prazo de adequação expirado em 2025-08-23) | Cláusulas-padrão contratuais para transferência internacional de dados pessoais sob LGPD. Citada em `artefatos/template-avaliacao-risco-ia.md` (campo "Dados — transferência internacional") e `referencias/crosswalk-normativo.md`. |
| EDPB — Opinion 28/2024 | 2024 | Opinião sobre uso de dados pessoais em modelos de IA. URL primária instável; conteúdo sustentado por fontes secundárias. |
| EDPB — Recommendations 01/2020 (Schrems II) | 2020 | Recomendações sobre Transfer Impact Assessment (TIA) quando provider está sujeito a leis extraterritoriais (CLOUD Act, FISA 702). |
| LGPD (Lei 13.709/2018 + Lei 13.853/2019) | redação vigente | Base normativa primária no Brasil. Citação de Art. 20 atualizada conforme Lei 13.853/2019. |

## Documentação de sistemas de IA

| Fonte | Versão / data | Uso operacional |
|---|---|---|
| Model Cards for Model Reporting (Mitchell et al.) | 2019 | Padrão de documentação para modelos. Citado implicitamente em `assessment/relatorio-template.md` §13 (Anexo técnico). |
| Datasheets for Datasets (Gebru et al.) | 2018/2021 | Padrão de documentação para datasets. Citado implicitamente em `assessment/relatorio-template.md` §13. |
| System Cards (OpenAI/Meta/Anthropic) | versões correntes | Padrão de documentação para sistemas baseados em GPAI/SaaS, complementar a model cards. |

## Auditoria, asseguração e metodologia

| Fonte | Versão / data | Uso operacional |
|---|---|---|
| ISO 19011 | 2018 (revisão Stage 60 em curso) | Diretrizes para auditoria de sistemas de gestão. Usado como referência metodológica para o assessment em modo auditoria/investimento. |
| ISO/IEC 33020 | 2019 | Avaliação de capacidade de processos. Referência para a escala 0–4 do assessment. |
| ISAE 3000 | versão corrente | Norma de asseguração internacional. Referência para o nível de rigor exigido se o assessment for usado como fundamento de relatório de asseguração. |
| CMMI 3.0 | release corrente | Inspiração metodológica para o modelo de maturidade em 4 níveis. |

## Regulação setorial brasileira (carry-over para v1.x)

Estas normas foram consideradas para o Anexo BR do crosswalk (`crosswalk-normativo.md`):

| Setor | Norma | Status no playbook |
|---|---|---|
| Financeiro (bancos e cooperativas) | CMN Res. 4.893/2021 + CMN Res. 4.557/2017 | Citada no Anexo BR. |
| Financeiro (IPs e demais autorizadas pelo BCB) | BCB Res. 85/2021 | Citada no Anexo BR (substitui BACEN Res. 4.658/2018, revogada em 2023). |
| Mercado de capitais | CVM Res. 35/2021 | Citada no Anexo BR. |
| Saúde suplementar | ANS RN 518/2022 | Citada no Anexo BR (substitui referência incorreta anterior a ANS RN 501/2022, que é Padrão TISS). |
| Infraestrutura crítica | ANEEL, ANATEL, agências setoriais | Citadas no Anexo BR (sem norma específica detalhada). |
| Saúde / dispositivos médicos | ANVISA | Citada no Anexo BR. |
| Carry-over v1.2 | BACEN Res. 538/2025; CMN Res. 5.274/2025 | Backlog. Notas de modernização recentes. |

## Sustentabilidade técnica

| Fonte | Versão / data | Uso operacional |
|---|---|---|
| GHG Protocol Scope 2/3 | versão corrente | Metodologia para inventário de emissões. Backlog v1.2 — sustentabilidade técnica de inferência LLM. |
| Green Software Foundation — Patterns | release corrente | Padrões de software sustentável. Backlog v1.2. |

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 1.0 | 2026-05-23 | Criação. Consolida fontes consultadas durante 6 revisões de assessment + 2 revisões de artefatos. Separação por área temática. |
