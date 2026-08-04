# Comece aqui

O playbook completo tem artigo, artefatos, assessment, diagramas e referências. Esta página é o caminho mínimo para sair do zero sem ler tudo.

## Se você tem 15 minutos

1. Leia o [resumo executivo do artigo](artigos/coe-ia-playbook.md#resumo-executivo) (6 parágrafos): a tese, o modelo federado e as seis funções de um CoE de IA.
2. Veja o [diagrama do modelo hub-and-spoke](diagramas/01-hub-spoke-federado.md): quem decide o quê.
3. Percorra o [exemplo preenchido do assessment](assessment/exemplo-preenchido.md): como uma organização fictícia nível 3 "na média" termina em nível 2 com dois vetos operacionais.

## Se você vai criar um CoE de IA agora

| Passo | Use | Tempo típico |
|---|---|---|
| 1. Formalizar mandato e sponsor | [`artefatos/charter-coe-ia.md`](artefatos/charter-coe-ia.md): adapte missão, escopo, fora de escopo e direitos de decisão | 1 a 2 semanas |
| 2. Definir papéis | [`artefatos/raci-coe-ia.md`](artefatos/raci-coe-ia.md): ajuste as colunas à sua estrutura (DPO e Jurídico separados se regulado) | 1 semana |
| 3. Triar o primeiro caso de uso | [`artefatos/template-avaliacao-risco-ia.md`](artefatos/template-avaliacao-risco-ia.md): preencha a ficha e aplique a matriz de decisão | Por caso |
| 4. Seguir o roadmap | [Seção 13 do artigo](artigos/coe-ia-playbook.md#13-roadmap-de-implementacao): 30/60/90/180 dias | Contínuo |

## Se você já tem um CoE e quer saber onde está

1. Responda o [questionário de 50 perguntas](assessment/questionario-assessment.md) com evidências (não intenção).
2. Rode a [calculadora](assessment/calculadora/) sobre suas notas: ela aplica as regras de contenção e aponta vetos operacionais.
3. Compare com o [exemplo preenchido](assessment/exemplo-preenchido.md) para calibrar o rigor das notas.
4. Produza o [relatório auditável](assessment/relatorio-template.md) e, para decisão executiva, o [board pack de uma página](assessment/board-pack-template.md).

## Se você precisa aprovar um caso de uso arriscado

1. Classifique com o [template de avaliação de risco](artefatos/template-avaliacao-risco-ia.md) (inclui LGPD, GDPR, EU AI Act e due diligence de fornecedor).
2. Consulte a [matriz risco × controles](diagramas/08-matriz-risco-controles.md): controles cumulativos por nível e SLAs de decisão.
3. Se envolver dados pessoais, veja os [regimes de dados](diagramas/06-regimes-dados.md): treino, inferência/RAG e logs têm controles distintos.
4. Antes de produção, confirme os gates go/no-go em [`assessment/criterios-pontuacao.md`](assessment/criterios-pontuacao.md#gates-de-gono-go-operacional).

## Aviso

Os materiais são ponto de partida, não parecer jurídico ou regulatório. Adapte ao seu setor, jurisdição e apetite de risco (ver [escopo no README](README.md#escopo)).
