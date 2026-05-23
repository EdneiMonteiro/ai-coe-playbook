# Diagrama 6 — Regimes de dados (treino × inferência/RAG × logs)

Este diagrama mostra a separação obrigatória entre **três regimes de dados** em sistemas de IA. Cada regime tem finalidade, base legal, retenção, controles e ciclo de vida próprios. Tratar tudo como "dados de IA" mistura responsabilidades e impede auditoria de privacidade — daí a inclusão como gate operacional em D2 do assessment.

## Os três regimes

```mermaid
flowchart TB
    classDef train fill:#1f6feb,stroke:#0d419d,color:#fff
    classDef infer fill:#1a7f37,stroke:#0a4d20,color:#fff
    classDef log fill:#9a6700,stroke:#633c01,color:#fff
    classDef control fill:#cf222e,stroke:#82071e,color:#fff

    subgraph TRAIN["Regime 1 — Treino / Fine-tuning"]
        direction TB
        T1["<b>Finalidade:</b> ajustar modelo<br/><b>Base legal:</b> revisão jurídica<br/>específica para uso de dados<br/>pessoais em treino"]:::train
        T2["<b>Conteúdo:</b> datasets curados,<br/>dados sintéticos com proveniência,<br/>preferências para RLHF"]:::train
        T3["<b>Retenção:</b> longa (versionada<br/>com o modelo)<br/><b>Direito de apagamento:</b> exige<br/>retrain ou unlearning"]:::train
    end

    subgraph INFER["Regime 2 — Inferência / RAG"]
        direction TB
        I1["<b>Finalidade:</b> responder usuário<br/>em tempo de execução<br/><b>Base legal:</b> definida por<br/>aplicação (contrato, legítimo<br/>interesse, consentimento)"]:::infer
        I2["<b>Conteúdo:</b> corpus RAG,<br/>embeddings, índice vetorial,<br/>políticas de recuperação"]:::infer
        I3["<b>Retenção:</b> conforme política<br/>do produto<br/><b>Direito de apagamento:</b> rebuild<br/>de embeddings ou purge<br/>seletivo"]:::infer
    end

    subgraph LOG["Regime 3 — Logs de interação"]
        direction TB
        L1["<b>Finalidade:</b> auditoria, evals,<br/>incident response<br/><b>Base legal:</b> exige declaração<br/>específica; não inferida do<br/>regime 2"]:::log
        L2["<b>Conteúdo:</b> prompts, respostas,<br/>tool calls, identificadores<br/>de sessão, metadados de eval"]:::log
        L3["<b>Retenção:</b> mínima necessária<br/>(curta por padrão)<br/><b>Direito de apagamento:</b> purge<br/>com tombstone para auditoria"]:::log
    end

    TRAIN -.->|<i>nunca compartilha</i><br/><i>controle de acesso</i>| INFER
    INFER -.->|<i>nunca compartilha</i><br/><i>controle de acesso</i>| LOG
    LOG -.->|<i>nunca alimenta</i><br/><i>treino sem consentimento</i><br/><i>explícito</i>| TRAIN
```

## Controles obrigatórios por regime

```mermaid
flowchart LR
    classDef tr fill:#1f6feb,stroke:#0d419d,color:#fff
    classDef inf fill:#1a7f37,stroke:#0a4d20,color:#fff
    classDef lg fill:#9a6700,stroke:#633c01,color:#fff

    subgraph TR_CTL["Controles — Treino"]
        TC1["Base legal específica<br/>para dados pessoais"]:::tr
        TC2["Proveniência dos dados<br/>(sintéticos declarados)"]:::tr
        TC3["Aprovação do data owner"]:::tr
        TC4["Teste de memorização<br/>e reidentificação"]:::tr
    end

    subgraph IN_CTL["Controles — Inferência/RAG"]
        IC1["Status de anonimização<br/>declarado (anonimizado /<br/>pseudonimizado / nenhum)"]:::inf
        IC2["Embeddings tratados como<br/>dados pseudonimizados<br/>por definição"]:::inf
        IC3["Política de recuperação<br/>versionada"]:::inf
        IC4["Rebuild de embeddings<br/>quando fonte muda<br/>ou é apagada"]:::inf
    end

    subgraph LG_CTL["Controles — Logs"]
        LC1["Política de retenção<br/>declarada"]:::lg
        LC2["Mascaramento/redacao<br/>de PII"]:::lg
        LC3["Purge automático<br/>+ tombstone para<br/>auditoria"]:::lg
        LC4["Acesso controlado<br/>(quem lê logs?)"]:::lg
    end

    TR_CTL ~~~ IN_CTL ~~~ LG_CTL
```

## Mapa de risco regulatório

```mermaid
flowchart TD
    classDef reg fill:#fff8c5,stroke:#9a6700,color:#24292f
    classDef risk fill:#cf222e,stroke:#82071e,color:#fff
    classDef ctl fill:#1a7f37,stroke:#0a4d20,color:#fff

    R1["LGPD Art. 6<br/>(princípios)"]:::reg
    R2["LGPD Art. 11<br/>(dados sensíveis)"]:::reg
    R3["LGPD Art. 18<br/>(direitos do titular)"]:::reg
    R4["LGPD Art. 33<br/>(transferência<br/>internacional)"]:::reg
    R5["GDPR Art. 17<br/>(direito ao apagamento)"]:::reg
    R6["GDPR Art. 9<br/>(categorias especiais)"]:::reg
    R7["EU AI Act<br/>Art. 10<br/>(data governance)"]:::reg

    AP1["PII em corpus RAG<br/>sem direito de<br/>apagamento implementado"]:::risk
    AP2["Logs com PII<br/>sem classificação<br/>nem retenção"]:::risk
    AP3["Sintéticos usados em eval<br/>sem teste de<br/>reidentificação"]:::risk
    AP4["Treino com dados<br/>pessoais sem base<br/>legal específica"]:::risk

    C1["Rebuild de embeddings<br/>+ purge seletivo"]:::ctl
    C2["Mascaramento + retenção<br/>+ tombstone"]:::ctl
    C3["Proveniência declarada<br/>+ aprovação owner"]:::ctl
    C4["Revisão jurídica antes<br/>do treino"]:::ctl

    R3 --> AP1 --> C1
    R5 --> AP1
    R7 --> AP1
    R2 --> AP2 --> C2
    R6 --> AP2
    R3 --> AP2
    R7 --> AP3 --> C3
    R2 --> AP4 --> C4
    R6 --> AP4
    R7 --> AP4
    R4 --> AP4
```

## Como ler

- A **separação por regime** é uma exigência operacional declarada em D2 do assessment. Sem ela, não é possível responder a um pedido de Art. 18 LGPD ou Art. 17 GDPR de forma rastreável.
- **Embeddings = dado pseudonimizado por definição** quando derivados de dados pessoais. Apagar a fonte não apaga o embedding — exige rebuild ou purge seletivo do índice vetorial.
- **Logs de interação não são apêndice da aplicação.** Têm finalidade própria, exigem base legal própria e prazo de retenção próprio.
- **Reuso entre regimes é controlado.** Logs não viram dados de treino sem consentimento e revisão; corpus RAG não vira dataset de fine-tuning sem nova base legal.
- Referências cruzadas: ver `assessment/questionario-assessment.md` D2/D3/D4 e `referencias/crosswalk-normativo.md` (tema "Dados e qualidade").
