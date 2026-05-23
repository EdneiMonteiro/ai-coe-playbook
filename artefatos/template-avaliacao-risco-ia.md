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
| Dados — transferência internacional | Há dados pessoais transmitidos a provider hospedado fora do Brasil (ou sub-processadores estrangeiros)? Se sim: indicar mecanismo habilitador — (a) decisão de adequação da ANPD; (b) **Cláusulas-Padrão Contratuais (CCPs) — ANPD Res. CD/ANPD nº 19/2024**; (c) Normas Corporativas Globais (NCGs); ou (d) outras hipóteses do art. 33 da LGPD. Registrar data de implementação e referência ao DPA/contrato. | Prazo de adequação às CCPs expirou em 23/08/2025. |
| Dados — uso pelo provider | O provider de modelo/plataforma usa inputs, outputs, prompts ou conversas para treino, fine-tuning, melhoria de modelo ou abuse monitoring? Registrar: (a) cláusula contratual de opt-out aplicada (sim/não/parcial); (b) referência ao DPA/TOS; (c) data de validação. | Em casos de dados sensíveis, segredo comercial ou dados regulados, opt-out deve ser obrigatório. |
| Exposição | Uso interno, parceiro, cliente final, público geral, alto volume, canal crítico | Soluções externas ou de alto volume elevam risco reputacional, operacional e regulatório. |
| Modelo e fornecedor | Modelo, versão, provedor, região, dependências, alternativa de saída | Registrar se o componente é portável, substituível ou dependente de fornecedor específico. |
| Modelo e fornecedor — instrumentos contratuais | DPA assinada (data, versão), AUP vigente do provider (data da última revisão), política de deprecação de modelo (prazo de aviso, plano de migração), lista de sub-processadores aprovada, mecanismo de fallback testado (provider alternativo, data do último teste). | Para casos críticos, exigir fallback multi-provider testado em ≤ 30 min. |
| Classificação regulatória | Categoria inspirada no EU AI Act e obrigações setoriais aplicáveis | Envolver jurídico/compliance quando houver dúvida. |
| EU AI Act — aplicabilidade | Avaliar se a organização está no escopo (provider, deployer, importer, distribuidor) ou se o output do sistema é usado na UE. Se sim: indicar a categoria aplicável (proibido Art. 5; alto risco Anexo III; transparência Art. 50; **GPAI Arts. 51-55** quando usar/integrar modelo GPAI). | Datas-chave: Cap. I/II (incl. Art. 4 AI literacy) desde 02/02/2025; Cap. V (GPAI) desde 02/08/2025; Anexo III + Art. 27 FRIA aplicáveis a partir de 02/08/2026. Consultar jurídico para escopo material/territorial preciso. |
| Classificação interna | Baixo, médio, alto, crítico ou proibido | Usar como camada operacional de tradução para controles internos. |
| Riscos principais | Privacidade, segurança, viés, alucinação, dano operacional, autonomia indevida, reputação, custo, sustentabilidade | Registrar risco inerente antes dos controles e risco residual depois dos controles. |
| Evals mínimos | Groundedness, faithfulness, context precision/recall, recusa correta, toxicidade, viés, latência, custo | Para RAG e agentes, incluir regressão ao trocar modelo, prompt, ferramenta, corpus ou política de recuperação. |
| Controles obrigatórios | Controle de acesso, segregação de ambiente, logs, monitoramento, filtros, human-in-the-loop, fallback, rollback | Cada controle deve ter responsável, evidência e critério de aceite. |
| Red teaming | Necessário, dispensado ou obrigatório antes de produção | Obrigatório para casos de alto risco, exposição externa, agentes com ferramentas ou dados sensíveis. |
| Operação | SLO, owner de produção, suporte, incidente, revisão periódica, critério de desligamento | Nenhuma solução deve ir para produção sem owner operacional e plano de resposta a incidente. |
| Adoção e comunicação | Plano de capacitação dos usuários internos, comunicação para usuários impactados, mecanismo de feedback, sinalização de IA quando aplicável (transparência), e revisão de aceite por amostragem | Aplicável a qualquer caso com usuário humano final (interno ou externo). |
| Decisão | Aprovado, aprovado com restrições, retornar para revisão, bloqueado | Registrar data, justificativa, aprovadores e condições de reavaliação. |

## Matriz operacional de decisão

| Classificação interna | Critério típico | Decisão padrão | Aprovação mínima | SLA de decisão |
|---|---|---|---|---|
| Baixo | Uso interno, dados não sensíveis, IA assistiva, baixo impacto em decisão | Aprovado com controles padrão | Produto/negócio e CoE | ≤ 5 dias úteis |
| Médio | Dados internos relevantes, impacto operacional moderado, dependência de RAG ou modelo externo | Aprovado com restrições e evals documentados | Produto/negócio, CoE, dados e segurança | ≤ 10 dias úteis |
| Alto | Dados sensíveis, impacto material em cliente/cidadão, agente com ferramentas, exposição externa ou decisão relevante | Aprovação condicionada, red teaming e monitoramento reforçado | Segurança/risco/compliance e sponsor executivo | ≤ 15 dias úteis |
| Crítico | Potencial dano legal, financeiro, reputacional ou social relevante; ausência de controle humano suficiente | Comitê de risco antes de qualquer produção | Sponsor executivo, segurança/risco/compliance e CoE; **parecer jurídico formal anexado** | Convocar comitê em ≤ 5 dias úteis |
| Proibido | Prática vedada por lei, política interna ou princípio de IA responsável | Bloqueado | Segurança/risco/compliance e sponsor informado; **parecer jurídico anexado documentando o motivo do bloqueio** | Imediato (D+0) |

## Definition of Done da avaliação de risco

- O caso de uso tem owner de negócio, owner técnico e sponsor identificados.
- A finalidade, o escopo negativo e os usuários impactados estão documentados.
- A classificação regulatória e a classificação interna foram registradas com justificativa.
- As fontes de dados, permissões, retenção, residência e requisitos de privacidade foram avaliados.
- Os evals mínimos foram executados ou planejados com critério de aceite.
- Os controles obrigatórios têm responsável e evidência verificável.
- O risco residual foi aceito pelo papel accountable correspondente à classificação interna do caso (ver "Matriz operacional de decisão"), com registro nominal (nome + função) e data no bloco "Decisão" da ficha.
- O plano de operação inclui monitoramento, incidente, fallback, rollback e critério de desligamento.

