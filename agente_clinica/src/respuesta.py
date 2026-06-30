# src/respuesta.py
def generar_respuesta(incidente):
    texto = incidente["texto"]
    categoria = incidente["categoria"]
    prioridad = incidente["prioridad"]
    sugerencias = incidente["sugerencias"]

    salida = f"""
    📌 Consulta recibida: {texto}
    🏷️ Categoría: {categoria}
    ⚠️ Prioridad: {prioridad}
    ✅ Sugerencias:
    """
    for s in sugerencias:
        salida += f"\n    - {s}"

    return salida
