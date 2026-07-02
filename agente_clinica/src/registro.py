# 1. Importar
import json, os

# 2. Crear funcion
def guardar_incidente(texto, categoria, prioridad, sugerencias, ruta=None):
    """
    Parametros:
    texto: la descripción del incidente.
    categoria: la categoría asignada por el clasificador.
    prioridad: el nivel de prioridad (Alta, Media, Baja, Pendiente).
    sugerencias: recomendaciones generadas para el incidente.
    ruta: opcional, la ubicación del archivo JSON donde se guardan los incidentes.
    """

    # 3. Buscar ruta
    base_dir = os.path.dirname(os.path.abspath(__file__))
    if ruta is None:
        ruta = os.path.join(base_dir, "../data/incidentes.json")
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    
    # 4. Crear carpeta si no existe
    if os.path.exists(ruta):
        with open(ruta, "r", encoding="utf-8") as f:
            incidentes = json.load(f)
    else:
        incidentes = []
    
    # 5. Crear diccionario con los datos
    incidente = {
        "id": len(incidentes) + 1,
        "texto": texto,
        "categoria": categoria,
        "prioridad": prioridad,
        "sugerencias": sugerencias
    }

    # 6. Agregar diccionario a la lista
    incidentes.append(incidente)

    # 7. Abrir archivo incidentes.json en formato escritura
    with open(ruta, "w", encoding="utf-8") as f:
        # 8. Guardar la lista en formato json,legible con sangria y que acepte caracteres especiales
        json.dump(incidentes, f, indent=4, ensure_ascii=False)
 
    # 9. Devolver el diccionario
    return incidente

