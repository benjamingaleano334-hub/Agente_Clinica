# 1. Importar modulos
# json para escribir y leer datos en formato json y os para manejar rutas de archivos y directorios
import json, os
# datetime para la hora y fecha actual
from datetime import datetime

# 2. Crear funcion 
def guardar_consulta(paciente_id, especialidad, ruta=None):
    """
    Parametros:
    paciente_id: el ID del paciente que hace la consulta.
    especialidad: la especialidad médica elegida.
    ruta: opcional, la ubicación del archivo JSON donde se guardan las consultas. Si no se pasa, se usa una ruta por defecto.
    """
    # 3. Si no se especifica ruta, se construye automáticamente
    if ruta is None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        ruta = os.path.join(base_dir, "../data/consultas.json")
        
    # 4. Leer archivo existente o crear lista nueva
    if os.path.exists(ruta):
        with open(ruta, "r", encoding="utf-8") as f:
            consultas = json.load(f)
    else:
        consultas = []
   
    # 5. ID incremental: cantidad de consultas + 1
    nuevo_id = len(consultas) + 1

    # 6. Crear consulta con fecha y hora automáticas
    consulta = {
        "id": nuevo_id,  
        "paciente_id": paciente_id,
        "especialidad": especialidad,
        "fecha_consulta": datetime.now().strftime("%Y-%m-%d"),
        "hora_consulta": datetime.now().strftime("%H:%M:%S")
    }

    
    # 7. Agregar el diccionario consulta con sus datos dentro de la lista consultas
    consultas.append(consulta)

    # 8. Guardar en JSON
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(consultas, f, indent=4, ensure_ascii=False)
    
    # 9. Devolver el diccionario con la consulta por si es necesario usarlo
    return consulta
