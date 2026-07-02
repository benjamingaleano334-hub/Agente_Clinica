# Importar

# ---Interfaz grafica----
import tkinter as tk 
import tkinter.ttk as ttk
from tkinter import messagebox

# -----Modulos-----
from pacientes import guardar_paciente
from consultas import guardar_consulta
from registro import guardar_incidente
from clasificacion import clasificar_incidente
from prioridad import asignar_prioridad
from sugerencias import generar_sugerencias
from respuesta import generar_respuesta  

# --- Validaciones ---
def validar_datos(nombre, edad, telefono):
    # Limpieza
    if not nombre.strip():
        return "El nombre no puede estar vacío."
    if not edad.isdigit():
        return "La edad debe ser un número entero."
    edad_num = int(edad)
    if edad_num <= 0 or edad_num > 120:
        return "La edad debe estar entre 1 y 120."
    if not telefono.isdigit() or len(telefono) < 8 or len(telefono) > 15:
        return "El teléfono debe contener solo números y tener entre 8 y 15 dígitos."
    return None

# --- Acción principal ---
def registrar_consulta():

    # Recuperar lo que el usuario escribio y eliminar espacios extras
    nombre = entry_nombre.get().strip()
    edad = entry_edad.get().strip()
    telefono = entry_telefono.get().strip()
    especialidad = combo_especialidad.get().strip()
    texto_incidente = entry_incidente.get().strip()

    # Validar datos
    error = validar_datos(nombre, edad, telefono)
    if error:
        messagebox.showerror("Error", error)
        return

    # Guardar paciente
    paciente = guardar_paciente({"nombre": nombre, "edad": int(edad), "telefono": telefono})

    # Guardar consulta 
    guardar_consulta(paciente["id"], especialidad)

    # Clasificar incidente
    categoria = clasificar_incidente(texto_incidente)
    prioridad = asignar_prioridad(categoria, texto_incidente)
    sugerencias = generar_sugerencias(categoria, prioridad)

    # Guardar incidente
    incidente = guardar_incidente(texto_incidente, categoria, prioridad, sugerencias)

    # Mostrar respuesta final (solo incidente)
    respuesta = generar_respuesta(incidente)
    messagebox.showinfo("Resultado", respuesta)

# --- Interfaz gráfica ---
# Crear ventana
ventana = tk.Tk()

# Titulo
ventana.title("Agente de Clínica")

# Tamaño
ventana.geometry("400x300")

# Menu
tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

tk.Label(ventana, text="Edad:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_edad = tk.Entry(ventana)
entry_edad.grid(row=1, column=1, padx=5, pady=5)

tk.Label(ventana, text="Teléfono:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry_telefono = tk.Entry(ventana)
entry_telefono.grid(row=2, column=1, padx=5, pady=5)

tk.Label(ventana, text="Especialidad:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
especialidades_validas = [
    "Clínica Médica",
    "Pediatría",
    "Cardiología",
    "Dermatología",
    "Neurología",
    "Ginecología"
]
combo_especialidad = ttk.Combobox(ventana, values=especialidades_validas, state="readonly")
combo_especialidad.grid(row=3, column=1, padx=5, pady=5)

tk.Label(ventana, text="Consulta/Incidente:").grid(row=4, column=0, padx=5, pady=5, sticky="w")
entry_incidente = tk.Entry(ventana)
entry_incidente.grid(row=4, column=1, padx=5, pady=5)

# Boton de accion
btn_guardar = tk.Button(ventana, text="Registrar Consulta", command=registrar_consulta, bg="lightblue")
btn_guardar.grid(row=5, column=0, columnspan=2, pady=15)

# Mantener ventana abierta
ventana.mainloop()
