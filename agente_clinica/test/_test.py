# Importar
import json
from src.pacientes import guardar_paciente
from src.consultas import guardar_consulta
from src.registro import guardar_incidente

# Preparar entorno de prueba en una carpeta temporal
def test_flujo_completo(tmp_path):
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    pacientes_file = data_dir / "pacientes.json"
    consultas_file = data_dir / "consultas.json"
    incidentes_file = data_dir / "incidentes.json"

    # Guardar paciente
    paciente = guardar_paciente({
        "nombre": "Test Paciente",
        "edad": 30,
        "telefono": "111222333"
    }, ruta=pacientes_file)
    assert paciente["id"] == 1

    # Guardar consulta
    consulta = guardar_consulta(
        paciente["id"],
        "Clínica Médica",
        ruta=consultas_file
    )
    assert consulta["id"] == 1
    assert consulta["paciente_id"] == paciente["id"]
    assert consulta["especialidad"] == "Clínica Médica"

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
    assert incidente["prioridad"] == "Alta"

    # Verificar que los archivos se crearon y contienen datos
    for archivo in [pacientes_file, consultas_file, incidentes_file]:
        assert archivo.exists()
        with open(archivo, "r", encoding="utf-8") as f:
            contenido = json.load(f)
            assert len(contenido) == 1
