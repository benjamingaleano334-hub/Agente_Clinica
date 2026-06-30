# src/prioridad.py
def asignar_prioridad(categoria, texto):
    if categoria == "critica":
        return "Alta"
    elif categoria == "general":
        return "Media"
    elif categoria == "administrativa":
        return "Baja"
    else:
        return "Pendiente"
