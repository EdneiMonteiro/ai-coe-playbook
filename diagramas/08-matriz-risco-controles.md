# Diagrama 8. Matriz risco × controles

> **Verificação regulatória:** referências normativas deste documento conferidas em **maio de 2026**. Datas de vigência, prazos e limites citados exigem revalidação antes de uso em decisão formal. Ver [`referencias/auditoria-referencias.md`](../referencias/auditoria-referencias.md).

Este diagrama mostra como a **classificação de risco** (EU AI Act + classificação interna) é traduzida em **controles operacionais** específicos. Cada combinação tem um conjunto mínimo de controles e gates; quanto maior o risco, maior a exigência de evidência e accountability.

## Mapa EU AI Act → classificação interna

**[Descrição acessível]:** flowchart esquerda-direita mapeando cinco categorias do EU AI Act (Risco inaceitável; Alto risco do Anexo III; Risco limitado Art. 50; Risco mínimo; GPAI Arts. 51-55) (em âmbar) a cinco classificações internas (Proibido em cinza escuro; Crítico em vermelho escuro; Alto em vermelho; Médio em amarelo; Baixo em verde). Setas sólidas indicam mapeamento direto; setas pontilhadas mostram escalonamento condicional (ex.: alto impacto operacional eleva alto risco a crítico; GPAI com risco sistêmico vira crítico).

```mermaid
flowchart LR
    classDef eu fill:#9a6700,stroke:#633c01,color:#fff
    classDef int fill:#1f6feb,stroke:#0d419d,color:#fff
    classDef block fill:#24292f,stroke:#0d1117,color:#fff
    classDef critical fill:#82071e,stroke:#491111,color:#fff
    classDef high fill:#cf222e,stroke:#82071e,color:#fff
    classDef med fill:#fff8c5,stroke:#9a6700,color:#24292f
    classDef low fill:#1a7f37,stroke:#0a4d20,color:#fff

    EU1["<b>Risco inaceitável</b><br/>(EU AI Act Art. 5)<br/>pontuação social,<br/>manipulação subliminar"]:::eu
    EU2["<b>Alto risco</b><br/>(EU AI Act Anexo III)<br/>biometria, recrutamento,<br/>infraestrutura crítica,<br/>saúde, justiça"]:::eu
    EU3["<b>Risco limitado</b><br/>(EU AI Act Art. 50)<br/>chatbots, deepfakes,<br/>reconhecimento de emoção"]:::eu
    EU4["<b>Risco mínimo</b><br/>filtros de spam,<br/>IA em jogos"]:::eu
    EU5["<b>GPAI</b><br/>(Arts. 51–55)<br/>modelo de uso geral<br/>integrado ou usado"]:::eu

    INT1["<b>Proibido</b>"]:::block
    INT2["<b>Crítico</b>"]:::critical
    INT3["<b>Alto</b>"]:::high
    INT4["<b>Médio</b>"]:::med
    INT5["<b>Baixo</b>"]:::low

    EU1 --> INT1
    EU2 --> INT2
    EU2 -.->|"alto impacto<br/>operacional"| INT3
    EU3 --> INT4
    EU3 -.->|"exposição<br/>externa"| INT3
    EU4 --> INT5
    EU5 --> INT3
    EU5 -.->|"GPAI<br/>risco sistêmico"| INT2
```

## Controles obrigatórios por classificação interna

**[Descrição acessível]:** flowchart top-bottom com cinco subgrupos empilhados: Baixo (verde), Médio (amarelo), Alto (vermelho), Crítico (vermelho escuro), Proibido (cinza escuro). Cada nível adiciona controles aos níveis anteriores (cumulativo): Baixo tem owner, classificação, avaliação básica, aprovação produto+CoE, SLA 5d; Médio adiciona DPIA, transparência, logs, +dados/segurança, SLA 10d; Alto adiciona red teaming, supervisão humana, fallback, +sponsor, SLA 15d; Crítico adiciona comitê de risco, parecer jurídico, FRIA, SLA convocação 5d; Proibido bloqueia decisão imediata D+0 com parecer jurídico do bloqueio. Setas verticais mostram ordem crescente de risco.

```mermaid
flowchart TB
    classDef low fill:#1a7f37,stroke:#0a4d20,color:#fff
    classDef med fill:#fff8c5,stroke:#9a6700,color:#24292f
    classDef high fill:#cf222e,stroke:#82071e,color:#fff
    classDef critical fill:#82071e,stroke:#491111,color:#fff
    classDef blocked fill:#24292f,stroke:#0d1117,color:#fff

    subgraph BAIXO["Baixo"]
        direction TB
        B1["Owner técnico e de negócio"]:::low
        B2["Classificação de risco formal"]:::low
        B3["Avaliação básica de dados"]:::low
        B4["Aprovação: produto + CoE"]:::low
        B5["SLA: ≤ 5 dias úteis"]:::low
    end

    subgraph MEDIO["Médio"]
        direction TB
        M1["+ Avaliação de viés<br/>+ DPIA quando aplicável"]:::med
        M2["+ Transparência aos<br/>usuários impactados"]:::med
        M3["+ Logs de auditoria"]:::med
        M4["+ Aprovação: + dados<br/>e segurança"]:::med
        M5["+ SLA: ≤ 10 dias úteis"]:::med
    end

    subgraph ALTO["Alto"]
        direction TB
        A1["+ AI red teaming<br/>+ monitoramento reforçado"]:::high
        A2["+ Supervisão humana<br/>no fluxo"]:::high
        A3["+ Fallback/rollback<br/>testado"]:::high
        A4["+ Aprovação: + segurança/<br/>risco/compliance + sponsor"]:::high
        A5["+ SLA: ≤ 15 dias úteis"]:::high
    end

    subgraph CRITICO["Crítico"]
        direction TB
        C1["+ Comitê de risco<br/>antes de qualquer produção"]:::critical
        C2["+ Parecer jurídico<br/>formal anexado"]:::critical
        C3["+ FRIA quando aplicável<br/>(EU AI Act Art. 27)"]:::critical
        C4["+ Aprovação: + jurídico<br/>+ sponsor executivo"]:::critical
        C5["+ Convocar comitê<br/>em ≤ 5 dias úteis"]:::critical
    end

    subgraph PROIBIDO["Proibido"]
        direction TB
        P1["Bloqueado<br/>(vedado por lei,<br/>política ou risco<br/>inaceitável)"]:::blocked
        P2["Decisão imediata (D+0)"]:::blocked
        P3["Parecer jurídico<br/>documentando o<br/>motivo do bloqueio"]:::blocked
    end

    BAIXO --> MEDIO --> ALTO --> CRITICO --> PROIBIDO
```

## Gates go/no-go aplicáveis

**[Descrição acessível]:** flowchart top-down mostrando entrada (caso de uso em MVP/produção/expansão) passando por 8 gates sequenciais (G1 classificação; G2 dados/privacidade; G3 FRIA/DPIA; G4 red teaming; G5 IR; G6 evals+regressão; G7 fallback/rollback/kill switch; G8 controles de agentes). Cada gate em amarelo bifurca: "sim ou n/a" segue para o próximo gate; "não" / "aplicável e ausente" direciona para "Veto Operacional Aberto" em vermelho. Sucesso em todos os gates leva a "Aprovado" em verde, com possível ramo para "Aprovado com Restrições" via setas pontilhadas.

```mermaid
flowchart TD
    classDef gate fill:#fff8c5,stroke:#9a6700,color:#24292f
    classDef low fill:#1a7f37,stroke:#0a4d20,color:#fff
    classDef high fill:#cf222e,stroke:#82071e,color:#fff

    GATE1{"Classificação<br/>de risco<br/>formal?"}:::gate
    GATE2{"Avaliação de<br/>dados e<br/>privacidade?"}:::gate
    GATE3{"FRIA/DPIA<br/>quando<br/>aplicável?"}:::gate
    GATE4{"AI red teaming<br/>quando<br/>aplicável?"}:::gate
    GATE5{"Incident response<br/>IA configurado?"}:::gate
    GATE6{"Evals + regressão<br/>quando<br/>aplicável?"}:::gate
    GATE7{"Fallback /<br/>rollback /<br/>kill switch?"}:::gate
    GATE8{"Controles<br/>de agentes<br/>(allowlist, HITL,<br/>kill switch por<br/>agente)?"}:::gate

    ENTRADA[/"Caso de uso<br/>em MVP,<br/>produção ou<br/>expansão"/]
    APROVADO(["<b>Aprovado</b><br/>(gates atendidos<br/>+ risco residual<br/>aceito)"]):::low
    RESTRICOES(["<b>Aprovado com<br/>restrições</b><br/>(prazo, escopo,<br/>controles<br/>compensatórios)"]):::low
    VETO[/"<b>Veto operacional<br/>aberto</b><br/>(bloqueio até<br/>remediação)"/]:::high

    ENTRADA --> GATE1
    GATE1 -->|sim| GATE2
    GATE1 -->|não| VETO
    GATE2 -->|sim| GATE3
    GATE2 -->|não| VETO
    GATE3 -->|sim ou n/a| GATE4
    GATE3 -->|aplicável e ausente| VETO
    GATE4 -->|sim ou n/a| GATE5
    GATE4 -->|aplicável e ausente<br/>sem waiver| VETO
    GATE5 -->|sim| GATE6
    GATE5 -->|não| VETO
    GATE6 -->|sim ou n/a| GATE7
    GATE6 -->|aplicável e ausente| VETO
    GATE7 -->|sim| GATE8
    GATE7 -->|não| VETO
    GATE8 -->|sim ou n/a| APROVADO
    GATE8 -->|aplicável e ausente| VETO
    APROVADO -.->|"se houver restrições<br/>condicionais"| RESTRICOES
```

## Como ler

- **Risco é cumulativo.** Cada nível adiciona controles aos níveis anteriores. Um caso "Alto" exige tudo do "Baixo" + tudo do "Médio" + os controles próprios.
- **Maturidade ≠ autorização operacional.** A organização pode ser madura (assessment N3 ou N4) e ainda assim ter casos vetados; gates são por caso, não por organização (ver `assessment/criterios-pontuacao.md`).
- **GPAI complica.** Um modelo GPAI pode aparecer em casos de baixo risco e ainda assim disparar obrigações específicas (transparência, GPAI Arts. 51–55). Avaliar separadamente.
- **Veto operacional é a saída padrão quando algum gate aplicável fica em aberto.** Não há "aprovado com pendência crítica": ou remedia, ou veta.
- Referências cruzadas:
  - `artefatos/template-avaliacao-risco-ia.md` (ficha + matriz operacional + DoD)
  - `assessment/criterios-pontuacao.md` (gates operacionais + regras de contenção)
  - `referencias/crosswalk-normativo.md` (EU AI Act, GPAI, FRIA Art. 27)
