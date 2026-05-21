# Template de avaliação de risco operacional para casos de uso de IA

Este template deve ser usado na triagem inicial de casos de uso e atualizado antes de MVP, produção e mudanças relevantes de modelo, prompt, dados, ferramenta, agente ou política de recuperação.

Ele não substitui parecer jurídico, avaliação regulatória formal ou revisão de segurança. Sua função é criar uma trilha operacional consistente para decisão do CoE.

## Ficha de avaliação

| Bloco | Campo | Orientação prática |
|---|---|---|
| Identificação | Nome do caso de uso, área dona, sponsor, product owner, responsável técnico | Deve haver dono de negócio e dono técnico antes de qualquer PoC com dados reais. |
| Objetivo | Problema, resultado esperado, decisão ou ação apoiada pela IA | Descrever o que a IA fará e, principalmente, o que ela não fará. |
| Usuários e impactados | Usuários internos, clientes, cidadãos, fornecedores, grupos vulneráveis | Indicar quem usa a solução e quem pode sofrer impacto mesmo sem usá-la diretamente. |
| Tipo de solução | IA preditiva, IA generativa, RAG, agente, automação decisória, copiloto, classificação, recomendação | Marcar múltiplas opções quando aplicável; agentes e automações decisórias exigem avaliação adicional. |
| Grau de autonomia | Assistivo, recomendativo, decisão com humano no loop, decisão automatizada, ação autônoma | Quanto maior a autonomia, maior a exigência de controles, logs, reversão e supervisão humana. |
| Dados | Fontes, proprietário dos dados, dados pessoais, dados sensíveis, segredo comercial, dados regulados | Registrar base legal, finalidade, minimização, retenção, mascaramento, anonimização e residência dos dados. |
| Exposição | Uso interno, parceiro, cliente final, público geral, alto volume, canal crítico | Soluções externas ou de alto volume elevam risco reputacional, operacional e regulatório. |
| Modelo e fornecedor | Modelo, versão, provedor, região, dependências, alternativa de saída | Registrar se o componente é portável, substituível ou dependente de fornecedor específico. |
| Classificação regulatória | Categoria inspirada no EU AI Act e obrigações setoriais aplicáveis | Envolver jurídico/compliance quando houver dúvida. |
| Classificação interna | Baixo, médio, alto, crítico ou proibido | Usar como camada operacional de tradução para controles internos. |
| Riscos principais | Privacidade, segurança, viés, alucinação, dano operacional, autonomia indevida, reputação, custo, sustentabilidade | Registrar risco inerente antes dos controles e risco residual depois dos controles. |
| Evals mínimos | Groundedness, faithfulness, context precision/recall, recusa correta, toxicidade, viés, latência, custo | Para RAG e agentes, incluir regressão ao trocar modelo, prompt, ferramenta, corpus ou política de recuperação. |
| Controles obrigatórios | Controle de acesso, segregação de ambiente, logs, monitoramento, filtros, human-in-the-loop, fallback, rollback | Cada controle deve ter responsável, evidência e critério de aceite. |
| Red teaming | Necessário, dispensado ou obrigatório antes de produção | Obrigatório para casos de alto risco, exposição externa, agentes com ferramentas ou dados sensíveis. |
| Operação | SLO, owner de produção, suporte, incidente, revisão periódica, critério de desligamento | Nenhuma solução deve ir para produção sem owner operacional e plano de resposta a incidente. |
| Decisão | Aprovado, aprovado com restrições, retornar para revisão, bloqueado | Registrar data, justificativa, aprovadores e condições de reavaliação. |

## Matriz operacional de decisão

| Classificação interna | Critério típico | Decisão padrão | Aprovação mínima |
|---|---|---|---|
| Baixo | Uso interno, dados não sensíveis, IA assistiva, baixo impacto em decisão | Aprovado com controles padrão | Produto/negócio e CoE |
| Médio | Dados internos relevantes, impacto operacional moderado, dependência de RAG ou modelo externo | Aprovado com restrições e evals documentados | Produto/negócio, CoE, dados e segurança |
| Alto | Dados sensíveis, impacto material em cliente/cidadão, agente com ferramentas, exposição externa ou decisão relevante | Aprovação condicionada, red teaming e monitoramento reforçado | Segurança/risco/compliance e sponsor executivo |
| Crítico | Potencial dano legal, financeiro, reputacional ou social relevante; ausência de controle humano suficiente | Comitê de risco antes de qualquer produção | Sponsor executivo, jurídico, risco/compliance e CoE |
| Proibido | Prática vedada por lei, política interna ou princípio de IA responsável | Bloqueado | Segurança/risco/compliance, jurídico e sponsor informado |

## Definition of Done da avaliação de risco

- O caso de uso tem owner de negócio, owner técnico e sponsor identificados.
- A finalidade, o escopo negativo e os usuários impactados estão documentados.
- A classificação regulatória e a classificação interna foram registradas com justificativa.
- As fontes de dados, permissões, retenção, residência e requisitos de privacidade foram avaliados.
- Os evals mínimos foram executados ou planejados com critério de aceite.
- Os controles obrigatórios têm responsável e evidência verificável.
- O risco residual foi aceito pelo papel accountable adequado.
- O plano de operação inclui monitoramento, incidente, fallback, rollback e critério de desligamento.

