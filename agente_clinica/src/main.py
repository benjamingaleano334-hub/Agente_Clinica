from clasificacion import clasificar_incidente
from prioridad import asignar_prioridad
from sugerencias import generar_sugerencias
from pacientes import guardar_paciente
from turnos import guardar_turno
from registro import guardar_incidente
from respuesta import generar_respuesta   # 👈 importamos tu función

if __name__ == "__main__":
    # Registrar paciente
    nombre = input("Ingrese nombre del paciente: ")
    edad = input("Ingrese edad del paciente: ")
    telefono = input("Ingrese teléfono del paciente: ")

    nuevo_paciente = guardar_paciente({
        "nombre": nombre,
        "edad": edad,
        "telefono": telefono
    })
    print("✅ Paciente guardado")

    # Registrar turno
    fecha = input("Ingrese fecha del turno (YYYY-MM-DD): ")
    hora = input("Ingrese hora del turno (HH:MM): ")
    especialidad = input("Ingrese especialidad: ")

    nuevo_turno = guardar_turno({
        "paciente_id": nuevo_paciente["id"],
        "fecha": fecha,
        "hora": hora,
        "especialidad": especialidad
    })
    print("✅ Turno guardado")

    # Registrar incidente
    texto = input("Ingrese consulta/incidente: ")
    categoria = clasificar_incidente(texto)
    prioridad = asignar_prioridad(categoria, texto)
    sugerencias = generar_sugerencias(categoria, prioridad)

    nuevo_incidente = guardar_incidente(texto, categoria, prioridad, sugerencias)
    print("✅ Incidente guardado")

    # Mostrar respuesta final usando respuesta.py
    salida = generar_respuesta(nuevo_incidente)
    print(salida)
