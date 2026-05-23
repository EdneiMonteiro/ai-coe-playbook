# Diagrama 1 — Hub-and-spoke e modelo federado/híbrido

Este diagrama mostra a essência do modelo operacional de um CoE de IA: um **hub central** que define padrões, governança, plataforma e ativos reutilizáveis, e **spokes federados** (squads de produto, plataforma e dados) que executam casos de uso dentro desses padrões. O CoE pode incubar PoCs/MVPs estratégicos, mas o ownership operacional é transferido para os spokes via **build-to-transfer**.

## Hub-and-spoke conceitual

```mermaid
flowchart TB
    classDef hub fill:#1f6feb,stroke:#0d419d,color:#fff,stroke-width:2px
    classDef spoke fill:#f6f8fa,stroke:#57606a,color:#24292f
    classDef gov fill:#fff8c5,stroke:#9a6700,color:#24292f

    HUB["<b>CoE de IA — Hub</b><br/>Padrões · Governança · Plataforma<br/>Capacitação · Catálogo · Evals"]:::hub

    GOV["Segurança, Risco<br/>Compliance, DPO"]:::gov

    S1["Spoke<br/><b>Produto / Negócio</b>"]:::spoke
    S2["Spoke<br/><b>Plataforma / Cloud</b>"]:::spoke
    S3["Spoke<br/><b>Dados</b>"]:::spoke
    S4["Spoke<br/><b>Squads de domínio</b><br/>(BU 1, BU 2, BU n)"]:::spoke

    HUB <--> GOV
    HUB --> S1
    HUB --> S2
    HUB --> S3
    HUB --> S4
    S1 -. feedback .-> HUB
    S2 -. feedback .-> HUB
    S3 -. feedback .-> HUB
    S4 -. feedback .-> HUB
```

## Direitos de decisão no modelo federado

```mermaid
flowchart LR
    classDef coe fill:#1f6feb,stroke:#0d419d,color:#fff
    classDef prod fill:#1a7f37,stroke:#0a4d20,color:#fff
    classDef plat fill:#9a6700,stroke:#633c01,color:#fff
    classDef risk fill:#cf222e,stroke:#82071e,color:#fff
    classDef spon fill:#8250df,stroke:#3e1f79,color:#fff

    COE["<b>CoE de IA</b><br/>padrões mínimos<br/>catálogo de modelos<br/>critérios de avaliação<br/>requisitos de observabilidade<br/>DoD de handoff"]:::coe

    PROD["<b>Produto / Negócio</b><br/>backlog funcional<br/>experiência do usuário<br/>priorização de domínio<br/>evolução do produto"]:::prod

    PLAT["<b>Plataforma / Cloud</b><br/>provisionamento<br/>automação · integração<br/>monitoramento<br/>operação técnica"]:::plat

    RISK["<b>Segurança / Risco / Compliance</b><br/>controles obrigatórios<br/>poder de veto em alto risco<br/>parecer jurídico anexado<br/>(quando aplicável)"]:::risk

    SPON["<b>Sponsor Executivo</b><br/>trade-offs de investimento<br/>risco residual<br/>go/no-go em impacto material<br/>árbitro de escalada"]:::spon

    COE  ---|"dentro dos padrões"| PROD
    COE  ---|"operação técnica"| PLAT
    RISK -.->|veto / escalada| SPON
    PROD -.->|escalada de conflito| SPON
    COE  -.->|escalada de conflito| SPON
```

## Como ler

- O **hub** decide o que é comum (padrões, plataforma, governança). Os **spokes** decidem o que é específico do domínio.
- **Segurança/Risco/Compliance** tem poder de veto em casos de alto risco; conflitos com o CoE escalam ao Sponsor com prazo definido (Charter §5).
- A seta `feedback` materializa o princípio "padrões evoluem com o uso real": squads informam o hub sobre lacunas e necessidades.
- **Jurídico**, **DPO**, **Auditoria Interna** e **Procurement** entram como colunas independentes do RACI quando a organização é regulada (ver `artefatos/raci-coe-ia.md`).
