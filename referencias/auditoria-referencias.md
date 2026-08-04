# Auditoria de referências

Esta página registra a memória operacional das referências do AI CoE Playbook: o que foi incluído, o que foi removido, o que foi corrigido e por quê. O objetivo é dar **rastreabilidade longitudinal** ao corpo de fontes, especialmente em casos de mudança regulatória ou perda de acesso.

## Princípios

- **Referência publicável** = URL acessível publicamente, conteúdo estável, fonte primária ou secundária verificável.
- **Remoção registrada** = quando uma fonte é removida do artigo principal, o motivo fica documentado aqui.
- **Correção registrada** = quando uma fonte foi citada incorretamente (revogada, mislabeled, número errado), a correção e a origem do erro ficam documentadas.
- **Verificação de vigência** = validar existência **e** vigência de uma norma; o anti-pattern *validator search* (confirmar só existência) foi a causa de duas regressões na história do playbook.

### Política bibliográfica para normas citadas no crosswalk

Nem toda menção normativa em `referencias/crosswalk-normativo.md` exige entrada própria em `bibliografia.bib`/`bibliografia.json`.

**Entrada bibliográfica obrigatória** quando a fonte for:
- norma, framework ou guia central do crosswalk principal (ex.: NIST AI RMF, ISO/IEC 42001, EU AI Act, LGPD, GDPR, ANPD Res. 15/2024 e 19/2024, OWASP LLM Top 10);
- instrumento citado por número/identificador oficial como fundamento direto de obrigação operacional no assessment;
- fonte usada no artigo principal como referência narrativa ou justificativa central.

**Registro em auditoria ou leituras complementares é suficiente** quando a fonte for:
- menção setorial em anexo/overview (ex.: CMN, BCB, CVM, ANS) sem análise artigo-a-artigo;
- norma revogada citada apenas para explicar substituição histórica;
- lei estrangeira ou jurisprudência mencionada como gatilho contextual de análise jurídica, salvo quando virar seção operacional própria;
- referência de backlog ou universo consultado não citada no artigo principal.

**Escalonamento:** se uma menção setorial ou jurisprudencial passar a sustentar gate, controle, checklist ou decisão operacional específica, ela deve ser promovida para entrada bibliográfica Tier 1 na próxima revisão.

## Referências removidas e por quê

| Fonte | Tipo | Motivo da remoção | Quando | Substituta |
|---|---|---|---|---|
| **Gartner** (várias publicações) | Analista | Conteúdo restrito a assinantes; não permite verificação pública | Audit inicial (pré-rev-01 do artigo) | Recomendações cruzadas de IBM, Microsoft CAF, KPMG, Deloitte, Oracle/CIO |
| **SalesChoice** | Vendor | Página/PDF apresentava 403 anti-bot em acessos automatizados; instabilidade de acesso comprometia auditoria | Audit inicial | Recomendações cruzadas de fornecedores estáveis |
| **UST** | Vendor | Inicialmente acessível, depois 403/timeout intermitente | Audit inicial | Recomendações cruzadas de fornecedores estáveis |
| **BACEN Res. 4.658/2018** | Norma setorial BR | **Revogada em 01/07/2023**, mas citada como vigente no Anexo C-BR | Patch v5 (assessment rev-06) | **CMN Res. 4.893/2021** (bancos e cooperativas) + **BCB Res. 85/2021** (IPs e demais autorizadas pelo BCB) |
| **ANS RN 501/2022** | Norma setorial BR | Mislabeled como "controles internos"; objeto real é Padrão TISS (interoperabilidade) | Patch v5 (assessment rev-06) | **ANS RN 518/2022** (controles internos, gestão de riscos e governança) |

## Correções de citação registradas

| Citação | Erro | Correção | Origem do erro |
|---|---|---|---|
| LGPD Art. 20 | Redação histórica "revisão por pessoa natural" | Redação vigente: "direito de solicitar revisão de decisões automatizadas + informação sobre critérios" (Lei 13.853/2019) | Texto histórico anterior à atualização |
| EU AI Act Art. 27 (FRIA) | Aplicação a todo deployer Anexo III | Restrito a (a) entes públicos, (b) entes privados em serviço público, (c) deployers de Anexo III 5(b)/5(c) | Sobreescopo na primeira leitura |
| OWASP LLM Top 10 | Versão não declarada | Versão **v2.0 (2024-11-18)** declarada explicitamente | Citação implícita sem versionamento |
| FOCUS | Versão v1.2 citada | Versão v1.3 atual | Defasagem por release |
| ISO 19011 | Versão 2018 citada para etapas em revisão 2026 | ISO 19011:2018 cl. 4 mantida onde aplicável; ISO 19011 com revisão em Stage 60 ainda não publicada | Antecipação prematura de versão |
| EDPB Opinion 28/2024 | URL primária retornou 404 | Conteúdo sustentado por fontes secundárias verificáveis | Mudança de URL após publicação |
| `ieee2025-aigovernance` autor "IEEE/ACM" | Alucinação de autor institucional para preprint arXiv | Autor real: **Ribeiro, Danilo Monteiro et al.**; chave renomeada para `ribeiro2025-aigovernance`; nota "preprint, not peer-reviewed" adicionada | Citação institucional inferida sem verificação da página arXiv |
| `eu2024-aiact` URL | URL de notícia do European Parliament | Substituído por **EUR-Lex CELEX 32024R1689** (fonte oficial); autor atualizado para "European Parliament and Council of the European Union" | Fonte secundária no lugar da primária |
| Crosswalk ISO/IEC 42001 Anexo A (5 entradas) | Cláusulas incorretas (A.6.2.4, A.6.2.5, A.6.2.6, A.7, A.8) | Corrigidas contra fontes Tier 2 (bastion.tech, kimova.ai, watchdog security); coluna A.6.2.7 marcada como "verificar texto oficial" devido a divergência entre fontes secundárias | Não-verificação contra texto oficial ISO/IEC 42001:2023 |
| Crosswalk ISO/IEC 42001 A.6.2.7 (rev-02) | Nota de incerteza sem resolução | Padronizado como "Documentação técnica do sistema de IA" com base em ISMS.online (fonte Tier 2 dedicada à ISO 42001 e watchdog security); divergência com bastion.tech (Retirement) registrada como discrepância de Tier 2/Tier 3 | Resolução pendente desde rev-01; fechamento parcial sem texto oficial ISO |
| Crosswalk EU AI Act Art. 17 (rev-02) | "Arts. 17, 26 (deveres do deployer)"; o Art. 17 é obrigação exclusiva do PROVIDER, não do deployer | Corrigido para "Art. 17 (provider: QMS, alto risco); Art. 26 (deployer)" via verificação direta no texto EUR-Lex CELEX 32024R1689 | Confusão estrutural entre obrigações de provider (QMS Art. 17) e deployer (Arts. 26, 27) |
| Diag.07 prazo ANPD (rev-02) | "ANPD Res. 15/2024 (≤72h)": prazo corrido errado | Corrigido para "ANPD Res. 15/2024 (≤3 dias úteis, Art. 6º)" via verificação no texto oficial da resolução | Tradução incorreta de "três dias úteis" para "72h corridas" |
| Diag.07 NIST SP 800-61 (rev-02) | Referência a Rev. 2 §3.1 | Atualizado para Rev. 3 (publicada em abril/2025) | Defasagem por release de framework |
| `kolbjornsrud2024-intelligent` campos `pages` e `doi` (rev-02) | Ausentes em @article incompleto | Adicionados `pages = {44--64}` e `doi = {10.1177/00081256231211020}` (verificados via SAGE Journals) | Patch parcial em revisão anterior; completude de campos @article |
| `nist2023-airmf` campo `doi` (rev-02) | Ausente | Adicionado `doi = {10.6028/NIST.AI.100-1}` em ambos BibTeX e JSON | Confiança apenas na URL; o DOI é redundante mas recomendado para persistência |
| `rudko2021-orgstructure` URL (rev-02) | Endpoint CrossRef API (`api.crossref.org/works/...`): retorna JSON de metadados, não artigo | Substituído por DOI canônico (`https://doi.org/10.3390/jtaer16060129`) | Identificação errada do endpoint resolvido na revisão inicial |
| `ribeiro2025-aigovernance` co-autores JSON e DOI arXiv (rev-02) | JSON com apenas 1 autor; ambos BibTeX e JSON sem DOI arXiv | Expandido para 7 co-autores (Ribeiro, Rocha, Pinto, Cartaxo, Amaral, Davila, Camargo, da Zup Innovation) em ambos formatos; adicionado `doi = {10.48550/arXiv.2505.23417}`; tipo CSL alterado de `article` para `article-journal` | Sincronização incompleta entre BibTeX e JSON; ausência de DOI persistente |
| `kolbjornsrud2024-intelligent` ano vs slug | Slug do PDF promocional indica 2023; chave indica 2024 | Nota adicionada explicando que CMR publicou versão revisada em 2024 e o manuscrito promocional circulou desde 2023; volume/issue documentados | Divergência entre versão draft e versão final |

## Política de verificação de URLs

Para o conjunto de **32 entradas bibliográficas** (25 referências numeradas do artigo principal `artigos/coe-ia-playbook.md` mais 7 instrumentos normativos citados em `crosswalk-normativo.md` e nos diagramas, adicionados ao longo do ciclo de revisão do comitê de diagramas e referências):

- **Frequência:** verificar todas as URLs antes de cada release major do playbook.
- **Escopo:** status HTTP, presença do título esperado, ausência de redirecionamento para página de erro/login.
- **Anti-padrão "validator search":** ao adicionar nova norma, exigir busca adversarial ("norma X foi revogada?" "qual é o objeto real?"), não apenas confirmação de existência.
- **Última verificação consolidada:** maio/2026, antes da publicação do artigo principal: 25/25 URLs OK, 0 restritas, 0 anti-bot.

## Carimbo de verificação por documento

Documentos que fazem afirmações normativas datadas (vigências, prazos, limites de multa, números de artigo) exibem, logo abaixo do título, um carimbo declarando o mês da última verificação. O objetivo é que o leitor saiba o que precisa revalidar, em vez de assumir que o texto está atualizado.

Documentos carimbados: `artefatos/template-avaliacao-risco-ia.md`, `artefatos/raci-coe-ia.md`, `assessment/questionario-assessment.md`, `assessment/criterios-pontuacao.md`, `assessment/board-pack-template.md`, `diagramas/06-regimes-dados.md`, `diagramas/07-fluxo-incidente.md`, `diagramas/08-matriz-risco-controles.md`, `referencias/crosswalk-normativo.md`.

### Checklist de release

Antes de cada release, executar e registrar nesta auditoria:

1. Revalidar as URLs das 32 entradas bibliográficas (política acima).
2. Revalidar as afirmações datadas dos documentos carimbados: vigências do EU AI Act, prazos ANPD, limites de multa LGPD/GDPR, normas setoriais (CMN, BCB, ANS) e status das normas ISO citadas.
3. Aplicar a busca adversarial a cada norma citada ("foi revogada?", "mudou de escopo?").
4. Atualizar o mês do carimbo nos documentos revalidados e registrar aqui o resultado.

## Universo consultado e não citado (leituras complementares)

Estas fontes apareceram nas revisões do comitê mas **não foram citadas no artigo**. Ficam registradas como universo consultado para evitar dúvida de cobertura em revisões futuras:

| Fonte | Área | Por que não citada |
|---|---|---|
| State of FinOps for AI (FinOps Foundation) | FinOps de IA | Conteúdo absorvido em recomendações sem citação direta. |
| OWASP LLM Top 10 v2.0 | Segurança de LLM | Citado no assessment (template e Red teaming), mas não na bibliografia narrativa do artigo. |
| NACD 2024 Oversight Guidance | Governança executiva | Usado no board pack e §10 do relatório auditável; não na bibliografia narrativa. |
| EDPB Opinion 28/2024 | Privacidade UE | Citado pontualmente no Anexo C; URL primária instável. |
| FOCUS v1.3 | FinOps Foundation | Referência operacional para taxonomia de custo. |
| NIST AI 600-1 (GenAI Profile) | NIST AI RMF complementar | Citado em referências; usado também como complemento ao RMF base. |
| ANPD Res. CD/ANPD nº 19/2024 (CCPs) | LGPD transferência internacional | Citado no template e crosswalk; não na bibliografia narrativa principal. |

## Histórico de auditoria

| Data | Evento | Mudança |
|---|---|---|
| 2026-05 (artigo rev-1) | Audit inicial | Removidas Gartner, SalesChoice, UST por instabilidade/acesso restrito. |
| 2026-05 (artigo rev-2/3) | Inclusão de Microsoft Foundry como nomenclatura corrente | Substituiu "Azure AI Studio / Azure AI Foundry" no texto e referências. |
| 2026-05 (assessment rev-05) | Patch v4 | Corrigiu BACEN Res. 4.658/2018 (revogada) → CMN 4.893/2021 + BCB 85/2021. Mislabel ANS RN 501 detectado. |
| 2026-05 (assessment rev-06) | Patch v5 | Corrigiu ANS RN 501/2022 (Padrão TISS) → ANS RN 518/2022 (controles internos). |
| 2026-05 (referencias rev-1) | Criação desta página | Extração do crosswalk para `referencias/crosswalk-normativo.md`. Auditoria consolidada. |
| 2026-05 (diagramas-referencias rev-01) | Patch v1 (P1..P10) | ISO 42001 Annex A corrigido (5 entradas); Regime 4 Feedback adicionado em Diag.06; chave `ieee2025-aigovernance` → `ribeiro2025-aigovernance`; Model registry em Diag.04; PREP em Diag.07; EU AI Act URL → EUR-Lex; volume/issue em kolbjornsrud; Ingestão em Diag.05; reporte regulatório expandido em Diag.07; coluna "Nível de cobertura" no crosswalk. |
| 2026-05 (diagramas-referencias rev-02) | Patch v2 (P-A..P-I) | RACI por fase em Diag.07; contenção C2 com owner + critério quantitativo; ANPD 72h → 3 dias úteis; Art. 17 EU AI Act provider/deployer corrigido; NIST SP 800-61 Rev. 2 → Rev. 3; A.6.2.7 padronizado como Technical Documentation; GPAI Code of Practice adicionado ao crosswalk; pages/DOI em kolbjornsrud; DOI em nist2023-airmf; URL canônica em rudko; 7 co-autores e DOI arXiv em ribeiro2025; alt-text WCAG em todos os 8 diagramas; `<i>` HTML → `*italic*` em Diag.06; classDef separado por nível de risco em Diag.08. |
| 2026-05 (diagramas-referencias rev-03) | Patch v3 (P-J..P-P) | Subgraph FB_CTL (controles Feedback/RLHF) em Diag.06 2º flowchart; R8 LGPD Art. 7 e AP5/C5 no mapa de risco regulatório de Diag.06; LGPD Art. 7 + GDPR Art. 6 adicionados à linha "Dados e qualidade" do crosswalk; Res. CD/ANPD Nº 15/2024 nomeada na linha "Monitoramento e incidente" + nova linha na tabela de versionamento normativo; A.6.2.8 (Event logs) ISO 42001 adicionado à coluna ISO da linha incidente; M4 Eval online (LLM-as-judge contínuo) adicionado ao subgraph MON de Diag.05; cross-refs EVAL→REG→CONSUMERS em Diag.04 e prompt registry/CP1 em Diag.05. |
| 2026-05 (diagramas-referencias rev-04) | Patch v4 (P-Q) | 3 novas entradas BibTeX/CSL-JSON para normas/instrumentos já citados nos artefatos mas ausentes da bibliografia: `nist2025-sp800-61r3` (NIST SP 800-61 Rev. 3, abr/2025); `euaioffice2025-gpai-cop` (GPAI Code of Practice, EU AI Office, 10/07/2025; aplicável desde 02/08/2025); `anpd2024-res15` (Resolução CD/ANPD Nº 15/2024, DOU 26/04/2024). Bibliografia agora tem 28 entradas (era 25). |
| 2026-05 (diagramas-referencias rev-05) | Patch v5 (P-R) | Substituídas 2 URLs com soft-404/404 (`euaioffice2025-gpai-cop`: `/policies/general-purpose-ai-code-practice` → `/policies/contents-code-gpai`; `anpd2024-res15`: `gov.br/anpd/.../resolucao-cd-anpd-no-15-...` → URL canônica DOU `in.gov.br/.../556243024`); adicionada nova entrada `owasp2024-llm-top10-v2` (OWASP Top 10 for LLM Applications 2025 v2.0, 18/11/2024) que era citada no crosswalk sem BibTeX. Bibliografia passa de 28 para 29 entradas. |
| 2026-05 (diagramas-referencias rev-06) | Patch v6 (P-S) | 3 novas entradas BibTeX/JSON para normas citadas no crosswalk sem entrada formal: `brasil2018-lgpd` (Lei 13.709/2018 LGPD); `eu2016-gdpr` (Regulamento UE 2016/679 GDPR); `anpd2024-res19` (Res. CD/ANPD Nº 19/2024 transferência internacional). Fecha gap pré-existente em auditoria + gap residual identificado por Ag.07 em rev-06 e validado pelo RD. Bibliografia passa de 29 para 32 entradas. |
| 2026-05 (diagramas-referencias rev-07) | Patch v7 (P-T) | Corrige URL `eu2016-gdpr` (EUR-Lex retorna HTTP 202 com WAF challenge → Publications Office canônica `publications.europa.eu/resource/celex/32016R0679` retorna HTTP 200 + RDF Tier 1, mesmo CELEX/ELI/OJ); adiciona seção "Política bibliográfica para normas citadas no crosswalk" separando entradas obrigatórias (frameworks centrais) de menções setoriais/contextuais (anexos, normas revogadas, leis estrangeiras-gatilho, jurisprudência), com critério explícito de escalonamento. Limita criterion creep do Ag.07 sem inflar a bibliografia além do escopo operacional. |

## Histórico de revisão deste documento

| Versão | Data | Mudança |
|---|---|---|
| 1.0 | 2026-05-23 | Criação. Consolida 4 audits anteriores (removidas + correções + verificação + universo consultado). |
| 1.1 | 2026-05-23 | Patch v1 (rev-01 diagramas/referências): adiciona 4 correções (ieee→ribeiro, EU AI Act URL, ISO 42001 5 entradas, kolbjornsrud ano). |
| 1.2 | 2026-05-23 | Patch v2 (rev-02 diagramas/referências): adiciona 8 correções (A.6.2.7 Technical Documentation, Art. 17 provider, ANPD 3 dias úteis, NIST SP 800-61 Rev. 3, kolbjornsrud pages/doi, nist airmf doi, rudko URL canônica, ribeiro JSON 7 co-autores + DOI arXiv). |
| 1.3 | 2026-05-23 | Patch v3 (rev-03 diagramas/referências): adiciona 7 correções estruturais e normativas (FB_CTL Diag.06; R8 LGPD Art. 7 mapa risco; LGPD Art. 7+GDPR Art. 6 crosswalk; Res. 15/2024 + versionamento; A.6.2.8 ISO 42001; M4 Eval online Diag.05; cross-refs EVAL→REG→CONSUMERS e prompt registry). |
| 1.4 | 2026-05-23 | Patch v4 (rev-04 diagramas/referências): adiciona 3 entradas BibTeX/JSON para normas já citadas (NIST SP 800-61 Rev. 3, GPAI Code of Practice, Res. CD/ANPD Nº 15/2024). Bibliografia passa de 25 para 28 entradas. |
| 1.5 | 2026-05-23 | Patch v5 (rev-05 diagramas/referências): substitui 2 URLs com soft-404/404 (GPAI CoP → /contents-code-gpai; ANPD Res. 15 → DOU canônica) e adiciona entrada `owasp2024-llm-top10-v2`. Bibliografia passa de 28 para 29 entradas. |
| 1.6 | 2026-05-23 | Patch v6 (rev-06 diagramas/referências): adiciona 3 entradas (`brasil2018-lgpd`, `eu2016-gdpr`, `anpd2024-res19`) para normas que eram citadas no crosswalk sem entrada formal. Bibliografia passa de 29 para 32 entradas. |
| 1.7 | 2026-05-23 | Patch v7 (rev-07 diagramas/referências): corrige URL `eu2016-gdpr` (EUR-Lex 202 WAF → Publications Office 200 RDF) e introduz seção "Política bibliográfica para normas citadas no crosswalk" delimitando entradas obrigatórias × menções setoriais/contextuais. |
