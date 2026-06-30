import json, os

def guardar_incidente(texto, categoria, prioridad, sugerencias, ruta=None):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    if ruta is None:
        ruta = os.path.join(base_dir, "../data/incidentes.json")
    os.makedirs(os.path.dirname(ruta), exist_ok=True)

    if os.path.exists(ruta):
        with open(ruta, "r", encoding="utf-8") as f:
            incidentes = json.load(f)
    else:
        incidentes = []

    incidente = {
        "id": len(incidentes) + 1,
        "texto": texto,
        "categoria": categoria,
        "prioridad": prioridad,
        "sugerencias": sugerencias
    }
    incidentes.append(incidente)

    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(incidentes, f, indent=4, ensure_ascii=False)

    return incidente

