import json, os

def guardar_paciente(paciente, ruta=None):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    if ruta is None:
        ruta = os.path.join(base_dir, "../data/pacientes.json")
    os.makedirs(os.path.dirname(ruta), exist_ok=True)

    if os.path.exists(ruta):
        with open(ruta, "r", encoding="utf-8") as f:
            pacientes = json.load(f)
    else:
        pacientes = []

    paciente["id"] = len(pacientes) + 1
    pacientes.append(paciente)

    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(pacientes, f, indent=4, ensure_ascii=False)

    return paciente
