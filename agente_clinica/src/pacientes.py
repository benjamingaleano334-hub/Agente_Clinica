# 1. Importar
import json, os

# 2. Crear funcion
def guardar_paciente(paciente, ruta=None):
    """
    Recibe:
    paciente: un diccionario con los datos del paciente (nombre, edad, teléfono).
    ruta: opcional, la ubicación del archivo JSON donde se guardan los pacientes. Si no se pasa, se usa una ruta por defecto.
    """
    # 3. Buscar el archivo
    base_dir = os.path.dirname(os.path.abspath(__file__))
    if ruta is None:
        ruta = os.path.join(base_dir, "../data/pacientes.json")
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    
    # 4. Crear carpeta si no existe
    if os.path.exists(ruta):
        with open(ruta, "r", encoding="utf-8") as f:
            pacientes = json.load(f)
    else:
        pacientes = []
    
    # 5. Asignar id unico al paciente
    paciente["id"] = len(pacientes) + 1

    # 6. Guardar cada nuevo paciente en la lista
    pacientes.append(paciente)
    
    # 7. Abrir archivo pacientes.json en formato escritura
    with open(ruta, "w", encoding="utf-8") as f:

        # 8. Guardar la lista en formato json,legible con sangria y que acepte caracteres especiales
        json.dump(pacientes, f, indent=4, ensure_ascii=False)
    
    # 9. Devolver el diccionario del paciente con su nuevo id para usarlo en main.py
    return paciente
