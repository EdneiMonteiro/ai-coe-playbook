# Charter-modelo resumido para um CoE de IA

Um charter simples evita que o CoE nasça ambíguo. O documento deve caber em poucas páginas e ser aprovado pelo sponsor executivo.

## 1. Missão

Habilitar adoção de IA com segurança, consistência e valor de negócio, por meio de padrões, governança, capacitação, plataforma e ativos reutilizáveis.

## 2. Escopo

O CoE define padrões, mantém catálogo de modelos e ferramentas, orienta arquitetura, coordena governança, apoia PoCs/MVPs estratégicos, capacita comunidades e mede valor, qualidade, risco, custo e sustentabilidade.

## 3. Fora de escopo

O CoE não é dono permanente de produtos de IA, não substitui squads de produto, não opera suporte de primeiro nível, não aprova exceções sem registro de risco e **não negocia ou assina contratos com fornecedores** (Procurement, Jurídico e área demandante conduzem; CoE é consultado para validar adequação técnica e padrões).

## 4. Princípios de decisão

Padrões antes de escala; build-to-transfer; governança embutida na plataforma; menor privilégio para agentes e ferramentas; avaliação contínua; transparência sobre risco, custo e limitações. Evitar concentração crítica em provider único: para casos de alto/crítico risco dependentes de modelo externo, o CoE documenta e testa provider alternativo (exit testado ≥ 1×/ano). Concentração em provider único é registrada como risco contratual e reportada ao Sponsor.

## 5. Direitos de decisão

- **CoE de IA:** decide padrões mínimos, catálogo de modelos aprovados, critérios de avaliação, requisitos de observabilidade e Definition of Done para handoff.
- **Produto/negócio:** decide backlog funcional, experiência do usuário, priorização de domínio e evolução do produto, dentro dos padrões aprovados.
- **Plataforma/cloud:** decide padrões de provisionamento, automação, integração, monitoramento e operação técnica.
- **Segurança, risco e compliance:** definem controles obrigatórios e têm poder de veto em casos de alto risco.
- **Sponsor executivo:** decide trade-offs de investimento, risco residual e go/no-go executivo quando há impacto material.

**Escalada de conflito:** divergência entre CoE e área de veto (Segurança, Risco, Compliance) sobre classificação ou aprovação deve ser registrada — com **parecer jurídico formal anexado quando aplicável** —, com posicionamento de cada parte, e escalada ao Sponsor Executivo em prazo definido (sugestão: ≤ 5 dias úteis para Alto, ≤ 2 dias úteis para Crítico). O Sponsor decide go/no-go com base nos pareceres e formaliza a decisão no instrumento de aprovação.

## 6. Métricas de sucesso

Cada métrica deve ter unidade, baseline e meta documentadas, revisadas anualmente. Exemplos:

- **Adoção de padrões:** % de casos em produção aderentes aos padrões mínimos (baseline ano 1: > 60%; meta ano 2: > 85%).
- **Time-to-production:** dias entre registro do caso e go-live em produção (baseline depende do contexto).
- **Valor por caso de uso:** margem de contribuição ou economia recorrente quando aplicável; OKR de negócio quando não-monetizável.
- **Cobertura de evals:** % de casos com evals automatizados mínimos rodando em CI/CD.
- **Incidentes críticos:** contagem absoluta por trimestre + MTTR.
- **Custo:** custo por interação (LLM) ou custo total por caso/mês.
- **Build-to-transfer:** % de casos em produção > 12 meses com owner em squad de produto (não no CoE).
- **Satisfação:** NPS interno do CoE pelas áreas consumidoras (medido semestralmente).

## 7. Cadência de governança

Revisão quinzenal de portfólio (convocador: CoE), comitê mensal com sponsor executivo (convocador: CoE), revisão trimestral de padrões (convocador: CoE com participação de Plataforma), avaliação semestral do modelo operacional do CoE (convocador: Sponsor executivo) e revisão anual de mandato e escopo do CoE pelo Sponsor executivo.

### Cadência da comunidade de prática

- **Fórum mensal de comunidade de IA:** facilitado pelo CoE; aberto a squads de produto, plataforma e dados. Objetivo: socializar lições, novos padrões e casos de uso em produção. Dono e convocador primário: CoE (R/A); squads atuam como co-facilitadores e podem propor pautas. Se nenhum squad propuser pauta, CoE garante conteúdo mínimo (release notes, métricas de adoção).
- **Comunicação de mudança de padrão:** todo padrão novo ou alteração material publicada pelo CoE deve ser comunicada via release notes + sessão dedicada no fórum mensal. SLA: até 30 dias entre publicação e socialização ativa. Mudanças críticas de segurança (vulnerabilidade em modelo em produção, comportamento adversarial confirmado, CVE com impacto em output): comunicação em até 48h via canal de incidente + sessão extraordinária no fórum dentro de 5 dias úteis.

