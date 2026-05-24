# AI CoE Playbook

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20357199.svg)](https://doi.org/10.5281/zenodo.20357199)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

Guia prático, artigos e artefatos operacionais para estruturar, governar e evoluir Centros de Excelência em Inteligência Artificial (AI CoE / CoE de IA).

Este repositório começou com o artigo **Centro de Excelência em Inteligência Artificial (CoE de IA)** e evoluiu como um playbook vivo: artigo principal + artefatos operacionais (charter, RACI, avaliação de risco) + mecanismo de assessment de maturidade + diagramas + referências consolidadas.

## Conteúdo principal

### Artigo

- [`artigos/coe-ia-playbook.md`](artigos/coe-ia-playbook.md) — artigo principal em Markdown
- [`artigos/coe-ia-playbook.html`](artigos/coe-ia-playbook.html) — versão HTML standalone

### Artefatos operacionais

- [`artefatos/charter-coe-ia.md`](artefatos/charter-coe-ia.md) — charter-modelo resumido
- [`artefatos/raci-coe-ia.md`](artefatos/raci-coe-ia.md) — RACI de referência
- [`artefatos/template-avaliacao-risco-ia.md`](artefatos/template-avaliacao-risco-ia.md) — template de avaliação de risco operacional

### Assessment de maturidade

- [`assessment/README.md`](assessment/README.md) — mecanismo de assessment de maturidade com gates go/no-go, modos diagnóstico/auditoria e board pack executivo
- [`assessment/modelo-maturidade-coe-ia.md`](assessment/modelo-maturidade-coe-ia.md) — modelo de 10 dimensões × 4 níveis
- [`assessment/questionario-assessment.md`](assessment/questionario-assessment.md) — 50 perguntas com rubrica observável e marcações de criticidade
- [`assessment/criterios-pontuacao.md`](assessment/criterios-pontuacao.md) — escala, regras de contenção, gates operacionais e amostragem anti-gaming
- [`assessment/relatorio-template.md`](assessment/relatorio-template.md) — relatório auditável completo
- [`assessment/board-pack-template.md`](assessment/board-pack-template.md) — destilação executiva de uma página

### Diagramas (Mermaid)

- [`diagramas/01-hub-spoke-federado.md`](diagramas/01-hub-spoke-federado.md) — modelo hub-and-spoke + direitos de decisão
- [`diagramas/02-fluxo-intake-handoff.md`](diagramas/02-fluxo-intake-handoff.md) — ciclo de vida operacional com gates
- [`diagramas/03-modelo-maturidade.md`](diagramas/03-modelo-maturidade.md) — maturidade em 4 níveis e sinais de transição
- [`diagramas/04-arquitetura-plataforma.md`](diagramas/04-arquitetura-plataforma.md) — plataforma corporativa de IA
- [`diagramas/05-pipeline-llmops.md`](diagramas/05-pipeline-llmops.md) — pipeline LLMOps/MLOps
- [`diagramas/06-regimes-dados.md`](diagramas/06-regimes-dados.md) — regimes de dados (treino × inferência/RAG × logs)
- [`diagramas/07-fluxo-incidente.md`](diagramas/07-fluxo-incidente.md) — fluxo de resposta a incidente IA
- [`diagramas/08-matriz-risco-controles.md`](diagramas/08-matriz-risco-controles.md) — matriz risco × controles + gates go/no-go

### Referências e bibliografia

- [`referencias/bibliografia.bib`](referencias/bibliografia.bib) — 25 referências em BibTeX (LaTeX/Pandoc/Overleaf)
- [`referencias/bibliografia.json`](referencias/bibliografia.json) — 25 referências em CSL-JSON (Zotero/Mendeley)
- [`referencias/crosswalk-normativo.md`](referencias/crosswalk-normativo.md) — crosswalk NIST × ISO × EU AI Act × LGPD/GDPR + GPAI + anexo setorial BR
- [`referencias/matriz-fonte-secao.md`](referencias/matriz-fonte-secao.md) — fonte × seção × recomendação + risco editorial
- [`referencias/auditoria-referencias.md`](referencias/auditoria-referencias.md) — memória operacional (removidas, correções, política de URLs)
- [`referencias/leituras-complementares.md`](referencias/leituras-complementares.md) — fontes consultadas e não citadas

## Estrutura

```text
ai-coe-playbook/
  README.md
  LICENSE
  CITATION.cff
  CONTRIBUTORS.md
  artigos/
    coe-ia-playbook.md
    coe-ia-playbook.html
  artefatos/
    README.md
    charter-coe-ia.md
    raci-coe-ia.md
    template-avaliacao-risco-ia.md
  assessment/
    README.md
    modelo-maturidade-coe-ia.md
    questionario-assessment.md
    criterios-pontuacao.md
    relatorio-template.md
    board-pack-template.md
  diagramas/
    README.md
    01-hub-spoke-federado.md
    02-fluxo-intake-handoff.md
    03-modelo-maturidade.md
    04-arquitetura-plataforma.md
    05-pipeline-llmops.md
    06-regimes-dados.md
    07-fluxo-incidente.md
    08-matriz-risco-controles.md
  referencias/
    README.md
    bibliografia.bib
    bibliografia.json
    crosswalk-normativo.md
    matriz-fonte-secao.md
    leituras-complementares.md
    auditoria-referencias.md
```

## Escopo

O material é uma **revisão narrativa orientada à prática**, voltada a líderes de tecnologia, arquitetura, dados, segurança, risco, compliance e produto que precisam criar ou evoluir um CoE de IA corporativo.

O repositório não substitui avaliação jurídica, regulatória ou arquitetural específica. Templates e exemplos devem ser adaptados ao contexto da organização, setor, jurisdição, apetite de risco e maturidade operacional.

## Como navegar

| Quero… | Comece por |
|---|---|
| Entender o que é um CoE de IA e como estruturá-lo | [`artigos/coe-ia-playbook.md`](artigos/coe-ia-playbook.md) |
| Adaptar artefatos para minha organização | [`artefatos/`](artefatos/) — charter, RACI, avaliação de risco |
| Avaliar a maturidade do meu CoE | [`assessment/README.md`](assessment/README.md) |
| Ver os fluxos e modelos em imagem | [`diagramas/`](diagramas/) — 8 diagramas Mermaid |
| Citar o playbook em outro material | [`referencias/bibliografia.bib`](referencias/bibliografia.bib) ou [`CITATION.cff`](CITATION.cff) |
| Entender qual norma cobre qual controle | [`referencias/crosswalk-normativo.md`](referencias/crosswalk-normativo.md) |

## Contribuindo

Este projeto distingue **autoria** de **contribuição** e credita ambas formalmente (release notes, `CITATION.cff`, `CONTRIBUTORS.md` e DOI Zenodo próprio de cada versão).

Política completa, critérios para coautoria substantiva e mecanismos de atribuição em [`CONTRIBUTORS.md`](CONTRIBUTORS.md).

A partir da **v1.1**, contribuições revisadas e incorporadas são creditadas nominalmente.

## Licença

Conteúdo textual, artigos, diagramas e templates estão licenciados sob **Creative Commons Attribution 4.0 International (CC BY 4.0)**. Consulte [`LICENSE`](LICENSE).

## Como citar

Esta release está arquivada no **Zenodo** com DOI permanente:

- **Concept DOI (sempre aponta para a versão mais recente):** [10.5281/zenodo.20357199](https://doi.org/10.5281/zenodo.20357199)
- **Version DOI (v1.0.2 — versão recomendada para revisão por pares):** [10.5281/zenodo.20361901](https://doi.org/10.5281/zenodo.20361901)

Metadados de citação em [`CITATION.cff`](CITATION.cff) (use o botão **"Cite this repository"** no canto superior direito desta página). Exemplo de citação:

> Monteiro, E. (2026). *AI CoE Playbook: Guia Prático para Estruturar, Operar e Escalar um Centro de Excelência em IA* (v1.0.2). Zenodo. https://doi.org/10.5281/zenodo.20361901
