# RACI de referência para um CoE de IA

Este RACI é um ponto de partida. Em organizações reguladas, jurídico, risco, compliance, auditoria interna e DPO podem exigir papéis mais formais. Em empresas digitais, produto e plataforma tendem a assumir mais responsabilidade operacional.

| Atividade | CoE de IA | Plataforma/Cloud | Produto/Negócio | Dados | Segurança/Risco/Compliance | Executivo sponsor |
|---|---|---|---|---|---|---|
| Definir estratégia e mandato do CoE | R | C | C | C | C | A |
| Priorizar portfólio de casos de uso | R | C | R | C | C | A |
| Definir padrões de arquitetura e LLMOps | A/R | R | C | C | C | I |
| Publicar templates, blueprints e catálogo de serviços | A/R | R | C | C | C | I |
| Classificar risco de casos de uso | R | C | R | C | A/R | I |
| Aprovar casos de alto risco | C | C | A/R | C | A/R | A |
| Desenvolver PoC/MVP inicial | R | C | A/R | R | C | I |
| Executar evals e testes de regressão | A/R | C | R | C | C | I |
| Realizar AI red teaming | C | C | C | C | A/R | I |
| Operar produto em produção | C | C | A/R | R | C | I |
| Monitorar custo, qualidade, risco e adoção | A/R | R | R | C | C | I |
| Capacitar comunidade / AI literacy interna | A/R | C | R | C | C | I |
| Comunicar mudanças de padrão de IA à comunidade técnica | A/R | C | I | I | I | I |
| Transferir solução para squad de produto | R | C | A/R | C | C | I |
| Avaliar, contratar e monitorar fornecedor de IA (modelo/plataforma) | R | R | C | C | C | A |

Legenda: **R** = responsável pela execução; **A** = accountable pela decisão/resultado; **C** = consultado; **I** = informado.

Nota sobre accountability: o RACI mantém um único **A** por linha, exceto em aprovações de alto risco. Nesses casos, o **A/R** de Segurança/Risco/Compliance representa o dono técnico do veto e dos controles obrigatórios, o **A/R** de Produto/Negócio representa o dono do produto cujo risco material é assumido, e o **A** do sponsor representa a decisão executiva de go/no-go e aceite de risco residual. **Em adaptação para organização específica, o Executivo Sponsor deve ser nomeado individualmente (nome + cargo), não apenas como papel genérico, e o instrumento de decisão deve registrar quem ocupava o papel na data da aprovação.**

**Sequência de aprovação para alto risco:** (i) Segurança/Risco/Compliance emite parecer técnico em ≤ 4 dias úteis e (iii) Produto/Negócio emite aceite formal em ≤ 3 dias úteis, **em paralelo** → (ii) Sponsor emite go/no-go executivo em ≤ 3 dias úteis após receber ambos. SLA total efetivo ≤ 10 dias úteis (compatível com a Matriz operacional do template, Alto ≤ 15 dias úteis, com buffer de 5 dias úteis). Notificação automática ao Sponsor se qualquer etapa atrasar.

**Nota sobre desacoplamento de papéis em ambiente regulado:** em organizações sob LGPD com decisões automatizadas (Art. 20) ou sob GDPR (Art. 37–39), o **DPO** deve ter coluna própria no RACI, independente de "Segurança/Risco/Compliance", para preservar autonomia funcional. Recomendação aplicável também a "Jurídico", "Auditoria Interna" e "Procurement/Vendor Management" em organizações reguladas; adapte conforme estrutura. Quando a organização possui função formal de Procurement/Vendor Management, considere adicionar coluna específica para refletir o ownership de contratos e gestão de fornecedor.

**Nota sobre AI literacy:** em organizações sob escopo do EU AI Act (deployer ou provider), AI literacy é obrigação documentada (Art. 4, vigente desde 02/02/2025); fora desse escopo, é boa prática operacional. A linha "Capacitar comunidade / AI literacy interna" reflete essa responsabilidade no RACI.

**DoD de transferência (linha "Transferir solução para squad de produto"):** transferência é considerada concluída quando: (i) documentação operacional completa (runbook, evals, métricas de monitoramento) está no repositório do squad receptor; (ii) sessão formal de knowledge transfer foi realizada com presença confirmada do tech lead e do PO do squad receptor; (iii) o squad receptor é o **R operacional** dos próximos 30 dias com CoE como **C** (não como R sombra); (iv) acordo formal de quem responde por incidentes em produção está registrado.
