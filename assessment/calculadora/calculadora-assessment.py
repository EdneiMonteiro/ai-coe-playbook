# -*- coding: utf-8 -*-
"""
Calculadora do assessment de maturidade do CoE de IA.

Aplica a escala, as regras de contenção e os pesos definidos em
`assessment/criterios-pontuacao.md`, sem arredondamento intermediário.

Uso:
    python calculadora-assessment.py notas.csv contexto.json [--pesos regulado]

Entradas:
    notas.csv     — 50 linhas: dimensao,id,critica,nota (ver notas-exemplo.csv)
    contexto.json — flags operacionais do escopo avaliado (ver contexto-exemplo.json)

Saída: relatório em texto com pontuação por dimensão, nível bruto,
contenções acionadas, nível final, travas de perguntas críticas e
análise de sensibilidade quando pesos alternativos são usados.

Requer apenas a biblioteca padrão do Python 3.8+.
"""

import csv
import json
import sys

for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

DIMENSOES = [
    "Estratégia e mandato",
    "Modelo operacional",
    "Governança e risco",
    "Plataforma e arquitetura",
    "Dados e conhecimento",
    "LLMOps/MLOps e evals",
    "Portfólio e valor",
    "Capacitação e comunidade",
    "FinOps e sustentabilidade",
    "Operação e melhoria contínua",
]

PESOS = {
    "padrao": {d: 0.10 for d in DIMENSOES},
    "regulado": {
        "Estratégia e mandato": 0.10,
        "Modelo operacional": 0.10,
        "Governança e risco": 0.15,
        "Plataforma e arquitetura": 0.10,
        "Dados e conhecimento": 0.15,
        "LLMOps/MLOps e evals": 0.10,
        "Portfólio e valor": 0.10,
        "Capacitação e comunidade": 0.05,
        "FinOps e sustentabilidade": 0.05,
        "Operação e melhoria contínua": 0.10,
    },
}

# Flags esperadas no contexto.json (todas booleanas)
FLAGS = [
    "producao",                                # há qualquer solução em produção
    "genai_rag_agentes_em_producao",           # GenAI/RAG/agentes em produção
    "producao_critica_ou_exposicao_externa",   # produção crítica ou exposição externa
    "sponsor_executivo_claro",
    "caso_alto_risco_sem_classificacao",
    "producao_sem_incident_response",
    "prod_critica_sem_red_teaming_ou_waiver",
    "fria_dpia_aplicavel_ausente",
    "agentes_externos_alto_risco_ou_acao_irreversivel",
]


def nivel(media):
    if media < 1.50:
        return 1
    if media < 2.50:
        return 2
    if media < 3.50:
        return 3
    return 4


def carregar(notas_path, contexto_path):
    notas = {}
    dims = {d: [] for d in DIMENSOES}
    criticas = {}
    with open(notas_path, encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            d = row["dimensao"].strip()
            i = row["id"].strip()
            n = float(row["nota"])
            if d not in dims:
                sys.exit(f"Dimensão desconhecida: {d}")
            if not 0 <= n <= 4:
                sys.exit(f"Nota fora da escala 0-4: {i}={n}")
            dims[d].append(n)
            notas[i] = n
            criticas[i] = row["critica"].strip().lower() in ("sim", "s", "true", "1")
    for d, lst in dims.items():
        if len(lst) != 5:
            sys.exit(f"Dimensão '{d}' tem {len(lst)} perguntas; esperado 5.")
    with open(contexto_path, encoding="utf-8-sig") as f:
        ctx = json.load(f)
    for flag in FLAGS:
        if flag not in ctx:
            sys.exit(f"Flag ausente em contexto.json: {flag}")
    return notas, dims, criticas, ctx


def contencoes(medias, notas, ctx):
    """Retorna lista de (regra, teto, gera_veto)."""
    out = []
    g = medias["Governança e risco"]
    p = medias["Plataforma e arquitetura"]
    l = medias["LLMOps/MLOps e evals"]
    o = medias["Operação e melhoria contínua"]
    genai = ctx["genai_rag_agentes_em_producao"]
    prod = ctx["producao"]

    if g < 2.0:
        out.append(("Governança e risco < 2,0", 2, False))
    if p < 2.0:
        out.append(("Plataforma e arquitetura < 2,0", 2, False))
    if genai and l < 2.0:
        out.append(("LLMOps/MLOps e evals < 2,0 com GenAI/RAG/agentes em produção", 2, False))
    if prod and o < 2.0:
        out.append(("Operação e melhoria contínua < 2,0 com produção", 2, False))
    if not ctx["sponsor_executivo_claro"]:
        out.append(("Sem sponsor executivo claro", 2, False))
    if ctx["caso_alto_risco_sem_classificacao"]:
        out.append(("Caso de alto risco sem classificação formal", 2, True))
    if ctx["producao_sem_incident_response"]:
        out.append(("Produção/expansão sem incident response IA", 2, True))
    if ctx["prod_critica_sem_red_teaming_ou_waiver"]:
        out.append(("Produção crítica/exposição externa sem AI red teaming ou waiver", 2, True))
    if ctx["fria_dpia_aplicavel_ausente"]:
        out.append(("FRIA/DPIA aplicável ausente", 2, True))
    if genai and notas.get("L3", 4) < 2:
        out.append(("L3 < 2 com GenAI/RAG/agentes em produção", 2, False))
    if genai and notas.get("L5", 4) < 2:
        out.append(("L5 < 2 com GenAI/RAG/agentes em produção", 2, False))
    if ctx["agentes_externos_alto_risco_ou_acao_irreversivel"] and notas.get("L5", 4) < 3:
        out.append(("L5 < 3 com agentes externos/alto risco/ação irreversível", 2, True))
    if g < 3.0:
        out.append(("Governança e risco < 3,0", 3, False))
    if ctx["producao_critica_ou_exposicao_externa"] and o < 3.0:
        out.append(("Operação e melhoria contínua < 3,0 com produção crítica", 3, False))
    return out


def consistencia_cruzada(notas):
    """Regras de consistência cruzada: geram alertas, não contenção."""
    alertas = []
    def n(i):
        return notas.get(i, None)
    if n("P5") is not None and n("L4") is not None and n("P5") >= 3 and n("L4") <= 2:
        alertas.append("P5 ≥ 3 e L4 ≤ 2: risco 'plataforma sem adoção'; amostrar logs/traces de ≥ 3 soluções.")
    if n("P5") is not None and n("F1") is not None and n("F4") is not None and n("P5") >= 3 and min(n("F1"), n("F4")) < 2:
        alertas.append("P5 alto e F1/F4 baixo: telemetria sem conexão com custo; revisar dashboards de custo unitário.")
    if n("G1") is not None and n("G3") is not None and n("D2") is not None and max(n("G1"), n("G3")) >= 3 and n("D2") < 2:
        alertas.append("G1/G3 alto e D2 baixo: governança aprova sem controles de dados; revisar base legal/retenção/expurgo.")
    if n("M3") is not None and n("O1") is not None and n("M3") >= 3 and n("O1") < 2:
        alertas.append("M3 alto e O1 baixo: handoff declarado sem ownership operacional; registrar dívida de transição.")
    return alertas


def main():
    argv = sys.argv[1:]
    esquema = "padrao"
    if "--pesos" in argv:
        k = argv.index("--pesos")
        if k + 1 >= len(argv) or argv[k + 1] not in PESOS:
            sys.exit(f"--pesos requer um esquema válido: {', '.join(PESOS)}")
        esquema = argv[k + 1]
        del argv[k:k + 2]
    if len(argv) != 2:
        sys.exit(__doc__)
    notas, dims, criticas, ctx = carregar(argv[0], argv[1])

    medias = {d: sum(v) / 5 for d, v in dims.items()}
    geral_simples = sum(medias.values()) / 10
    pesos = PESOS[esquema]
    geral_ponderada = sum(medias[d] * pesos[d] for d in DIMENSOES) / sum(pesos.values())

    print("=" * 72)
    print("ASSESSMENT DE MATURIDADE DO CoE DE IA: RESULTADO")
    print("=" * 72)
    print(f"\nPontuação por dimensão (média simples de 5 perguntas):\n")
    for d in DIMENSOES:
        peso_txt = f"  peso {pesos[d]:.0%}" if esquema != "padrao" else ""
        print(f"  {medias[d]:.2f}  Nível {nivel(medias[d])}  {d}{peso_txt}")

    print(f"\nPontuação geral (média simples): {geral_simples:.2f}  → Nível bruto {nivel(geral_simples)}")
    if esquema != "padrao":
        print(f"Pontuação geral (ponderada '{esquema}'): {geral_ponderada:.2f} → Nível bruto {nivel(geral_ponderada)}")
        print("Lembrete: pesos alternativos exigem racional, comparação e análise")
        print("de sensibilidade registrados no relatório (criterios-pontuacao.md).")

    regras = contencoes(medias, notas, ctx)
    base = geral_ponderada if esquema != "padrao" else geral_simples
    nivel_final = nivel(base)
    tetos = [teto for _, teto, _ in regras]
    if tetos:
        nivel_final = min(nivel_final, min(tetos))

    print(f"\nContenções acionadas: {len(regras)}")
    for regra, teto, veto in regras:
        marca = "  [VETO OPERACIONAL]" if veto else ""
        print(f"  - {regra} → nível geral máximo = {teto}{marca}")

    print(f"\nNÍVEL FINAL APÓS CONTENÇÕES: {nivel_final}")

    vetos = [r for r, _, v in regras if v]
    if vetos:
        print(f"\nVetos operacionais abertos ({len(vetos)}): produção/expansão dos casos")
        print("afetados bloqueada até remediação, independentemente do nível.")

    trava = [i for i, c in criticas.items() if c and notas[i] < 2]
    if trava:
        print(f"\nTrava anti-gaming, perguntas críticas com nota < 2: {', '.join(sorted(trava))}")
        print("O relatório deve declarar por que cada caso pode permanecer em produção")
        print("OU registrar veto operacional aberto. O board pack deve refletir a decisão.")

    alertas = consistencia_cruzada(notas)
    if alertas:
        print(f"\nAlertas de consistência cruzada ({len(alertas)}):")
        for a in alertas:
            print(f"  - {a}")

    if esquema != "padrao":
        print("\nAnálise de sensibilidade (±2pp nas dimensões de peso ≥ 15%):")
        crits = [d for d in DIMENSOES if pesos[d] >= 0.15]
        cenarios = {"worst": -0.02, "expected": 0.0, "best": +0.02}
        for nome, delta in cenarios.items():
            p2 = dict(pesos)
            for d in crits:
                p2[d] = max(0.0, p2[d] + delta)
            g2 = sum(medias[d] * p2[d] for d in DIMENSOES) / sum(p2.values())
            n2 = min(nivel(g2), min(tetos)) if tetos else nivel(g2)
            print(f"  {nome:9s}: pontuação {g2:.2f} → nível final {n2}")
        print("Se o nível final mudar entre cenários, registrar como risco metodológico.")

    print()


if __name__ == "__main__":
    main()
