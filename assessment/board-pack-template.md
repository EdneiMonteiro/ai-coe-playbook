# Board pack do assessment de maturidade do CoE de IA

> Destilação executiva de uma página. Use junto com o relatório auditável completo em [`relatorio-template.md`](relatorio-template.md).

## 1. Mensagem única

> [Uma frase de até 30 palavras: nível atual, risco principal e decisão pedida.]

## 2. Decisão pedida

| Decisão | Prazo | Owner executivo |
|---|---|---|
| [aprovar investimento / pausar expansão / aceitar risco residual / bloquear caso / priorizar remediação] | [data] | [nome/cargo] |

## 3. Recomendação

**Recomendação:** [opção recomendada]

**Racional:** [2–3 frases conectando maturidade, risco, custo de inação e valor esperado]

**Racional financeiro mínimo:** [custo unitário atual, custo unitário alvo, variação vs baseline, volume esperado, custo de evals/regressão, impacto de SaaS/licenças de IA e impacto financeiro do custo de inação]

**Síntese financeira (uma frase):** investimento de **R$ [X]** retorna **[benefício/eficiência Y]** em **[Z meses]**, com risco regulatório residual **[W]** e custo de inação estimado em **[valor/faixa]**.

| Métrica financeira | Atual | Alvo | Variação vs baseline | Observações |
|---|---:|---:|---:|---|
| Custo unitário principal | [ex.: R$/resolução] | [valor] | [%] | [obs] |
| Volume esperado | [n/mês] | [n/mês] | [%] | [obs] |
| Custo mensal de inferência/uso | [valor] | [valor] | [%] | [obs] |
| Custo mensal de evals/regressão | [valor] | [valor] | [%] | [frequência e risco coberto] |
| SaaS/licenças de IA | [valor] | [valor] | [%] | [utilização ativa, reclaim e showback por assento] |
| Custo de inação estimado | [valor/faixa] | [n/a] | [n/a] | [risco financeiro, operacional ou regulatório] |

## 4. Opções executivas

| Opção | O que significa | Benefício | Risco/trade-off | Investimento/capacidade |
|---|---|---|---|---|
| Status quo | [continuar como está] | [benefício] | [risco] | [custo/capacidade] |
| Contenção | [pausar, limitar ou bloquear expansão até remediação] | [benefício] | [risco] | [custo/capacidade] |
| Investimento recomendado | [financiar plataforma, governança, equipe, controles, evals etc.] | [benefício] | [risco] | [custo/capacidade] |

## 5. Resultado do assessment

| Item | Resultado |
|---|---|
| Nível geral bruto | [Nível / pontuação] |
| Nível final após contenções | [Nível / pontuação] |
| Vetos operacionais abertos | [número e resumo] |
| Dimensões mais fortes | [lista] |
| Dimensões mais frágeis | [lista] |
| Confiança da avaliação | [alta/média/baixa/inconclusiva] |

## 6. Consequência das contenções

| Contenção/veto | Consequência de negócio | Consequência regulatória/risco | Decisão necessária |
|---|---|---|---|
| [veto] | [risco para cliente, receita, operação, prazo] | [risco regulatório/compliance] | [decisão] |

## 7. Custo de inação

Quando o custo de inação não puder ser estimado diretamente, usar proxies explícitos: (a) custo de oportunidade do projeto/iniciativa deslocado pelo retrabalho, (b) multa regulatória estimada por exposição (com referência ao artigo aplicável); **quando houver exposição LGPD, dimensionar pelo limite do Art. 52 (até R$ 50 milhões por infração) e pelo regime de urgência aplicável**; sob GDPR, usar o limite de 4% do faturamento global; (c) churn/perda estimada da unidade de negócio impactada, (d) custo de remediação caso veto operacional persista. Não deixar o campo em branco; declarar o proxy usado.

| Horizonte | Consequência provável se nada mudar | Proxy usado |
|---|---|---|
| 30 dias | [consequência] | [oportunidade / multa / churn / remediação / direto] |
| 90 dias | [consequência] | [oportunidade / multa / churn / remediação / direto] |
| 180 dias | [consequência] | [oportunidade / multa / churn / remediação / direto] |

## 8. Próximos 30 dias

| Ação | Owner operacional | Accountable executivo | Bloqueio a remover | Resultado esperado |
|---|---|---|---|---|
| [ação 1] | [owner] | [executivo] | [bloqueio] | [resultado] |
| [ação 2] | [owner] | [executivo] | [bloqueio] | [resultado] |
| [ação 3] | [owner] | [executivo] | [bloqueio] | [resultado] |
