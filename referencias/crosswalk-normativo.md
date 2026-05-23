# Crosswalk normativo — NIST AI RMF × ISO/IEC 42001 × EU AI Act × LGPD/GDPR

Este crosswalk é um mapeamento heurístico entre os principais frameworks e regulações de IA, organizado por **tema de governança** (não por enumeração 1-para-1). Use-o para preencher de forma consistente a matriz de rastreabilidade do assessment, para localizar lacunas de cobertura entre frameworks e para orientar a construção de evidências auditáveis.

> **Limitações.** A correspondência é aproximada e exige verificação para cada implementação. Mudanças regulatórias (faseamento do EU AI Act, atualizações ISO, novas opiniões EDPB/ANPD) podem alterar o mapeamento. Este crosswalk **não substitui parecer jurídico, auditoria credenciada nem revisão setorial específica**.

## Crosswalk principal (4 frameworks)

| Tema de governança | NIST AI RMF (função/subcategoria) | ISO/IEC 42001:2023 — Anexo A | EU AI Act — artigos principais | LGPD / GDPR — base correspondente | Nível de cobertura |
|---|---|---|---|---|---|
| Política, governança e mandato | Govern 1.1, 1.2, 1.4; Govern 2.1, 2.2 | A.2 Políticas relacionadas à IA; A.3 Funções e responsabilidades; A.4 Recursos para sistemas de IA | Arts. 17, 26 (deveres do deployer) | LGPD Arts. 50, 41 (DPO/agentes); GDPR Arts. 24, 37 | Plena |
| Inventário de sistemas e classificação de risco | Map 1.1, 1.2, 1.3; Map 5.1, 5.2 | A.5 Avaliação de impacto de sistemas de IA; A.6.1 Ciclo de vida de sistemas de IA | Arts. 6, 9 (alto risco); Anexo III | LGPD Arts. 38, 11; GDPR Art. 35 (DPIA) | Plena |
| Gestão de risco e controles | Manage 1, 2, 3, 4 | A.5 Avaliação de impacto e tratamento de risco; A.6.2 Controles ao longo do ciclo de vida | Arts. 9, 15, 26, 27 | LGPD Art. 5(XVII), 50; GDPR Art. 32 | Plena |
| Dados e qualidade | Map 2.3; Measure 2.10; Manage 3 | A.7 Dados para sistemas de IA (data for AI systems) | Arts. 10 (data governance), 15 | LGPD Arts. 6 (princípios), 11 (sensíveis), 18 (direitos); GDPR Arts. 5, 9, 15–22 | Plena |
| Transparência e documentação | Govern 1.4; Map 4.1, 4.2; Measure 3 | A.6.2.3 Documentação técnica de sistemas de IA; A.8 Informação para partes interessadas | Arts. 11, 13, 50, 53 (GPAI) | LGPD Arts. 9, 20 (revisão de decisão); GDPR Arts. 13, 14, 22 | Plena |
| Avaliação, evals e testes | Measure 1, 2, 3, 4 | A.6.2.4 Verificação e validação | Arts. 9, 15 (acurácia, robustez) | LGPD Art. 38; GDPR Art. 35 | Plena |
| AI red teaming e segurança | Measure 2.6, 2.7; Manage 4.1 | A.6.2.6 Operação e monitoramento (operação adversarial e robustez) | Arts. 9, 15 (resiliência); Art. 55 (GPAI risco sistêmico) | LGPD Art. 46; GDPR Art. 32 | Parcial |
| Monitoramento e incidente | Manage 4.2, 4.3 | A.6.2.6 Operação e monitoramento (verificar texto oficial para A.6.2.7) | Arts. 16, 26, 73 (reporte de incidente sério) | LGPD Art. 48; GDPR Art. 33 | Parcial |
| Direitos do titular e supervisão humana | Govern 5.2; Map 3.5; Measure 2.8 | A.5 Avaliação de impacto; A.6.2.4 V&V; A.8 Informação para partes interessadas | Arts. 14 (supervisão humana), 26, 27, 86 | LGPD Arts. 18, 20; GDPR Arts. 15–22 | Plena |
| Transferência internacional e fornecedor | Govern 6; Map 4.1 | A.10 Fornecedores e relações com terceiros | Arts. 25 (provedor), 26 (deployer), 53 (GPAI) | LGPD Arts. 33–36; GDPR Cap. V (Arts. 44–50) | Plena |
| Modelo de uso geral (GPAI) | Map 1.1; Govern 1.4 | n/a direto; A.6.2 controles aplicáveis | Arts. 51–55 (GPAI), Anexo XI/XII | n/a direto; aplicam-se Art. 5 GDPR / Art. 6 LGPD para uso pessoal | Tangencial |

> **Nota de verificação ISO/IEC 42001:2023.** As referências ao Anexo A acima foram revisadas contra fontes públicas Tier 2 (bastion.tech, kimova.ai, watchdog security) durante a auditoria da rev-01 do comitê de diagramas e referências. Cinco entradas foram corrigidas em relação à versão anterior do crosswalk (notadamente A.6.2.4 V&V, A.6.2.6 Operação e monitoramento, A.7 Dados para IA, A.8 Informação para partes interessadas). Há divergência entre fontes secundárias sobre o objeto exato do controle A.6.2.7 — recomenda-se cruzar contra o texto oficial da norma ISO/IEC 42001:2023 antes de uso em auditoria credenciada.

**Coluna "Nível de cobertura":** indica quão completamente o tema é coberto pela coluna ISO/EU AI Act mais próxima. `Plena` = controle/artigo trata explicitamente o tema; `Parcial` = trata o tema mas exige composição com outro controle ou parecer setorial; `Tangencial` = aplicável por extensão, não como obrigação direta; `Não cobre` = ausência declarada (não usado nesta versão).

## Versionamento normativo

Referências evolutivas usadas como linha de base:

| Framework | Versão de referência | Data | Observação |
|---|---|---|---|
| NIST AI RMF | 1.0 + AI 600-1 (GenAI Profile) | 2023 / 2024 | RMF base + Generative AI Profile como complemento. |
| ISO/IEC 42001 | 2023 | 2023-12-18 | AIMS — Artificial Intelligence Management System. |
| EU AI Act | Regulamento 2024/1689 | em vigor desde 02/02/2025 (Cap. I/II); GPAI desde 02/08/2025; Anexo III desde 02/08/2026 | Faseamento por capítulo. |
| LGPD | Lei 13.709/2018 (com Lei 13.853/2019) | vigente | Art. 20 redação atualizada por Lei 13.853/2019. |
| GDPR | Reg. (UE) 2016/679 | vigente desde 25/05/2018 | — |
| OWASP LLM Top 10 | v2.0 | 2024-11-18 | Linha de base de segurança aplicada a LLMs. |

Este crosswalk deve ser reavaliado a cada release major dessas referências.

## Especificidades GPAI (Arts. 51–55)

| Tema GPAI | Art. EU AI Act | Conteúdo |
|---|---|---|
| Classificação como GPAI | Art. 51 | Critérios para enquadrar modelo de uso geral. |
| Obrigações do provider | Art. 53 | Documentação técnica, sumário de dados de treino, política de copyright, transparência. |
| GPAI com risco sistêmico | Art. 55 | Avaliação adversarial, red teaming, reporte de incidentes, cibersegurança. |
| Obrigações de deployer | Art. 26 + Art. 50 (transparência) | Quem usa GPAI em produção tem deveres mesmo sem ser o provider. |

## Anexo BR — nota setorial para holdings reguladas no Brasil

Mapeamento heurístico entre o crosswalk principal e dispositivos setoriais brasileiros. Aplicação específica exige parecer setorial.

| Setor | Regulador / norma principal | Mapeamento típico no assessment |
|---|---|---|
| Financeiro (bancos e cooperativas) | CMN Res. 4.893/2021 (segurança cibernética — bancos e cooperativas); CMN Res. 4.557/2017 (risco operacional) | Reforçar Governança e risco, Operação e melhoria contínua, Plataforma e arquitetura; gates de incidente integrados ao reporte BACEN. |
| Financeiro (instituições de pagamento e demais autorizadas pelo BCB) | BCB Res. 85/2021 (segurança cibernética — substitui a antiga BACEN Res. 4.658/2018, revogada em 01/07/2023, no escopo das IPs e demais entidades reguladas pelo BCB) | Reforçar Governança e risco, Operação e melhoria contínua, Plataforma e arquitetura; gates de incidente integrados ao reporte BCB. |
| Mercado de capitais | CVM Res. 35/2021 (gestão de riscos e controles internos) | Reforçar Governança e risco e Portfólio e valor; documentação técnica alinhada ao reporte CVM. |
| Saúde suplementar | ANS RN 518/2022 (controles internos, gestão de riscos e governança em operadoras de saúde suplementar — revogou RN 443/2019) | Reforçar Dados e conhecimento (dados sensíveis de saúde), Governança e risco e Operação e melhoria contínua; FRIA/DPIA obrigatória em casos de alto risco. |
| Setor elétrico, telecom, água | ANEEL, ANATEL, agências setoriais | Reforçar Operação e melhoria contínua (resiliência, continuidade) e Plataforma e arquitetura (infraestrutura crítica). |
| Saúde / dispositivos médicos | ANVISA | Reforçar Dados e conhecimento, Governança e risco e LLMOps/MLOps (rastreabilidade clínica e pós-mercado). |

## Instrumentos de transferência internacional de dados

Resumo dos mecanismos formais aplicáveis quando dados pessoais transitam entre jurisdições:

| Origem | Mecanismo | Base normativa | Observação |
|---|---|---|---|
| LGPD (BR) | Decisão de adequação da ANPD | LGPD Art. 33, I | Lista mantida pela ANPD. |
| LGPD (BR) | Cláusulas-Padrão Contratuais (CCPs) | LGPD Art. 33, II; ANPD Res. CD/ANPD nº 19/2024 | Prazo de adequação expirou em 23/08/2025. |
| LGPD (BR) | Normas Corporativas Globais (NCGs) | LGPD Art. 33, III | Para transferências intragrupo. |
| GDPR (UE) | Decisão de adequação | GDPR Art. 45 | Lista mantida pela Comissão Europeia. |
| GDPR (UE) | Standard Contractual Clauses (SCCs) | GDPR Art. 46 | Versão 2021 vigente. |
| GDPR (UE) | Binding Corporate Rules (BCRs) | GDPR Art. 47 | Para transferências intragrupo. |
| Provider sob lei extraterritorial | Transfer Impact Assessment (TIA) | Schrems II + EDPB Recommendations 01/2020 | Necessário quando provider está sujeito a CLOUD Act, FISA 702 ou similares. |

## Como usar este crosswalk

1. **No assessment** (`assessment/relatorio-template.md` §8) — usar como referência para preencher as colunas NIST AI RMF, ISO/IEC 42001 Anexo A, EU AI Act, GPAI Arts. 51–55 e LGPD/GDPR.
2. **No artigo** (`artigos/coe-ia-playbook.md`) — usar como apoio para justificar recomendações regulatórias citadas no texto.
3. **Em pareceres internos** — usar como ponto de partida para localizar a base normativa que sustenta uma decisão de gate.
4. **Em revisão periódica** — quando uma das referências da seção "Versionamento normativo" tiver release major, este crosswalk deve ser reavaliado.

## Histórico de revisão

| Versão | Data | Mudança |
|---|---|---|
| 1.0 | 2026-05-23 | Extraído de `assessment/relatorio-template.md` (Anexo C + Anexo C-BR) para vida própria em `referencias/`. Inclui correções regulatórias aplicadas até a rev-06 do assessment (BACEN 4.658 revogada → CMN 4.893/BCB 85; ANS RN 501 → ANS RN 518). |
