# Contribuidores

Este projeto distingue **autoria** (responsável pela obra) de **contribuição** (revisão crítica, sugestões, correções, exemplos) e credita ambas formalmente.

## Política de co-autoria por versão

A partir da **v1.1**, cada contribuição revisada e incorporada é creditada de três formas:

1. **Release notes** da versão que incorpora a contribuição, com menção nominal e descrição da contribuição.
2. **CITATION.cff**, no campo apropriado (`authors` quando a contribuição configurar coautoria substantiva conforme política abaixo; menção em comentário ou em `references` quando for contribuição pontual).
3. **DOI Zenodo próprio** da nova versão (cada release gera um Version DOI distinto sob o mesmo Concept DOI), tornando a contribuição **citável de forma independente e permanente**.

## Como contribuir

| Tipo de contribuição | Mecanismo | Onde fica registrado |
|---|---|---|
| Correção de fato (erro, link quebrado, citação incorreta) | Issue ou PR | release notes; commit history |
| Sugestão de melhoria editorial (clareza, escopo, redação) | Issue ou PR com proposta | release notes; commit history |
| Adição de seção, exemplo prático ou anexo | PR substantivo | release notes; CITATION.cff (`authors`) se configurar coautoria |
| Revisão crítica documentada (com comentários nominais sobre seções específicas) | Issue de revisão ou documento anexo | release notes; CONTRIBUTORS.md |

Todo feedback fica versionado no histórico do repositório (Issues, PRs, commits) e é parte do material derivado quando publicado.

## Critérios para coautoria substantiva

Uma contribuição é elevada a **coautoria** (entrada em `authors` no CITATION.cff e na próxima publicação) quando atende, no mínimo, a um destes critérios:

- Revisão crítica detalhada de uma ou mais seções (≥ 1 página/seção do artigo principal), com comentários acionáveis incorporados.
- Adição substantiva de conteúdo técnico (≥ 1 seção, anexo, artefato ou diagrama).
- Revisão regulatória ou arquitetural especializada (ex.: validação contra Microsoft CAF/Foundry, conformidade NIST/ISO, requisitos setoriais).
- Contribuição editorial estrutural (reorganização de capítulos, reescrita significativa, padronização de glossário/terminologia).

Contribuições pontuais (correção de erros, sugestões isoladas) são creditadas nas release notes e neste arquivo, mas não configuram coautoria. A decisão final sobre enquadramento é do mantenedor principal, em diálogo com a pessoa que contribuiu.

## Atribuição em apresentações e materiais derivados

Sempre que o playbook for usado em apresentações executivas, propostas comerciais, capacitações ou consultorias derivadas:

- A versão de referência deve ser citada com o **DOI Zenodo** apropriado (preferencialmente o Version DOI da versão usada).
- Contribuidores listados na versão usada devem ser mencionados nos créditos do material derivado.

## Lista de contribuidores

> Esta lista será populada a partir da v1.1, conforme as contribuições forem revisadas e incorporadas.

_Nenhum contribuidor adicional listado até v1.0.2. Autoria: Ednei Monteiro._

## Mantenedor principal

- **Ednei Monteiro** — ORCID: [0009-0006-0765-4201](https://orcid.org/0009-0006-0765-4201)

## Licença

Ao contribuir, você concorda em licenciar sua contribuição sob os mesmos termos do projeto: [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE).
