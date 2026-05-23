# Diagrama 7 — Fluxo de incidente de IA

Este diagrama mostra o ciclo de resposta a incidente quando uma solução de IA em produção falha, vaza, alucina criticamente, é usada indevidamente ou exibe comportamento fora do esperado. **Incident response IA não é o mesmo que incident response geral**: tem categorias próprias (alucinação, jailbreak, vazamento, excessive agency, drift material) e mecanismos próprios (kill switch por agente, rollback de modelo/prompt, evals adversariais).

## Fluxo end-to-end

```mermaid
flowchart TB
    classDef prep fill:#1f6feb,stroke:#0d419d,color:#fff
    classDef detect fill:#fff8c5,stroke:#9a6700,color:#24292f
    classDef triage fill:#1f6feb,stroke:#0d419d,color:#fff
    classDef contain fill:#cf222e,stroke:#82071e,color:#fff
    classDef investigate fill:#9a6700,stroke:#633c01,color:#fff
    classDef remediate fill:#1a7f37,stroke:#0a4d20,color:#fff
    classDef learn fill:#8250df,stroke:#3e1f79,color:#fff

    subgraph PREP["Preparation (NIST SP 800-61 §3.1 / SANS PICERL)"]
        direction LR
        P1["Runbooks publicados<br/>+ versionados"]:::prep
        P2["Kill switches testados<br/>(por agente / fluxo)"]:::prep
        P3["On-call configurado<br/>+ rotações + escalação"]:::prep
        P4["Comunicações<br/>pré-aprovadas<br/>(jurídico, PR, regulador)"]:::prep
        P5["Tabletop exercises<br/>+ revisão periódica"]:::prep
    end

    subgraph DETECT["Detecção"]
        direction LR
        D1["Monitoramento<br/>(drift, alucinação,<br/>custo, latência)"]:::detect
        D2["Feedback do usuário<br/>/ canal de incidente"]:::detect
        D3["Eval em produção<br/>(amostragem)"]:::detect
        D4["Alerta de guardrail<br/>(PII, jailbreak,<br/>excessive agency)"]:::detect
    end

    TRIAGE{"<b>Triagem</b><br/>Severidade?<br/>Escopo de impacto?<br/>Tipo de incidente?"}:::triage

    subgraph CONTAIN["Contenção imediata"]
        direction LR
        C1["Fallback para<br/>versão anterior<br/>ou provider alternativo"]:::contain
        C2["Kill switch<br/>(agente ou fluxo)"]:::contain
        C3["Bloqueio temporário<br/>do caso de uso"]:::contain
        C4["Comunicação aos<br/>usuários afetados"]:::contain
    end

    subgraph INV["Investigação"]
        direction LR
        I1["Coleta de logs e<br/>traces da janela<br/>do incidente"]:::investigate
        I2["Reprodução em<br/>ambiente isolado"]:::investigate
        I3["Análise de causa<br/>(modelo, prompt,<br/>dados, retriever,<br/>guardrail, tool)"]:::investigate
    end

    subgraph REM["Remediação"]
        direction LR
        R1["Correção técnica<br/>(prompt, modelo, dados,<br/>guardrail, schema)"]:::remediate
        R2["Regressão obrigatória<br/>em golden datasets"]:::remediate
        R3["Atualização de<br/>kill switch / fallback /<br/>rollback"]:::remediate
        R4["Re-aprovação no gate<br/>de produção"]:::remediate
    end

    subgraph LEARN["Aprendizado"]
        direction LR
        L1["Postmortem<br/>(sem blame)"]:::learn
        L2["Atualização de<br/>padrões, runbooks,<br/>evals e guardrails"]:::learn
        L3["Comunicação à<br/>comunidade de prática"]:::learn
        L4["Reporte regulatório:<br/>BACEN Res. 4.893/2021 Art. 6º;<br/>ANPD Res. 15/2024 (≤72h);<br/>EU AI Act Art. 73 (2/10/15 d.);<br/>LGPD Art. 48; GDPR Art. 33"]:::learn
    end

    PREP --> DETECT
    DETECT --> TRIAGE
    TRIAGE -->|crítico ou alto| CONTAIN
    TRIAGE -->|médio ou baixo| INV
    CONTAIN --> INV
    INV --> REM
    REM --> LEARN
    LEARN -.->|melhorias no<br/>pipeline| DETECT
    LEARN -.->|atualiza runbooks,<br/>kill switches, comunicações| PREP
```

## Severidade e SLA de resposta

```mermaid
flowchart TB
    classDef sev fill:#f6f8fa,stroke:#57606a,color:#24292f
    classDef sla fill:#fff8c5,stroke:#9a6700,color:#24292f

    SEV1["<b>SEV-1 — Crítico</b><br/>vazamento de dados sensíveis,<br/>dano legal/financeiro material,<br/>agente externo com<br/>excessive agency confirmada"]:::sev
    SEV2["<b>SEV-2 — Alto</b><br/>alucinação crítica em decisão,<br/>jailbreak em produção,<br/>degradação material<br/>de qualidade"]:::sev
    SEV3["<b>SEV-3 — Médio</b><br/>drift relevante,<br/>aumento de erros,<br/>custo fora do esperado"]:::sev
    SEV4["<b>SEV-4 — Baixo</b><br/>queixa pontual,<br/>falsa positiva isolada,<br/>microincidente"]:::sev

    SLA1["Contenção imediata<br/>(< 15 min)<br/>+ comitê de risco<br/>+ reporte regulatório<br/>se aplicável"]:::sla
    SLA2["Contenção em horas<br/>+ sponsor informado<br/>+ postmortem em 5 dias"]:::sla
    SLA3["Mitigação em 1–2 dias<br/>+ postmortem em 10 dias"]:::sla
    SLA4["Backlog priorizado<br/>+ postmortem agregado"]:::sla

    SEV1 --> SLA1
    SEV2 --> SLA2
    SEV3 --> SLA3
    SEV4 --> SLA4
```

## Categorias específicas de incidente IA

```mermaid
flowchart LR
    classDef cat fill:#cf222e,stroke:#82071e,color:#fff
    classDef trigger fill:#fff8c5,stroke:#9a6700,color:#24292f

    A["Vazamento de PII<br/>em resposta ou log"]:::cat
    B["Alucinação crítica<br/>em decisão"]:::cat
    C["Jailbreak / prompt<br/>injection"]:::cat
    D["Excessive agency<br/>(agente executou<br/>ação não autorizada)"]:::cat
    E["Supply chain<br/>(modelo, embedding,<br/>tool comprometidos)"]:::cat
    F["Drift material<br/>(qualidade ou custo)"]:::cat
    G["Uso indevido por<br/>usuário (abuse)"]:::cat

    T1["LLM02<br/>(OWASP)"]:::trigger
    T2["NIST AI 600-1<br/>(confabulação)"]:::trigger
    T3["LLM01<br/>(OWASP)"]:::trigger
    T4["LLM06<br/>(OWASP)"]:::trigger
    T5["LLM03<br/>(OWASP)"]:::trigger
    T6["LLM10 / NIST<br/>Measure"]:::trigger
    T7["OWASP +<br/>política interna"]:::trigger

    A --- T1
    B --- T2
    C --- T3
    D --- T4
    E --- T5
    F --- T6
    G --- T7
```

## Como ler

- **Detecção não é só monitoramento técnico.** Inclui feedback do usuário, evals em produção e alertas de guardrail. Sem canal de incidente ativo, problemas viram silêncio.
- **Triagem decide se contém antes ou investiga primeiro.** SEV-1 e SEV-2 contêm imediatamente; SEV-3 e SEV-4 podem investigar primeiro.
- **Contenção tem 4 mecanismos** (fallback, kill switch, bloqueio, comunicação). Para agentes externos e alto risco, o kill switch é obrigatório (ver L5 no assessment).
- **Postmortem alimenta a plataforma.** Padrões, runbooks, evals e guardrails são atualizados — incidente vira melhoria sistêmica, não só fix pontual.
- **Reporte regulatório quando aplicável:** EU AI Act Art. 73 (incidente sério em alto risco), LGPD Art. 48 (vazamento de dados pessoais), GDPR Art. 33 (notificação à autoridade).
- Referências cruzadas: `assessment/questionario-assessment.md` G5 / O1–O5, `referencias/crosswalk-normativo.md` (tema "Monitoramento e incidente"), `artigos/coe-ia-playbook.md` (seção sobre incident response).
