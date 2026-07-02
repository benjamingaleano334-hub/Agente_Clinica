# 1. Crear funcion
def asignar_prioridad(categoria):
    """Recibe el parámetro:
     categoria: la categoría que salió del clasificador (ejemplo: "critica", "general", "administrativa").
    """

    if categoria == "critica":
        return "Alta"
    elif categoria == "general":
        return "Media"
    elif categoria == "administrativa":
        return "Baja"
    else:
        return "Pendiente"
