# 1. Crear funcion
def generar_respuesta(incidente):
    """Parametro:
       incidente: es un diccionario con toda la información del incidente (texto, categoría, prioridad, sugerencias).
       """
    # 2. Extraer los valores del diccionario incidente y los guarda en variables:
    texto = incidente["texto"]
    categoria = incidente["categoria"]
    prioridad = incidente["prioridad"]
    sugerencias = incidente["sugerencias"]
 
    # 3. Mostrar salida
    salida = f"""
    📌 Consulta recibida: {texto}
    🏷️ Categoría: {categoria}
    ⚠️ Prioridad: {prioridad}
    ✅ Sugerencias:
    """
    # 4. Recorrer la lista de sugerencias (sugerencias).Por cada sugerencia, agrega una nueva línea al texto salida con un guion (-) delante.Así se arma una lista ordenada de recomendaciones.
    for s in sugerencias:
        salida += f"\n    - {s}"
 
    # 5. Devolver salida
    return salida
