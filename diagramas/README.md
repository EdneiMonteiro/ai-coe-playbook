# Diagramas

Diagramas visuais que complementam os artefatos textuais do playbook. Todos em **Mermaid** (renderiza nativamente no GitHub e é versionável em texto).

## Diagramas disponíveis

### Modelo organizacional

- [`01-hub-spoke-federado.md`](01-hub-spoke-federado.md): Modelo hub-and-spoke do CoE + direitos de decisão no modelo federado/híbrido.

### Operação

- [`02-fluxo-intake-handoff.md`](02-fluxo-intake-handoff.md): Ciclo de vida operacional: intake → PoC → MVP → produção → handoff, com gates go/no-go.
- [`07-fluxo-incidente.md`](07-fluxo-incidente.md): Fluxo de resposta a incidente IA (detecção, contenção, investigação, remediação, postmortem) + SLA por severidade.

### Maturidade

- [`03-modelo-maturidade.md`](03-modelo-maturidade.md): Modelo de maturidade em 4 níveis, perfil por dimensão e sinais de transição.

### Arquitetura e técnico

- [`04-arquitetura-plataforma.md`](04-arquitetura-plataforma.md): Plataforma corporativa de IA: landing zone, ambientes, catálogo, guardrails, observabilidade, FinOps, dados.
- [`05-pipeline-llmops.md`](05-pipeline-llmops.md): Pipeline LLMOps/MLOps: versionamento, evals, regressão, fallback, kill switch.
- [`06-regimes-dados.md`](06-regimes-dados.md): Regimes de dados (treino/fine-tuning × inferência/RAG × logs de interação) + controles obrigatórios + mapa de risco regulatório.

### Risco e governança

- [`08-matriz-risco-controles.md`](08-matriz-risco-controles.md): Mapa EU AI Act → classificação interna + controles obrigatórios por nível + fluxo de gates go/no-go.

## Convenções

- **Mermaid** sempre que possível (versionável, renderiza no GitHub).
- **draw.io com XML embutido** para diagramas com layout livre.
- **SVG** para versões polidas (ex.: board pack, comunicação externa).
- Evitar PNG sem fonte editável.
