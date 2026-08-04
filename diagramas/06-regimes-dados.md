# Diagrama 6. Regimes de dados (treino × inferência/RAG × logs)

> **Verificação regulatória:** referências normativas deste documento conferidas em **maio de 2026**. Datas de vigência, prazos e limites citados exigem revalidação antes de uso em decisão formal. Ver [`referencias/auditoria-referencias.md`](../referencias/auditoria-referencias.md).

Este diagrama mostra a separação obrigatória entre **três regimes de dados** em sistemas de IA. Cada regime tem finalidade, base legal, retenção, controles e ciclo de vida próprios. Tratar tudo como "dados de IA" mistura responsabilidades e impede auditoria de privacidade; daí a inclusão como gate operacional em D2 do assessment.

## Os três regimes

**[Descrição acessível]:** flowchart top-bottom com quatro subgrupos coloridos representando regimes distintos de dados: Regime 1 Treino/Fine-tuning (azul), Regime 2 Inferência/RAG (verde), Regime 3 Logs de Interação (âmbar) e Regime 4 Feedback/Preferência RLHF/RLAIF (roxo). Cada regime declara finalidade, base legal, conteúdo, retenção e direito de apagamento. Setas pontilhadas em itálico mostram restrições de fluxo: TRAIN nunca compartilha com INFER, INFER nunca compartilha com LOG, LOG nunca alimenta TRAIN sem consentimento explícito, INFER vira FEEDBACK só com opt-in, FEEDBACK alimenta retreino do reward model com base legal própria.

```mermaid
flowchart TB
    classDef train fill:#1f6feb,stroke:#0d419d,color:#fff
    classDef infer fill:#1a7f37,stroke:#0a4d20,color:#fff
    classDef log fill:#9a6700,stroke:#633c01,color:#fff
    classDef feedback fill:#8250df,stroke:#3e1f79,color:#fff
    classDef control fill:#cf222e,stroke:#82071e,color:#fff

    subgraph TRAIN["Regime 1: Treino / Fine-tuning"]
        direction TB
        T1["<b>Finalidade:</b> ajustar modelo<br/><b>Base legal:</b> revisão jurídica<br/>específica para uso de dados<br/>pessoais em treino"]:::train
        T2["<b>Conteúdo:</b> datasets curados,<br/>dados sintéticos com proveniência,<br/>preferências para RLHF"]:::train
        T3["<b>Retenção:</b> longa (versionada<br/>com o modelo)<br/><b>Direito de apagamento:</b> exige<br/>retrain ou unlearning"]:::train
    end

    subgraph INFER["Regime 2: Inferência / RAG"]
        direction TB
        I1["<b>Finalidade:</b> responder usuário<br/>em tempo de execução<br/><b>Base legal:</b> definida por<br/>aplicação (contrato, legítimo<br/>interesse, consentimento)"]:::infer
        I2["<b>Conteúdo:</b> corpus RAG,<br/>embeddings, índice vetorial,<br/>políticas de recuperação"]:::infer
        I3["<b>Retenção:</b> conforme política<br/>do produto<br/><b>Direito de apagamento:</b> rebuild<br/>de embeddings ou purge<br/>seletivo"]:::infer
    end

    subgraph LOG["Regime 3: Logs de interação"]
        direction TB
        L1["<b>Finalidade:</b> auditoria, evals,<br/>incident response<br/><b>Base legal:</b> exige declaração<br/>específica; não inferida do<br/>regime 2"]:::log
        L2["<b>Conteúdo:</b> prompts, respostas,<br/>tool calls, identificadores<br/>de sessão, metadados de eval"]:::log
        L3["<b>Retenção:</b> mínima necessária<br/>(curta por padrão)<br/><b>Direito de apagamento:</b> purge<br/>com tombstone para auditoria"]:::log
    end

    subgraph FEEDBACK["Regime 4: Dados de feedback / preferência (RLHF/RLAIF)"]
        direction TB
        F1["<b>Finalidade:</b> alinhar modelo via<br/>preferência humana ou de IA<br/>(RLHF/RLAIF, DPO)<br/><b>Base legal:</b> consentimento<br/>específico para nova finalidade<br/>(LGPD Art. 7º, I; GDPR Art. 6(1)(a))"]:::feedback
        F2["<b>Conteúdo:</b> pares de preferência,<br/>thumbs up/down, comparações,<br/>anotações humanas, sinais<br/>implícitos (reuso, edição)"]:::feedback
        F3["<b>Retenção:</b> versionada com o<br/>modelo de recompensa<br/><b>Direito de apagamento:</b> exclusão<br/>do par + retreino da policy<br/>quando aplicável"]:::feedback
        F4["<b>Controles:</b> opt-in explícito,<br/>opt-out reversível, separação<br/>do regime de logs (3),<br/>auditoria de viés do anotador"]:::feedback
    end

    TRAIN -.->|*nunca compartilha*<br/>*controle de acesso*| INFER
    INFER -.->|*nunca compartilha*<br/>*controle de acesso*| LOG
    LOG -.->|*nunca alimenta*<br/>*treino sem consentimento*<br/>*explícito*| TRAIN
    INFER -.->|*vira feedback apenas*<br/>*com opt-in explícito*| FEEDBACK
    FEEDBACK -.->|*alimenta retreino*<br/>*do reward model*<br/>*com base legal própria*| TRAIN
```

## Controles obrigatórios por regime

**[Descrição acessível]:** flowchart esquerda-direita com três subgrupos paralelos (Controles Treino, Inferência/RAG, Logs) listando 4 controles obrigatórios por regime. Os subgrupos não se conectam (operador `~~~`), indicando que os controles são independentes por regime e não devem ser misturados.

```mermaid
flowchart LR
    classDef tr fill:#1f6feb,stroke:#0d419d,color:#fff
    classDef inf fill:#1a7f37,stroke:#0a4d20,color:#fff
    classDef lg fill:#9a6700,stroke:#633c01,color:#fff
    classDef fb fill:#8250df,stroke:#3e1f79,color:#fff

    subgraph TR_CTL["Controles: Treino"]
        TC1["Base legal específica<br/>para dados pessoais"]:::tr
        TC2["Proveniência dos dados<br/>(sintéticos declarados)"]:::tr
        TC3["Aprovação do data owner"]:::tr
        TC4["Teste de memorização<br/>e reidentificação"]:::tr
    end

    subgraph IN_CTL["Controles: Inferência/RAG"]
        IC1["Status de anonimização<br/>declarado (anonimizado /<br/>pseudonimizado / nenhum)"]:::inf
        IC2["Embeddings tratados como<br/>dados pseudonimizados<br/>por definição"]:::inf
        IC3["Política de recuperação<br/>versionada"]:::inf
        IC4["Rebuild de embeddings<br/>quando fonte muda<br/>ou é apagada"]:::inf
    end

    subgraph LG_CTL["Controles: Logs"]
        LC1["Política de retenção<br/>declarada"]:::lg
        LC2["Mascaramento/redacao<br/>de PII"]:::lg
        LC3["Purge automático<br/>+ tombstone para<br/>auditoria"]:::lg
        LC4["Acesso controlado<br/>(quem lê logs?)"]:::lg
    end

    subgraph FB_CTL["Controles: Feedback/RLHF"]
        FC1["Opt-in explícito<br/>antes da coleta"]:::fb
        FC2["Opt-out reversível<br/>(LGPD Art. 7º I;<br/>GDPR Art. 7(3))"]:::fb
        FC3["Separação de armazenamento<br/>do Regime 3 (logs)"]:::fb
        FC4["Auditoria de viés<br/>do anotador"]:::fb
    end

    TR_CTL ~~~ IN_CTL ~~~ LG_CTL ~~~ FB_CTL
```

## Mapa de risco regulatório

**[Descrição acessível]:** flowchart top-down ligando sete dispositivos regulatórios (LGPD Arts. 6, 11, 18, 33; GDPR Arts. 17, 9; EU AI Act Art. 10) (em amarelo) a quatro anti-patterns de risco (PII em RAG sem direito de apagamento; logs com PII sem retenção; sintéticos em eval sem teste de reidentificação; treino com dados pessoais sem base legal) (em vermelho) e finalmente a quatro controles obrigatórios (rebuild de embeddings; mascaramento+retenção+tombstone; proveniência declarada; revisão jurídica) (em verde). As ligações mostram qual dispositivo dispara qual risco e qual controle remedia.

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
    R8["LGPD Art. 7<br/>(bases legais<br/>para tratamento)"]:::reg

    AP1["PII em corpus RAG<br/>sem direito de<br/>apagamento implementado"]:::risk
    AP2["Logs com PII<br/>sem classificação<br/>nem retenção"]:::risk
    AP3["Sintéticos usados em eval<br/>sem teste de<br/>reidentificação"]:::risk
    AP4["Treino com dados<br/>pessoais sem base<br/>legal específica"]:::risk
    AP5["Feedback capturado<br/>sem base legal<br/>explícita"]:::risk

    C1["Rebuild de embeddings<br/>+ purge seletivo"]:::ctl
    C2["Mascaramento + retenção<br/>+ tombstone"]:::ctl
    C3["Proveniência declarada<br/>+ aprovação owner"]:::ctl
    C4["Revisão jurídica antes<br/>do treino"]:::ctl
    C5["Revisão de base legal<br/>antes de cada regime"]:::ctl

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
    R8 --> AP4
    R8 --> AP5 --> C5
```

## Como ler

- A **separação por regime** é uma exigência operacional declarada em D2 do assessment. Sem ela, não é possível responder a um pedido de Art. 18 LGPD ou Art. 17 GDPR de forma rastreável.
- **Embeddings = dado pseudonimizado por definição** quando derivados de dados pessoais. Apagar a fonte não apaga o embedding: exige rebuild ou purge seletivo do índice vetorial.
- **Logs de interação não são apêndice da aplicação.** Têm finalidade própria, exigem base legal própria e prazo de retenção próprio.
- **Reuso entre regimes é controlado.** Logs não viram dados de treino sem consentimento e revisão; corpus RAG não vira dataset de fine-tuning sem nova base legal.
- Referências cruzadas: ver `assessment/questionario-assessment.md` D2/D3/D4 e `referencias/crosswalk-normativo.md` (tema "Dados e qualidade").
