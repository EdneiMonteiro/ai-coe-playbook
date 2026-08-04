# Matriz fonte × seção × recomendação

Esta matriz cruza cada uma das **25 fontes** do artigo principal com as seções do playbook onde ela é usada e com a **recomendação prática** que dela deriva. Serve para auditoria de cobertura, para reduzir dependência editorial de uma única fonte e para validar que toda recomendação tem ao menos uma fonte sustentadora.

> **Fonte canônica:** [`bibliografia.bib`](bibliografia.bib) / [`bibliografia.json`](bibliografia.json) / [`../artigos/coe-ia-playbook.md`](../artigos/coe-ia-playbook.md): seção "Referências".

## Convenção

- **Fonte** = referência canônica (chave BibTeX).
- **Seção** = seção numerada do artigo principal ou artefato do playbook.
- **Recomendação derivada** = enunciado prático que a fonte sustenta.
- **Tipo** = `principal` (sustenta diretamente a recomendação) ou `cruzada` (corrobora uma recomendação sustentada por outra fonte).

## Matriz consolidada

### Fornecedores de tecnologia

| Fonte | Seções usadas | Recomendação derivada | Tipo |
|---|---|---|---|
| `ibm2026-coe` | §2, §3, §5.3 (Capacitação) | CoE como capacidade organizacional permanente; capacitação contínua via comunidade de prática. | principal |
| `microsoft2025-coe` | §4 (Modelos de Atuação); §4.4 evolução executor → consultivo; §10 (Maturidade) | Trajetória evolutiva do CoE; transição centralizado → consultivo; padrões antes de produtos. | principal |
| `microsoft2025-landingzone` | §6 (Arquitetura) | Landing zone como fundação técnica governada (segregação, RBAC, IaC). | principal |
| `microsoft2026-foundry` | §6.x (Microsoft Foundry); nomenclatura | Substituição de "Azure AI Studio/Foundry" por "Microsoft Foundry" como nome corrente. | principal |
| `microsoft2025-sustainableai` | §5.4 (FinOps), §6 sustentabilidade | Sustentabilidade como critério arquitetural; eficiência por modelo, região e inferência. | principal |
| `googlecloud2025-adoption` | §10 (Maturidade); níveis Tactical → Strategic → Transformational | Modelo de maturidade em níveis progressivos. | principal |
| `googlecloud2025-opex` | §6 (Arquitetura); §7 (Ciclo de Vida) | Excelência operacional como pilar de MLOps/LLMOps. | cruzada |
| `googlecloud2025-sustainability` | §5.4 (FinOps); §6 sustentabilidade | Sustentabilidade como pilar Well-Architected. | cruzada |
| `aws2025-mllens` | §6 (Arquitetura); §7 (Ciclo de Vida) | ML Lens como referência de operação ML/IA em cloud. | principal |
| `aws2025-genai` | §8 (GenAI/Agentic); §13 (Roadmap) | Centro de inovação como modelo de aceleração de PoCs. | cruzada |
| `ibm2025-nationwide` | §4.6 (Vinheta pública); Quadro 2 | Vinheta pública de CoE em organização financeira regulada (AI Centre of Expertise + IBM Consulting + Azure OpenAI). | principal |

### Consultorias e analistas

| Fonte | Seções usadas | Recomendação derivada | Tipo |
|---|---|---|---|
| `kpmg2024-coe` | §5.1 (Padrões), §11 (Métricas) | Priorização de portfólio + métricas executivas vinculadas a valor. | principal |
| `deloitte2025-coe` | §2 (CoE evoluído), §5.1, §11 | CoE como centro de excelência, não de experimentação permanente; repositório central de assets reutilizáveis. | principal |
| `oracle2026-coe` | §12 (Checklist Prático para Líderes); §13 (Roadmap) | Checklist operacional para construir CoE; orientação CIO/IT leadership. | principal |

### Protocolos, regulamentação, normas e frameworks de governança

| Fonte | Seções usadas | Recomendação derivada | Tipo |
|---|---|---|---|
| `mcp2025-spec` | §8 (GenAI/Agentic); §8.3 MCP | Catálogo de servidores aprovados, princípio de menor privilégio, critérios de bloqueio para agentes. | principal |
| `iso2023-42001` | §5.2 (Governança); §5.2.2 ISO 42001 | Sistema de gestão de IA (AIMS) como base contínua de governança. | principal |
| `nist2023-airmf` | §5.2 (Govern/Map/Measure/Manage); Tabela 3 | NIST AI RMF como framework operacional aplicado ao CoE. | principal |
| `nist2024-genaiprofile` | §5.2.6 (Red teaming); §5.2.7 (Evals); §8 (GenAI) | Riscos específicos de GenAI: confabulação, vazamento, abuso de ferramentas, prompt injection. | principal |
| `eu2024-aiact` | §5.2.4 (Classificação); §8.2 (Foundry); §8.3 (MCP); Tabela 4 | Classificação de risco; aplicabilidade GPAI Arts. 51-55; FRIA Art. 27; reporte Art. 73. | principal |
| `oecd2024-aiprinciples` | §5.2.3 (Princípios) | Cinco dimensões de IA confiável (crescimento inclusivo, direitos humanos, transparência, robustez, accountability). | principal |
| `google2025-responsibleai` | §5.2 (Governança); §8 (GenAI) | Práticas de IA responsável vendor-neutra. | cruzada |

### Artigos acadêmicos e científicos

| Fonte | Seções usadas | Recomendação derivada | Tipo |
|---|---|---|---|
| `curry2021-bdai-coe` | §3 (Equipe e Papéis-Chave); §5 (Pilares) | Framework de melhores práticas para CoEs em Big Data e IA. | principal |
| `rudko2021-orgstructure` | §4 (Modelos de Atuação); §4.4 evolução | Resposta organizacional ao "AI contingency"; centralização inicial → descentralização gradual. | principal |
| `kolbjornsrud2024-intelligent` | §8 (Era GenAI); §10 (Maturidade) | Seis princípios para colaboração humano-IA; design de organização inteligente. | principal |
| `ribeiro2025-aigovernance` | §5.2 (Governança); §13 (Roadmap) | Revisão de princípios de governança de IA; convergência entre frameworks. Preprint, não revisado por pares. | principal |

## Cobertura por seção do artigo

| Seção | Fontes sustentadoras (principais) | Risco de dependência única |
|---|---|---|
| §2: O que é um CoE | `ibm2026-coe`, `deloitte2025-coe` | Baixo |
| §3: Equipe e Papéis-Chave | `curry2021-bdai-coe`, `ibm2026-coe` | Baixo |
| §4: Modelos de Atuação | `microsoft2025-coe`, `rudko2021-orgstructure` | Baixo |
| §4.6: Vinheta pública | `ibm2025-nationwide` | **Alto** (única vinheta) |
| §5.1: Padrões | `deloitte2025-coe`, `kpmg2024-coe` | Baixo |
| §5.2: Governança e IA Responsável | `nist2023-airmf`, `iso2023-42001`, `eu2024-aiact`, `oecd2024-aiprinciples`, `google2025-responsibleai`, `ribeiro2025-aigovernance` | Muito baixo |
| §5.2.6: AI red teaming | `nist2024-genaiprofile` | **Alto** (única fonte normativa principal) |
| §5.2.7: Evals contínuos | `nist2024-genaiprofile`, `nist2023-airmf` | Baixo |
| §5.3: Capacitação e Comunidade | `ibm2026-coe` | **Alto** |
| §5.4: FinOps para IA | `microsoft2025-sustainableai`, `googlecloud2025-sustainability`, `kpmg2024-coe` | Baixo |
| §6: Arquitetura e Plataforma Cloud | `microsoft2025-landingzone`, `microsoft2026-foundry`, `aws2025-mllens`, `googlecloud2025-opex` | Muito baixo |
| §7: Ciclo de Vida | `aws2025-mllens`, `googlecloud2025-opex` | Médio |
| §8: Era GenAI / Agentic | `mcp2025-spec`, `nist2024-genaiprofile`, `eu2024-aiact`, `kolbjornsrud2024-intelligent`, `aws2025-genai` | Baixo |
| §10: Modelo de Maturidade | `googlecloud2025-adoption`, `microsoft2025-coe`, `kolbjornsrud2024-intelligent` | Baixo |
| §11: Métricas e KPIs | `kpmg2024-coe`, `deloitte2025-coe`, `microsoft2025-coe` | Baixo |
| §12: Checklist Prático | `oracle2026-coe` | **Alto** (única fonte direta de checklist) |
| §13: Roadmap de Implementação | `oracle2026-coe`, `aws2025-genai`, `ribeiro2025-aigovernance` | Médio |

## Risco de dependência editorial

Seções com **dependência alta** (uma única fonte principal) devem ser cruzadas com fontes secundárias em futuras revisões:

- **§4.6 (Vinheta Nationwide):** considerar pelo menos uma vinheta adicional ou nota de limitação (já presente: case study de fornecedor, não estudo independente).
- **§5.2.6 (Red teaming):** complementar com OWASP LLM Top 10 v2.0 e MITRE ATLAS quando aplicável.
- **§5.3 (Capacitação):** acrescentar fonte sobre AI literacy (BCG, MIT) quando disponível.
- **§12 (Checklist):** o Oracle/CIO é declaradamente um "checklist"; o risco editorial é mínimo aqui, mas vale cruzar com KPMG/Deloitte em revisão futura.

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 1.0 | 2026-05-23 | Criação. Matriz inicial de 25 fontes × seções × recomendações. Análise de risco de dependência editorial. |
