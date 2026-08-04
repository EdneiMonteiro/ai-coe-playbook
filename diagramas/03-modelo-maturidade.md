# Diagrama 3. Modelo de maturidade do CoE de IA

Este diagrama mostra a trajetória evolutiva de um CoE de IA em 4 níveis. Cada nível tem características distintas de operação, governança, plataforma e adoção. O assessment de maturidade (em `assessment/`) mede onde a organização está em cada uma das 10 dimensões; o modelo abaixo mostra o **perfil dominante** de cada nível e os principais sinais de transição.

## Evolução em 4 níveis

**[Descrição acessível]:** flowchart esquerda-direita com quatro estágios em cores progressivas: Nível 1 Reativo (vermelho), Nível 2 Executor (âmbar), Nível 3 Habilitador (azul), Nível 4 Transformador (verde). Cada transição é rotulada com a mudança requerida: "Definir mandato" (N1→N2), "Construir plataforma" (N2→N3), "Habilitar transformação" (N3→N4). A progressão de cor comunica intuitivamente direção de maturidade.

```mermaid
flowchart LR
    classDef n1 fill:#cf222e,stroke:#82071e,color:#fff
    classDef n2 fill:#9a6700,stroke:#633c01,color:#fff
    classDef n3 fill:#1f6feb,stroke:#0d419d,color:#fff
    classDef n4 fill:#1a7f37,stroke:#0a4d20,color:#fff

    N1["<b>Nível 1: Reativo</b><br/>Experimentos isolados<br/>Sem padrões nem governança<br/>Conhecimento concentrado<br/>Infra ad hoc"]:::n1

    N2["<b>Nível 2: Executor</b><br/>CoE centralizado<br/>Primeiros PoCs/MVPs<br/>Padrões iniciais<br/>Plataforma concentrada"]:::n2

    N3["<b>Nível 3: Habilitador</b><br/>Plataforma self-service governada<br/>Padrões publicados + guardrails<br/>Squads autônomos<br/>Comunidade ativa · FinOps"]:::n3

    N4["<b>Nível 4: Transformador</b><br/>CoE consultivo<br/>IA na estratégia de negócio<br/>Expertise distribuída<br/>Inovação contínua"]:::n4

    N1 -->|"<b>Definir mandato</b><br/>charter, sponsor,<br/>controle de risco básico"| N2
    N2 -->|"<b>Construir plataforma</b><br/>MVS, governança embutida,<br/>handoff, capacitação"| N3
    N3 -->|"<b>Habilitar transformação</b><br/>otimização contínua,<br/>cultura, inovação responsável"| N4
```

## Perfil dominante por dimensão

**[Descrição acessível]:** flowchart top-bottom com quatro subgrupos colados (N1g..N4g) representando perfis dominantes em 4 dimensões (Estratégia, Governança, Plataforma, LLMOps) em cada nível. As cores espelham as do diagrama anterior (vermelho/âmbar/azul/verde). Mostra que cada nível tem um perfil consistente em todas as dimensões dominantes.

```mermaid
flowchart TB
    classDef header fill:#24292f,stroke:#0d1117,color:#fff
    classDef dim fill:#f6f8fa,stroke:#57606a,color:#24292f
    classDef n1 fill:#cf222e,stroke:#82071e,color:#fff
    classDef n2 fill:#9a6700,stroke:#633c01,color:#fff
    classDef n3 fill:#1f6feb,stroke:#0d419d,color:#fff
    classDef n4 fill:#1a7f37,stroke:#0a4d20,color:#fff

    subgraph N1g["Nível 1: Reativo"]
        direction TB
        D1A["Estratégia<br/>ambígua"]:::n1
        D1B["Governança<br/>informal"]:::n1
        D1C["Plataforma<br/>ad hoc"]:::n1
        D1D["LLMOps<br/>manual"]:::n1
    end

    subgraph N2g["Nível 2: Executor"]
        direction TB
        D2A["Sponsor<br/>ativo"]:::n2
        D2B["Controles<br/>por projeto"]:::n2
        D2C["Ambientes<br/>controlados"]:::n2
        D2D["Evals<br/>iniciais"]:::n2
    end

    subgraph N3g["Nível 3: Habilitador"]
        direction TB
        D3A["Portfolio<br/>priorizado"]:::n3
        D3B["Gates<br/>padronizados"]:::n3
        D3C["Self-service<br/>governado"]:::n3
        D3D["Evals<br/>automatizados"]:::n3
    end

    subgraph N4g["Nível 4: Transformador"]
        direction TB
        D4A["IA na<br/>estratégia"]:::n4
        D4B["Risco<br/>preditivo"]:::n4
        D4C["Plataforma<br/>otimizada"]:::n4
        D4D["Aprendizado<br/>sistemático"]:::n4
    end

    N1g --> N2g --> N3g --> N4g
```

## Sinais de transição entre níveis

**[Descrição acessível]:** flowchart top-down listando sinais de transição em três blocos amarelos (N1→N2, N2→N3, N3→N4) com bullets concretos para cada salto. Um bloco vermelho destaca "Regressão típica": perdas que tipicamente fazem a organização recuar (padrões sem adoção, casos críticos sem classificação, produção sem IR, sponsor afastado). Setas pontilhadas indicam caminhos de regressão a partir de transições anteriores.

```mermaid
flowchart TD
    classDef trigger fill:#fff8c5,stroke:#9a6700,color:#24292f
    classDef risk fill:#cf222e,stroke:#82071e,color:#fff

    T12["<b>Sinais Nível 1 → 2</b><br/>• Charter aprovado e sponsor identificado<br/>• Primeiro caso de alto impacto entregue<br/>• Padrões mínimos publicados<br/>• Owner de risco formal nomeado"]:::trigger

    T23["<b>Sinais Nível 2 → 3</b><br/>• CoE vira gargalo de aprovação<br/>• Plataforma de autoatendimento operacional<br/>• Squads desenvolvem soluções sem depender do CoE<br/>• Handoff em ≥ 2 BUs com DoD cumprido<br/>• FinOps com showback/chargeback ativo"]:::trigger

    T34["<b>Sinais Nível 3 → 4</b><br/>• IA parte da estratégia de negócio<br/>• Comunidade de prática autossustentável<br/>• Métricas de valor realizadas e auditadas<br/>• CoE consultivo, não executor<br/>• Dívida de transição em redução contínua"]:::trigger

    REGR["<b>Regressão típica</b><br/>• Padrões sem adoção real (plataforma sem uso)<br/>• Casos críticos sem classificação formal<br/>• Produção sem incident response IA<br/>• Sponsor afastado, métricas paradas"]:::risk

    T12 --> T23 --> T34
    T34 -.->|"sem manutenção<br/>ou sponsor"| REGR
    T23 -.->|"sem ownership<br/>operacional"| REGR
```

## Como ler

- O assessment mede maturidade **por dimensão** (10) e calcula um **nível geral** (1–4). Veja `assessment/modelo-maturidade-coe-ia.md` para a definição completa.
- **Maturidade não é monotônica.** Sem manutenção, dimensões críticas (governança, plataforma, operação) podem regredir e disparar contenções automáticas (ver `assessment/criterios-pontuacao.md`).
- **Cada transição exige investimento diferente.** N1→N2 exige clareza estratégica; N2→N3 exige plataforma e disciplina de handoff; N3→N4 exige cultura, métricas de valor e maturidade de portfólio.
- O nível pleno **A** do assessment exige convergência das 10 dimensões; um CoE pode estar em N3 médio com algumas dimensões em N4 e outras em N2; o relatório auditável e o board pack devem refletir essa heterogeneidade.
