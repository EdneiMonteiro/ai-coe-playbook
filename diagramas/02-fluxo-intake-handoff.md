# Diagrama 2 — Fluxo de intake a handoff com gates

Este diagrama mostra o ciclo de vida operacional de um caso de uso de IA dentro do CoE: da entrada no funil de intake até o handoff para o squad de produto. Os **gates operacionais** (classificação de risco, FRIA/DPIA quando aplicável, red team, incident response, evals, fallback) determinam se um caso pode avançar entre estágios. Esses gates protegem produção, dados, clientes e conformidade.

## Funil operacional

**[Descrição acessível]:** flowchart top-bottom de funil go/no-go com 4 estágios principais (Intake → PoC → MVP → Produção → Handoff completo) em azul. Entre estágios há quatro gates em amarelo (G1 classificação de risco; G2 FRIA/DPIA; G3 red team/evals/IR; G4 handoff DoD). De cada gate saem dois caminhos vermelhos: "veto aberto" e (quando aplicável) "risco inaceitável → Bloqueado". O fluxo do veto retorna ao G1 após remediação; o handoff completo é estado terminal em roxo.

```mermaid
flowchart TB
    classDef stage fill:#1f6feb,stroke:#0d419d,color:#fff
    classDef gate fill:#fff8c5,stroke:#9a6700,color:#24292f
    classDef decision fill:#1a7f37,stroke:#0a4d20,color:#fff
    classDef veto fill:#cf222e,stroke:#82071e,color:#fff
    classDef done fill:#8250df,stroke:#3e1f79,color:#fff

    INTAKE["<b>Intake</b><br/>formulário, owner de negócio,<br/>owner técnico, hipótese de valor"]:::stage

    G1{"Gate 1 —<br/>Classificação de risco<br/>+ avaliação de dados"}:::gate

    POC["<b>PoC</b><br/>experimento controlado<br/>sem produção real"]:::stage

    G2{"Gate 2 — Pré-MVP<br/>FRIA/DPIA aplicável?<br/>Base legal? Owner de risco?"}:::gate

    MVP["<b>MVP</b><br/>piloto limitado<br/>usuários controlados<br/>critérios de sucesso"]:::stage

    G3{"Gate 3 — Pré-produção<br/>Red team? Evals com<br/>thresholds? Incident response?<br/>Fallback/kill switch?"}:::gate

    PROD["<b>Produção</b><br/>tráfego real<br/>monitoramento contínuo<br/>SLO + on-call"]:::stage

    G4{"Gate 4 — Handoff<br/>DoD: runbook, evals,<br/>métricas, knowledge transfer,<br/>owner em squad por 30 dias"}:::gate

    HANDOFF(["<b>Handoff completo</b><br/>squad é R operacional<br/>CoE atua como C"]):::done

    VETO[/"<b>Veto operacional</b><br/>aberto até remediação"/]:::veto

    BLOCK[/"<b>Bloqueado</b><br/>vedado por lei/política/<br/>risco inaceitável"/]:::veto

    INTAKE --> G1
    G1 -->|aprovado / aprovado c/ restrições| POC
    G1 -->|veto aberto| VETO
    G1 -->|risco inaceitável| BLOCK

    POC --> G2
    G2 -->|aprovado| MVP
    G2 -->|veto aberto| VETO
    G2 -->|kill criteria atingido| BLOCK

    MVP --> G3
    G3 -->|aprovado| PROD
    G3 -->|veto aberto| VETO

    PROD --> G4
    G4 -->|DoD atingido| HANDOFF
    G4 -.->|DoD incompleto<br/>volta ao squad CoE| PROD

    VETO -.->|remediação| G1
```

## Status possíveis em cada gate

**[Descrição acessível]:** state diagram com estado inicial "Em Avaliação" e quatro estados de saída — Aprovado (terminal), Aprovado Com Restrições, Veto Operacional e Bloqueado (terminal). Restrições e vetos voltam ao estado de avaliação após revisão/remediação. Mostra que o gate é dinâmico: maturidade da organização não imuniza casos individuais.

```mermaid
stateDiagram-v2
    [*] --> EmAvaliação
    EmAvaliação --> Aprovado: gates atendidos<br/>+ risco residual aceito
    EmAvaliação --> AprovadoComRestrições: avança com<br/>prazo/escopo/controles<br/>compensatórios
    EmAvaliação --> VetoOperacional: produção/expansão<br/>bloqueada até remediação
    EmAvaliação --> Bloqueado: vedado por lei,<br/>política ou risco inaceitável

    AprovadoComRestrições --> EmAvaliação: revisão na<br/>data prevista
    VetoOperacional --> EmAvaliação: remediação<br/>concluída

    Aprovado --> [*]
    Bloqueado --> [*]
```

## Como ler

- Cada **gate** é uma decisão go/no-go que separa maturidade de capacidade organizacional da autorização operacional do caso. Uma organização madura pode, ainda assim, **vetar** um caso específico.
- Gates 2 e 3 ativam as **regras de contenção** documentadas em `assessment/criterios-pontuacao.md`: FRIA/DPIA, AI red teaming, incident response IA, fallback/rollback/kill switch, evals com thresholds.
- O **handoff** é o critério prático de **build-to-transfer**: o squad receptor é o R operacional, com o CoE atuando como consultor. Sem DoD atingido, o caso volta para iteração (ver `artefatos/raci-coe-ia.md` — DoD de transferência).
- O fluxo é cíclico: **expansão** de um caso existente (novos países, dados, ferramentas, autonomia) é tratada como nova decisão go/no-go.
