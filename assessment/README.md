# Assessment de maturidade do CoE de IA

Este diretório contém um mecanismo prático para avaliar a maturidade de um Centro de Excelência em IA usando o modelo de quatro níveis descrito no artigo principal:

1. **Reativo** — experimentação isolada, sem coordenação.
2. **Executor** — CoE centralizado, primeiros padrões e PoCs/MVPs.
3. **Habilitador** — plataforma, padrões, guardrails e squads autônomos.
4. **Transformador** — CoE consultivo, IA integrada à estratégia e melhoria contínua.

## Escopo e limites

Este assessment mede **maturidade organizacional do CoE de IA**. Ele não certifica conformidade regulatória, não substitui auditoria jurídica, não substitui auditoria de sistema de gestão e não constitui parecer sobre aderência a ISO/IEC 42001, EU AI Act, LGPD, GDPR ou regulações setoriais.

Referências a NIST AI RMF, ISO/IEC 42001, EU AI Act e frameworks similares são usadas como **heurísticas de medição e organização de evidências**. Para uso externo, regulado, due diligence, funding, M&A ou comunicação pública de conformidade, o assessment deve ser complementado por revisão jurídica/regulatória e, quando aplicável, asseguração independente.

## Arquivos

- [`modelo-maturidade-coe-ia.md`](modelo-maturidade-coe-ia.md) — dimensões avaliadas e descrição dos níveis.
- [`questionario-assessment.md`](questionario-assessment.md) — perguntas de avaliação com evidências esperadas.
- [`criterios-pontuacao.md`](criterios-pontuacao.md) — escala, fórmula, critérios de nivelamento e regras de contenção.
- [`relatorio-template.md`](relatorio-template.md) — relatório auditável completo, com trilha pergunta-evidência-nota.
- [`board-pack-template.md`](board-pack-template.md) — resumo executivo de uma página para decisão de board/C-level.

## Como aplicar

1. **Preparar** — definir escopo, unidades avaliadas, sponsor, participantes e modo de aplicação: diagnóstico interno ou auditoria/investimento.
2. **Classificar contexto operacional** — separar PoC, MVP, produção, produção crítica, exposição externa, alto risco e expansão.
3. **Coletar evidências** — políticas, artefatos, repositórios, dashboards, atas, trilhas de auditoria, templates, logs, registros de decisão e exemplos de projetos.
4. **Amostrar** — quando houver produção, avaliar pelo menos três soluções por dimensão operacionalmente relevante, ou todas se houver menos de três.
5. **Pontuar** — responder ao questionário usando a escala 0–4, rubricas por pergunta e regras de contenção.
6. **Aplicar gates go/no-go** — separar nível de maturidade da decisão de permitir, restringir ou bloquear produção/expansão.
7. **Validar** — revisar resultados com CoE, produto, plataforma, dados, segurança, risco/compliance e sponsor.
8. **Reportar** — produzir relatório auditável completo e, quando houver decisão executiva, board pack de uma página.
9. **Planejar evolução** — transformar lacunas em roadmap 30/60/90 dias e backlog de maturidade.

## Quando usar

- Antes de criar formalmente um CoE de IA.
- Ao final dos primeiros PoCs/MVPs.
- Antes de escalar para modelo federado.
- Como revisão trimestral/semestral de maturidade.
- Como diagnóstico independente antes de investimento em plataforma, governança ou capacitação.

## Princípio importante

O assessment deve avaliar **evidência operacional**, não intenção. Uma prática só deve receber pontuação alta quando houver artefato verificável, uso recorrente e accountability definido.

## Separação essencial

- **Pontuação de maturidade**: mede a capacidade organizacional do CoE de IA.
- **Go/no-go operacional**: decide se um caso de uso pode avançar para MVP, produção ou expansão.

Um caso pode receber **veto operacional** mesmo que a organização tenha boa pontuação geral. Exemplos: produção sem classificação formal de risco, sem incident response IA, sem AI red teaming quando aplicável, sem FRIA/DPIA aplicável, ou sem fallback/kill switch em agentes de alto risco.

## Modos de aplicação

| Modo | Quando usar | Rigor mínimo |
|---|---|---|
| Diagnóstico interno | Baseline, priorização e melhoria interna | Um avaliador, evidências principais, amostragem proporcional e ressalvas explícitas. |
| Auditoria/investimento | Board pack, decisão de funding, aplicação em cliente, ambiente regulado ou produção crítica | Dois avaliadores, matriz de rastreabilidade, amostragem mínima, tratamento formal de divergência e gates go/no-go. |
