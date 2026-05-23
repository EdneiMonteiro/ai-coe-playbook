# Auditoria de referências

Esta página registra a memória operacional das referências do AI CoE Playbook: o que foi incluído, o que foi removido, o que foi corrigido e por quê. O objetivo é dar **rastreabilidade longitudinal** ao corpo de fontes, especialmente em casos de mudança regulatória ou perda de acesso.

## Princípios

- **Referência publicável** = URL acessível publicamente, conteúdo estável, fonte primária ou secundária verificável.
- **Remoção registrada** = quando uma fonte é removida do artigo principal, o motivo fica documentado aqui.
- **Correção registrada** = quando uma fonte foi citada incorretamente (revogada, mislabeled, número errado), a correção e a origem do erro ficam documentadas.
- **Verificação de vigência** = validar existência **e** vigência de uma norma; o anti-pattern *validator search* (confirmar só existência) foi a causa de duas regressões na história do playbook.

## Referências removidas e por quê

| Fonte | Tipo | Motivo da remoção | Quando | Substituta |
|---|---|---|---|---|
| **Gartner** (várias publicações) | Analista | Conteúdo restrito a assinantes; não permite verificação pública | Audit inicial (pré-rev-01 do artigo) | Recomendações cruzadas de IBM, Microsoft CAF, KPMG, Deloitte, Oracle/CIO |
| **SalesChoice** | Vendor | Página/PDF apresentava 403 anti-bot em acessos automatizados; instabilidade de acesso comprometia auditoria | Audit inicial | Recomendações cruzadas de fornecedores estáveis |
| **UST** | Vendor | Inicialmente acessível, depois 403/timeout intermitente | Audit inicial | Recomendações cruzadas de fornecedores estáveis |
| **BACEN Res. 4.658/2018** | Norma setorial BR | **Revogada em 01/07/2023** — citada como vigente no Anexo C-BR | Patch v5 (assessment rev-06) | **CMN Res. 4.893/2021** (bancos e cooperativas) + **BCB Res. 85/2021** (IPs e demais autorizadas pelo BCB) |
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

## Política de verificação de URLs

Para o conjunto de **25 referências** atualmente publicadas no artigo principal (`artigos/coe-ia-playbook.md`):

- **Frequência:** verificar todas as URLs antes de cada release major do playbook.
- **Escopo:** status HTTP, presença do título esperado, ausência de redirecionamento para página de erro/login.
- **Anti-padrão "validator search":** ao adicionar nova norma, exigir busca adversarial ("norma X foi revogada?" "qual é o objeto real?") — não apenas confirmação de existência.
- **Última verificação consolidada:** maio/2026, antes da publicação do artigo principal — 25/25 URLs OK, 0 restritas, 0 anti-bot.

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

## Histórico de revisão deste documento

| Versão | Data | Mudança |
|---|---|---|
| 1.0 | 2026-05-23 | Criação. Consolida 4 audits anteriores (removidas + correções + verificação + universo consultado). |
