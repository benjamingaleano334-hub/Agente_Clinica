def generar_sugerencias(categoria, prioridad):
    if categoria == "critica" and prioridad == "Alta":
        return [
            "Derivar a guardia inmediatamente",
            "Notificar al médico de turno",
            "Registrar en sistema como emergencia"
        ]
    elif categoria == "general" and prioridad == "Media":
        return [
            "Ofrecer turno disponible en clínica médica",
            "Recomendar reposo y control de síntomas",
            "Registrar solicitud en sistema"
        ]
    elif categoria == "administrativa" and prioridad == "Baja":
        return [
            "Informar requisitos administrativos",
            "Ofrecer horarios de atención",
            "Registrar consulta en sistema"
        ]
    else:
        return ["No se encontraron sugerencias específicas"]

