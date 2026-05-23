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

Em modo diagnóstico interno, as colunas normativas podem ser preenchidas apenas quando relevantes. Em modo auditoria/investimento, uso externo, regulado, funding, due diligence ou M&A, a matriz normativa é obrigatória para perguntas críticas, gates go/no-go e lacunas materiais. A coluna **GPAI Arts. 51–55** é obrigatória quando a organização avaliada usa modelo classificado como GPAI sob o EU AI Act; pode ficar como `n/a` em demais casos. Para crosswalk consolidado entre NIST AI RMF, ISO/IEC 42001, EU AI Act e LGPD, consulte o [crosswalk normativo em `referencias/`](../referencias/crosswalk-normativo.md).

| ID | Pergunta resumida | Evidência observada | Evidência negativa | Nota | Confiança | Avaliador | Decisão go/no-go | NIST AI RMF | ISO/IEC 42001 Anexo A | EU AI Act artigo | GPAI Arts. 51–55 | LGPD/GDPR | Tipo de exigência | Owner regulatório | Periodicidade | Ressalvas | Ação recomendada |
|---|---|---|---|---:|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E1 | [resumo] | [link/artefato] | [lacuna] | [0–4] | [alta/média/baixa] | [nome] | [aprovar/restringir/vetar/n/a] | [função/subcategoria] | [controle] | [artigo/n/a] | [artigo/n/a] | [artigo/n/a] | [lei/norma voluntária/política interna/boa prática] | [owner] | [mensal/trimestral/anual/evento] | [ressalva] | [ação] |

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

Para produção e casos de alto risco, anexar pacote documental mínimo: **model card**, **system card** e, quando houver corpus RAG/datasets críticos, **datasheet**. Esses artefatos devem cobrir intended use, misuse, limitações conhecidas, métricas, vieses conhecidos, mudanças materiais, logs relevantes, owners nominados (pessoa com email institucional, não cargo genérico) e risco residual.

Em sistemas baseados em **GPAI** sob escopo do EU AI Act, registrar também a divulgação técnica exigida pelo Art. 53 e referências a documentação do provedor.

> **Nota — GPAI e SaaS terceirizado.** Para sistemas baseados em GPAI ou SaaS terceirizado, campos do model card que dependem de internals do modelo (pesos, datasets de treino, métricas internas, ablation studies) podem ser declarados como **N/A — substituído por system card e contrato/SLA do provider**. O system card deve então registrar: identificação do provider, versão do modelo/serviço, escopo de uso, controles contratuais aplicáveis, dependências críticas, plano de saída e referência à documentação técnica pública do provider (incluindo GPAI Art. 53 disclosure quando aplicável).

| Artefato técnico | Owner nominado | Evidência | Observações |
|---|---|---|---|
| Model card | [pessoa/email] | [link] | Intended use, limitações, métricas, vieses conhecidos, versões, mudanças materiais, licença e origem (OSS vs proprietary) quando aplicável. |
| System card | [pessoa/email] | [link] | Arquitetura do sistema, integrações, guardrails, riscos, incidentes, logs, controles operacionais; GPAI Art. 53 disclosure quando aplicável; check de contaminação treino/eval realizado por [pessoa/equipe] — **N/A para GPAI/SaaS terceirizado quando o provider não expõe internals; nesse caso declarar "N/A — substituído por contrato/SLA do provider" e referenciar a documentação técnica pública do provider**. |
| Datasheet de corpus RAG/dataset crítico | [pessoa/email] | [link] | Proveniência, finalidade, base legal, retenção, limitações, atualização, expurgo e owner; status de anonimização do corpus, dos logs de interação e dos embeddings. |
| Versões de modelos | [pessoa/email] | [link] | Inclui licença e origem (OSS vs proprietary) quando relevante. |
| Versões de prompts | [pessoa/email] | [link] | [obs] |
| Embeddings, índices vetoriais e política de recuperação | [pessoa/email] | [link] | Status de anonimização declarado; embeddings tratados como dado pseudonimizado por definição quando derivados de dados pessoais. |
| Cobertura de evals e harness integrity | [pessoa/email] | [link] | Hash do golden dataset, judge independente do gerador, controle de contaminação treino/eval. |
| Últimos resultados de regressão | [pessoa/email] | [link] | [obs] |
| Incidentes e postmortems | [pessoa/email] | [link] | [obs] |
| Kill switches/fallbacks testados | [pessoa/email] | [link] | [obs] |
| Exceções e waivers aprovados | [pessoa/email] | [link] | [obs] |
| Transferência internacional de dados via API GPAI | [pessoa/email] | [link] | Fornecedor, jurisdição de processamento, base para transferência internacional (LGPD Art. 33 / GDPR Cap. V) e cláusulas contratuais aplicáveis. |
| Risco residual por solução | [pessoa/email] | [link] | [obs] |

## 14. Pesos e análise de sensibilidade

Preencher quando forem usados pesos diferentes de 10% por dimensão. Se esta seção não for preenchida, o relatório deve usar a média simples.

A análise de sensibilidade deve cobrir, no mínimo, **variação de ±2 pontos percentuais** por dimensão crítica e três cenários: **worst**, **expected** e **best**. Se a mudança de pesos alterar o nível geral, a aplicação de contenção ou a decisão executiva em qualquer um dos cenários, registrar como risco metodológico e exigir aceite explícito do sponsor.

Em **modo auditoria/investimento**, a aprovação dos pesos deve ser feita por **avaliador independente que não seja o sponsor avaliado**, para evitar conflito metodológico. Em **modo diagnóstico interno**, o board pack deve declarar explicitamente quando os pesos foram aprovados pelo próprio sponsor avaliado.

| Item | Registro |
|---|---|
| Esquema de pesos usado | [padrão 10% / regulado / customizado] |
| Regulação ou contexto que justifica pesos alternativos | [descrição] |
| Racional por dimensão alterada | [descrição] |
| Pontuação e nível com pesos padrão | [resultado] |
| Pontuação e nível com pesos alternativos | [resultado] |
| Cenário worst (−2pp dimensões críticas) | [resultado; mudança de nível/contenção/decisão] |
| Cenário expected | [resultado] |
| Cenário best (+2pp dimensões críticas) | [resultado; mudança de nível/contenção/decisão] |
| Análise de sensibilidade — síntese | [se decisão muda entre cenários, registrar como risco metodológico] |
| Modo de aplicação | [diagnóstico interno / auditoria-investimento] |
| Owner metodológico | [nome/cargo] |
| Aprovador dos pesos | [nome/cargo — em modo auditoria, deve ser avaliador independente, não o sponsor avaliado] |
| Sponsor que aceitou risco metodológico | [nome/cargo] |

## 15. Limitações do assessment

[Descrever limitações: áreas não avaliadas, evidências não disponíveis, entrevistas pendentes, baixa confiança em alguma dimensão, escopo geográfico ou regulatório não coberto, ausência de especialista setorial, ausência de revisão jurídica formal.]

**Nota sobre auto-assessment.** Quando o assessment for conduzido apenas por avaliadores internos, sem revisor externo, sua validade é limitada para: (a) decisão de investimento de comitê executivo com peso fiduciário; (b) apresentação a regulador ou autoridade de proteção de dados; (c) due diligence de M&A; (d) comunicação pública de conformidade. Para esses usos, exigir auditoria assistida por revisor externo independente e, quando aplicável, asseguração credenciada.

## 16. Decisões executivas necessárias

| Decisão | Opções | Recomendação | Prazo | Owner executivo |
|---|---|---|---|---|
| [decisão] | [opções] | [recomendação] | [prazo] | [owner] |

## Anexo C — Crosswalk normativo NIST AI RMF × ISO/IEC 42001 × EU AI Act × LGPD/GDPR

O crosswalk normativo foi extraído para vida própria em [`../referencias/crosswalk-normativo.md`](../referencias/crosswalk-normativo.md), permitindo reutilização entre o assessment e o artigo principal sem duplicação.

Use o crosswalk consolidado como referência canônica para preencher as colunas normativas da matriz §8 (NIST AI RMF, ISO/IEC 42001 Anexo A, EU AI Act, GPAI Arts. 51–55, LGPD/GDPR), bem como o anexo setorial brasileiro e os instrumentos de transferência internacional de dados.

> Antes de usar para auditoria/investimento, confirme que o crosswalk foi reavaliado contra a última versão das normas de referência (ver seção "Versionamento normativo" do arquivo).
