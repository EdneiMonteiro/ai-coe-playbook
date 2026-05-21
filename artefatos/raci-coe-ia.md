# RACI de referência para um CoE de IA

Este RACI é um ponto de partida. Em organizações reguladas, jurídico, risco, compliance, auditoria interna e DPO podem exigir papéis mais formais. Em empresas digitais, produto e plataforma tendem a assumir mais responsabilidade operacional.

| Atividade | CoE de IA | Plataforma/Cloud | Produto/Negócio | Dados | Segurança/Risco/Compliance | Executivo sponsor |
|---|---|---|---|---|---|---|
| Definir estratégia e mandato do CoE | R | C | C | C | C | A |
| Priorizar portfólio de casos de uso | R | C | R | C | C | A |
| Definir padrões de arquitetura e LLMOps | A/R | R | C | C | C | I |
| Publicar templates, blueprints e catálogo de serviços | A/R | R | C | C | C | I |
| Classificar risco de casos de uso | R | C | R | C | A/R | I |
| Aprovar casos de alto risco | C | C | R | C | A/R | A |
| Desenvolver PoC/MVP inicial | R | C | A/R | R | C | I |
| Executar evals e testes de regressão | A/R | C | R | C | C | I |
| Realizar AI red teaming | C | C | C | C | A/R | I |
| Operar produto em produção | C | C | A/R | R | C | I |
| Monitorar custo, qualidade, risco e adoção | A/R | R | R | C | C | I |
| Transferir solução para squad de produto | R | C | A/R | C | C | I |

Legenda: **R** = responsável pela execução; **A** = accountable pela decisão/resultado; **C** = consultado; **I** = informado.

Nota sobre accountability: o RACI mantém um único **A** por linha, exceto em aprovações de alto risco. Nesses casos, o **A/R** de Segurança/Risco/Compliance representa o dono técnico do veto e dos controles obrigatórios, enquanto o **A** do sponsor representa a decisão executiva de go/no-go e aceite de risco residual.

