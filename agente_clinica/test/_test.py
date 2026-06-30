import json

from src.pacientes import guardar_paciente
from src.turnos import guardar_turno
from src.registro import guardar_incidente

def test_flujo_completo(tmp_path):
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    pacientes_file = data_dir / "pacientes.json"
    turnos_file = data_dir / "turnos.json"
    incidentes_file = data_dir / "incidentes.json"

    # Guardar paciente
    paciente = guardar_paciente({
        "nombre": "Test Paciente",
        "edad": "30",
        "telefono": "111222333"
    }, ruta=pacientes_file)
    assert paciente["id"] == 1

    # Guardar turno
    turno = guardar_turno({
        "paciente_id": paciente["id"],
        "fecha": "2026-07-01",
        "hora": "10:00",
        "especialidad": "Clínica Médica"
    }, ruta=turnos_file)
    assert turno["id"] == 1
    assert turno["paciente_id"] == paciente["id"]

    # Guardar incidente
    incidente = guardar_incidente(
        "me duele el pecho",
        "critica",
        "Alta",
        ["Derivar a guardia inmediatamente"],
        ruta=incidentes_file
    )
    assert incidente["id"] == 1
    assert incidente["categoria"] == "critica"

    # Verificar que los archivos se crearon y contienen datos
    for archivo in [pacientes_file, turnos_file, incidentes_file]:
        assert archivo.exists()
        with open(archivo, "r", encoding="utf-8") as f:
            contenido = json.load(f)
            assert len(contenido) == 1

