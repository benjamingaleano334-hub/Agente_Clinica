import json, os

def guardar_turno(turno, ruta=None):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    if ruta is None:
        ruta = os.path.join(base_dir, "../data/turnos.json")
    os.makedirs(os.path.dirname(ruta), exist_ok=True)

    if os.path.exists(ruta):
        with open(ruta, "r", encoding="utf-8") as f:
            turnos = json.load(f)
    else:
        turnos = []

    turno["id"] = len(turnos) + 1
    turnos.append(turno)

    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(turnos, f, indent=4, ensure_ascii=False)

    return turno
