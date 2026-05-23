# Diagrama 5 — Pipeline LLMOps/MLOps

Este diagrama mostra o ciclo operacional de versionamento, avaliação, regressão e operação segura de uma solução de IA. O foco é **rastreabilidade**: cada release é traceable até modelo, prompt, embedding, corpus, retriever, tool schema, guardrail e resultado de evals. Sem isso, rollback seletivo e auditoria pós-incidente ficam inviáveis.

## Pipeline ponta a ponta

**[Descrição acessível]:** flowchart top-bottom com seis subgrupos coloridos: Ingestão & Data Prep (âmbar) com fontes/lineage/embeddings/golden datasets; Desenvolvimento (azul) com versionamento + hash/snapshot; Avaliação (azul) com evals em golden datasets, métricas e harness integrity; Produção (verde) com deploy canary e SLO; Observabilidade (roxo) com métricas, drift e amostragem; Mecanismos de Segurança (vermelho) com fallback, rollback e kill switch. Dois gates amarelos (G1 release; G2 mudança relevante) interrompem o fluxo. Setas mostram que Ingestão alimenta Dev e golden datasets para Eval; falhas no G1 retornam ao Dev; incidentes em produção disparam SAFE que retroalimenta Dev.

```mermaid
flowchart TB
    classDef ingest fill:#9a6700,stroke:#633c01,color:#fff
    classDef dev fill:#1f6feb,stroke:#0d419d,color:#fff
    classDef gate fill:#fff8c5,stroke:#9a6700,color:#24292f
    classDef prod fill:#1a7f37,stroke:#0a4d20,color:#fff
    classDef safety fill:#cf222e,stroke:#82071e,color:#fff
    classDef monitor fill:#8250df,stroke:#3e1f79,color:#fff

    subgraph INGEST["Ingestão & data prep"]
        direction LR
        IN1["Fontes (catálogo<br/>de dados, owners,<br/>classificação)"]:::ingest
        IN2["Limpeza + lineage<br/>+ deduplicação"]:::ingest
        IN3["Chunking + embeddings<br/>+ índice vetorial<br/>(versionados com hash)"]:::ingest
        IN4["Golden datasets<br/>de eval (curados,<br/>com hash)"]:::ingest
    end

    subgraph DEV["Desenvolvimento"]
        direction LR
        D1["Versionar:<br/>modelo, prompt,<br/>embeddings, corpus,<br/>retriever, tool schema,<br/>guardrails"]:::dev
        D2["Build com hash<br/>+ snapshot"]:::dev
    end

    subgraph EVAL["Avaliação"]
        direction LR
        E1["Evals em<br/>golden datasets"]:::dev
        E2["Métricas:<br/>groundedness,<br/>safety, security,<br/>custo, latência"]:::dev
        E3["Harness integrity:<br/>judge ≠ família<br/>do gerador"]:::dev
    end

    G1{"Gate de release<br/>(thresholds por risco)"}:::gate

    subgraph PROD["Produção"]
        direction LR
        P1["Deploy<br/>(canary / blue-green)"]:::prod
        P2["Tráfego real<br/>+ SLO + on-call"]:::prod
    end

    subgraph MON["Observabilidade"]
        direction LR
        M1["Métricas por<br/>aplicação<br/>(L4)"]:::monitor
        M2["Drift, degradação,<br/>alucinação, custo,<br/>feedback"]:::monitor
        M3["Amostragem +<br/>revisão humana"]:::monitor
        M4["Eval online<br/>(LLM-as-judge contínuo,<br/>groundedness, faithfulness<br/>por amostra)"]:::monitor
    end

    subgraph SAFE["Mecanismos de segurança"]
        direction LR
        S1["Fallback<br/>(provider alternativo)"]:::safety
        S2["Rollback<br/>(versão anterior)"]:::safety
        S3["Kill switch<br/>por agente/fluxo"]:::safety
    end

    G2{"Mudança<br/>relevante?"}:::gate

    DEV --> EVAL --> G1
    G1 -->|aprovado| PROD
    INGEST --> DEV
    INGEST -.->|golden datasets<br/>versionados| EVAL
    G1 -->|falhou eval / threshold| DEV

    PROD --> MON
    MON --> G2
    G2 -->|modelo, prompt,<br/>corpus, retriever,<br/>política mudou| EVAL
    G2 -->|incidente / degradação| SAFE
    SAFE -.->|remediação| DEV
```

## Trigger de regressão

**[Descrição acessível]:** flowchart esquerda-direita listando seis gatilhos amarelos (troca de modelo, mudança de prompt, tool schema/allowlist, corpus/chunking/retriever, política de recuperação, guardrail) que convergem em um único nó verde "Regressão obrigatória contra golden datasets versionados". A regressão alimenta um gate "Thresholds atendidos?" — sim libera release; não bloqueia e retorna para iteração.

```mermaid
flowchart LR
    classDef trigger fill:#fff8c5,stroke:#9a6700,color:#24292f
    classDef action fill:#1a7f37,stroke:#0a4d20,color:#fff

    T1[/"Troca de modelo<br/>ou versão"/]:::trigger
    T2[/"Mudança de<br/>prompt"/]:::trigger
    T3[/"Mudança de<br/>tool schema<br/>ou allowlist"/]:::trigger
    T4[/"Mudança de<br/>corpus / chunking /<br/>retriever"/]:::trigger
    T5[/"Mudança de<br/>política de<br/>recuperação"/]:::trigger
    T6[/"Mudança de<br/>guardrail"/]:::trigger

    REG["<b>Regressão obrigatória</b><br/>contra golden datasets<br/>versionados"]:::action

    T1 --> REG
    T2 --> REG
    T3 --> REG
    T4 --> REG
    T5 --> REG
    T6 --> REG

    REG --> GATE{"Thresholds<br/>atendidos?"}
    GATE -->|sim| OK(["Release autorizada"])
    GATE -->|não| BLOCK(["Release bloqueada;<br/>volta para iteração"])
```

## Estados de uma versão em produção

**[Descrição acessível]:** state diagram mostrando o ciclo de vida de uma versão: Em Desenvolvimento → Em Avaliação → (Rejeitado no Gate ou Em Canary) → Em Produção → Em Investigação → (Em Produção / Rolled Back / Kill Switch Ativado). Kill Switch Ativado é estado terminal. Rolled Back e Rejeitado retornam ao Desenvolvimento.

```mermaid
stateDiagram-v2
    [*] --> EmDesenvolvimento
    EmDesenvolvimento --> EmAvaliação: build versionado<br/>com hash
    EmAvaliação --> RejeitadoNoGate: thresholds não atendidos
    EmAvaliação --> EmCanary: gate aprovado
    EmCanary --> EmProdução: rollout completo<br/>sem regressão
    EmCanary --> RolledBack: regressão detectada<br/>em canary
    EmProdução --> EmInvestigação: degradação,<br/>drift ou incidente
    EmInvestigação --> EmProdução: causa contornada
    EmInvestigação --> RolledBack: rollback acionado
    EmInvestigação --> KillSwitchAtivado: kill switch<br/>(agente externo /<br/>alto risco)
    RejeitadoNoGate --> EmDesenvolvimento
    RolledBack --> EmDesenvolvimento
    KillSwitchAtivado --> [*]
```

## Como ler

- **L1 = versionamento total.** Sem versionar embeddings, índices, retriever e tool schemas, não há reprodutibilidade — o release não é auditável. Prompts versionados em D1 são registrados no catálogo de Diag.04/CP1 (modelos, prompts, templates) — o prompt registry vive na plataforma, não na solução.
- **L2 = evals com harness integrity.** O judge não pode ser da mesma família do gerador (evita circular evaluation). Hash do golden dataset prova que o teste não foi modificado para passar.
- **L3 = regressão em toda mudança relevante.** Qualquer um dos 6 gatilhos da segunda figura obriga regressão; sem isso, o release não pode ir para produção (gate bloqueia).
- **L4 = monitoramento por aplicação.** A plataforma oferece capacidade (P5); a solução tem que instrumentar e usar. **M4 (eval online) é distinto de M1/M2**: M1/M2 são métricas operacionais (latência, custo, drift estatístico); M4 é eval semântica contínua em produção (groundedness, faithfulness, qualidade de resposta) via LLM-as-judge ou amostragem humana. Owner: mesmo da suite de evals offline (EVAL); threshold de amostragem define custo e latência de coleta.
- **L5 = fallback + rollback + contenção testados.** Para agentes externos ou de alto risco, a contenção é obrigatória e por agente/fluxo, não global.

Referências cruzadas: ver `assessment/questionario-assessment.md` dimensão "LLMOps/MLOps e evals" (L1–L5) e `referencias/crosswalk-normativo.md` (Measure / Manage no NIST AI RMF; A.6.2.5 / A.6.2.7 no ISO 42001).
