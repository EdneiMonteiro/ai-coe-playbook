# Referências

Conteúdo operacional sobre as referências do AI CoE Playbook. A bibliografia narrativa completa permanece no artigo principal (`../artigos/coe-ia-playbook.md`); esta pasta consolida material reutilizável, citável e rastreável.

## Conteúdo

### Bibliografia citável

- [`bibliografia.bib`](bibliografia.bib): Exportação **BibTeX** com 32 entradas: as 25 referências numeradas do artigo principal mais 7 instrumentos normativos citados em `crosswalk-normativo.md` e nos diagramas (NIST SP 800-61 Rev. 3, GPAI Code of Practice, OWASP LLM Top 10 v2.0, LGPD, GDPR, ANPD Res. 15/2024, ANPD Res. 19/2024). Para LaTeX, Pandoc, Overleaf.
- [`bibliografia.json`](bibliografia.json): Exportação **CSL-JSON** com as mesmas 32 entradas. Para Zotero, Mendeley e qualquer ferramenta CSL-aware.

### Operacional

- [`crosswalk-normativo.md`](crosswalk-normativo.md): Crosswalk entre NIST AI RMF, ISO/IEC 42001, EU AI Act, LGPD e GDPR; especificidades GPAI Arts. 51–55; anexo setorial BR; instrumentos de transferência internacional. Reutilizado pelo assessment e pelo artigo.
- [`matriz-fonte-secao.md`](matriz-fonte-secao.md): Matriz cruzando fonte × seção do playbook × recomendação derivada; análise de risco de dependência editorial.
- [`leituras-complementares.md`](leituras-complementares.md): Fontes consultadas durante as revisões mas não citadas no artigo (OWASP LLM Top 10, FinOps Foundation, NACD, ANPD CCPs, model/system cards, ISO 19011 etc.), separadas por área.
- [`auditoria-referencias.md`](auditoria-referencias.md): Memória operacional das referências: removidas e por quê, correções de citação, política de verificação de URLs e universo consultado.

## Convenções

- **Chaves BibTeX/CSL** seguem o padrão `<autor-curto><ano>-<token>` (ex.: `microsoft2025-coe`, `nist2024-genaiprofile`, `kolbjornsrud2024-intelligent`). Itens corporativos usam `<org><ano>-<token>`.
- **Sincronização:** ao adicionar nova referência no artigo principal, replicar em `bibliografia.bib`, `bibliografia.json` e `matriz-fonte-secao.md`.
- Quando o **crosswalk normativo** for atualizado, atualizar também a referência cruzada em:
  - `assessment/relatorio-template.md` (Anexo C)
  - `artigos/coe-ia-playbook.md` (apêndice de referências regulatórias, quando aplicável)
