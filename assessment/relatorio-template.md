# Relatório auditável de assessment de maturidade do CoE de IA

> Template para consolidar a trilha completa do assessment. Para decisão executiva de board/C-level, produza também o [`board-pack-template.md`](board-pack-template.md), que resume este relatório em uma página.

## 1. Identificação e escopo

| Campo | Valor |
|---|---|
| Organização/unidade avaliada | [nome] |
| Data | [data] |
| Sponsor executivo | [nome/cargo] |
| Facilitador do assessment | [nome/cargo] |
| Avaliadores | [nomes/cargos] |
| Modo de aplicação | [diagnóstico interno / auditoria-investimento] |
| Escopo organizacional | [áreas, produtos, países, unidades] |
| Escopo técnico | [GenAI, RAG, agentes, ML clássico, copilots, automações decisórias] |
| Amostra avaliada | [número e tipo de soluções/casos] |
| Limites declarados | [fora de escopo, evidências ausentes, restrições] |

## 2. Taxonomia operacional aplicada

| Categoria | Definição usada | Casos enquadrados |
|---|---|---|
| PoC | [definição aplicada] | [casos] |
| MVP | [definição aplicada] | [casos] |
| Produção | [definição aplicada] | [casos] |
| Produção crítica | [definição aplicada] | [casos] |
| Exposição externa | [definição aplicada] | [casos] |
| Alto risco | [definição aplicada] | [casos] |
| Expansão | [definição aplicada] | [casos] |

## 3. Resultado consolidado

| Métrica | Resultado |
|---|---|
| Pontuação geral bruta | [0,00–4,00] |
| Nível bruto | [Nível 1/2/3/4] |
| Contenções aplicadas | [sim/não — quais] |
| Nível final após contenções | [Nível 1/2/3/4] |
| Vetos operacionais abertos | [número] |
| Confiança geral | [alta/média/baixa/inconclusiva] |
| Decisão operacional agregada | [aprovado / aprovado com restrições / veto operacional aberto / bloqueado] |

## 4. Resultado por dimensão

| Dimensão | Pontuação bruta | Ajuste por confiança | Pontuação final | Nível | Confiança | Comentário executivo |
|---|---:|---:|---:|---|---|---|
| Estratégia e mandato | [x,x] | [x,x] | [x,x] | [N] | [alta/média/baixa] | [comentário] |
| Modelo operacional | [x,x] | [x,x] | [x,x] | [N] | [alta/média/baixa] | [comentário] |
| Governança e risco | [x,x] | [x,x] | [x,x] | [N] | [alta/média/baixa] | [comentário] |
| Plataforma e arquitetura | [x,x] | [x,x] | [x,x] | [N] | [alta/média/baixa] | [comentário] |
| Dados e conhecimento | [x,x] | [x,x] | [x,x] | [N] | [alta/média/baixa] | [comentário] |
| LLMOps/MLOps e evals | [x,x] | [x,x] | [x,x] | [N] | [alta/média/baixa] | [comentário] |
| Portfólio e valor | [x,x] | [x,x] | [x,x] | [N] | [alta/média/baixa] | [comentário] |
| Capacitação e comunidade | [x,x] | [x,x] | [x,x] | [N] | [alta/média/baixa] | [comentário] |
| FinOps e sustentabilidade | [x,x] | [x,x] | [x,x] | [N] | [alta/média/baixa] | [comentário] |
| Operação e melhoria contínua | [x,x] | [x,x] | [x,x] | [N] | [alta/média/baixa] | [comentário] |

## 5. Gates go/no-go e vetos operacionais

| Caso de uso | Contexto | Gate violado | Evidência | Consequência | Owner | Prazo de remediação | Status |
|---|---|---|---|---|---|---|---|
| [caso] | [produção/crítica/externa/etc.] | [gate] | [evidência] | [bloqueio/restrição] | [owner] | [prazo] | [aberto/fechado] |

### Tradução dos vetos para negócio

| Veto | Risco de negócio | Risco regulatório/compliance | Risco operacional | Impacto em receita/custo/cliente | Decisão necessária |
|---|---|---|---|---|---|
| [veto] | [risco] | [risco] | [risco] | [impacto] | [decisão] |

## 6. Regras de contenção aplicadas

| Regra | Aplicável? | Evidência | Efeito no nível geral | Observações |
|---|---|---|---|---|
| Governança e risco < 2,0 | [sim/não] | [evidência] | [efeito] | [obs] |
| Plataforma < 2,0 | [sim/não] | [evidência] | [efeito] | [obs] |
| LLMOps/MLOps < 2,0 com GenAI/RAG/agentes em produção | [sim/não] | [evidência] | [efeito] | [obs] |
| Operação < 2,0 com produção | [sim/não] | [evidência] | [efeito] | [obs] |
| Sponsor executivo ausente | [sim/não] | [evidência] | [efeito] | [obs] |
| Alto risco sem classificação formal | [sim/não] | [evidência] | [efeito] | [obs] |
| Produção/expansão sem incident response IA | [sim/não] | [evidência] | [efeito] | [obs] |
| Produção crítica/externa sem AI red team ou waiver | [sim/não] | [evidência] | [efeito] | [obs] |
| FRIA/DPIA aplicável ausente | [sim/não] | [evidência] | [efeito] | [obs] |
| L3 < 2 para GenAI/RAG/agentes em produção | [sim/não] | [evidência] | [efeito] | [obs] |
| L5 < 2 para GenAI/RAG/agentes em produção | [sim/não] | [evidência] | [efeito] | [obs] |
| L5 < 3 para agentes externos/alto risco | [sim/não] | [evidência] | [efeito] | [obs] |

## 7. Regras de consistência cruzada

| Regra | Resultado | Evidência | Ação |
|---|---|---|---|
| P5 = plataforma oferece; L4 = solução usa | [ok/risco] | [evidência] | [ação] |
| P5 ≥ 3 e L4 ≤ 2 | [sim/não] | [evidência] | [ação] |
| P5 alto e F1/F4 baixo | [sim/não] | [evidência] | [ação] |
| G1/G3 alto e D2 baixo | [sim/não] | [evidência] | [ação] |
| M3 alto e O1 baixo | [sim/não] | [evidência] | [ação] |

## 8. Matriz de rastreabilidade pergunta-evidência-nota

| ID | Pergunta resumida | Evidência observada | Evidência negativa | Nota | Confiança | Avaliador | Ressalvas | Ação recomendada |
|---|---|---|---|---:|---|---|---|---|
| E1 | [resumo] | [link/artefato] | [lacuna] | [0–4] | [alta/média/baixa] | [nome] | [ressalva] | [ação] |

## 9. Amostragem e protocolo anti-gaming

| Item | Resultado |
|---|---|
| Critério de amostragem usado | [aleatório / risco / produção crítica / combinado] |
| Número de soluções em produção avaliadas | [n] |
| Número de soluções críticas avaliadas | [n] |
| Evidências negativas consideradas | [sim/não — quais] |
| Perguntas com confiança baixa | [lista] |
| Perguntas inconclusivas | [lista] |
| Ajustes de nota por baixa confiança | [lista] |
| Divergências > 1 ponto entre avaliadores | [lista] |
| Terceira opinião acionada | [sim/não] |

## 10. Forças observadas

| Força | Evidência | Impacto |
|---|---|---|
| [força 1] | [evidência] | [impacto] |
| [força 2] | [evidência] | [impacto] |
| [força 3] | [evidência] | [impacto] |

## 11. Lacunas críticas

| Lacuna | Dimensão | Risco | Recomendação | Owner | Prazo |
|---|---|---|---|---|---|
| [lacuna] | [dimensão] | [risco] | [ação] | [owner] | [prazo] |

## 12. Roadmap recomendado

### Próximos 30 dias

| Ação | Owner | Resultado esperado |
|---|---|---|
| [ação] | [owner] | [resultado] |

### 31–60 dias

| Ação | Owner | Resultado esperado |
|---|---|---|
| [ação] | [owner] | [resultado] |

### 61–90 dias

| Ação | Owner | Resultado esperado |
|---|---|---|
| [ação] | [owner] | [resultado] |

## 13. Anexo técnico

| Artefato técnico | Evidência | Observações |
|---|---|---|
| Versões de modelos | [link] | [obs] |
| Versões de prompts | [link] | [obs] |
| Embeddings, índices vetoriais e política de recuperação | [link] | [obs] |
| Cobertura de evals | [link] | [obs] |
| Últimos resultados de regressão | [link] | [obs] |
| Incidentes e postmortems | [link] | [obs] |
| Kill switches/fallbacks testados | [link] | [obs] |
| Exceções e waivers aprovados | [link] | [obs] |
| Risco residual por solução | [link] | [obs] |

## 14. Limitações do assessment

[Descrever limitações: áreas não avaliadas, evidências não disponíveis, entrevistas pendentes, baixa confiança em alguma dimensão, escopo geográfico ou regulatório não coberto, ausência de especialista setorial, ausência de revisão jurídica formal.]

## 15. Decisões executivas necessárias

| Decisão | Opções | Recomendação | Prazo | Owner executivo |
|---|---|---|---|---|
| [decisão] | [opções] | [recomendação] | [prazo] | [owner] |

