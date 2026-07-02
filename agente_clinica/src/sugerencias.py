# 1. Crear funcion
def generar_sugerencias( prioridad):
    """
    Parametros:
    prioridad: el nivel de prioridad asignado (Alta, Media, Baja, Pendiente).
    """

    # 2. Para cada prioridad devolver su respectiva sugerencia
    if prioridad == "Alta":
        return [
            "Diríjase a la guardia inmediatamente",
            "Contacte a su médico de cabecera cuanto antes",
            "Su consulta ha sido registrada en el sistema para seguimiento"
        ]
    elif prioridad == "Media":
        return [
            "Agende una consulta en clínica en los próximos días",
            "Repose y controle síntomas en casa",
            "Su consulta quedó guardada y será revisada por el equipo médico"
        ]
    elif prioridad == "Baja":
        return [
            "Comuníquese con administración para trámites",
            "Verifique disponibilidad de turnos en recepción",
            "Su solicitud fue registrada correctamente en el sistema"
        ]
    
    # 3. Pendiente u otro caso
    else:  
        return [
            "Su consulta fue registrada, un profesional la revisará",
            "Si los síntomas empeoran, acuda a la guardia"
        ]
