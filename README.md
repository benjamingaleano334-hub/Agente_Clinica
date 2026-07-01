
# 🏥 Agente Clínica

Sistema clínico inteligente en Python que permite registrar pacientes, turnos e incidentes médicos, y además clasificar automáticamente las consultas usando un modelo entrenado.

---

## 📂 Estructura del proyecto

```
agente_clinica/
├── src/                  # Código fuente principal
│   ├── main.py           # Punto de entrada del sistema
│   ├── pacientes.py      # Registro y almacenamiento de pacientes
│   ├── turnos.py         # Registro y almacenamiento de turnos
│   ├── incidentes.py     # Registro y almacenamiento de incidentes
│   ├── clasificacion.py  # Clasificación automática de incidentes
│   ├── prioridad.py      # Asignación de prioridad
│   ├── sugerencias.py    # Generación de sugerencias de acción
│   └── respuesta.py      # Formateo de la salida final
│
├── data/                 # Datos persistentes
│   ├── pacientes.json    # Pacientes registrados
│   ├── turnos.json       # Turnos agendados
│   ├── incidentes.json   # Incidentes clínicos
│   └── dataset.csv       # Dataset de frases para entrenar el modelo
│
├── modelos/              # Modelos entrenados
│   └── clasificador.pkl  # Modelo de clasificación guardado
│
├── tests/                # Pruebas automáticas
│   └── test_integracion.py # Test de integración con pytest
│
└── README.md             # Documentación del proyecto
```

---

## 🚀 Funcionalidades

1. **Registro de pacientes**  
   Guarda datos básicos (nombre, edad, teléfono) en `data/pacientes.json`.

2. **Gestión de turnos**  
   Agenda turnos vinculados a pacientes en `data/turnos.json`.

3. **Registro de incidentes**  
   Guarda consultas médicas en `data/incidentes.json` con categoría, prioridad y sugerencias.

4. **Clasificación automática**  
   Usa el dataset (`data/dataset.csv`) y el modelo entrenado (`modelos/clasificador.pkl`) para categorizar incidentes.

5. **Asignación de prioridad**  
   Determina si el incidente es **Alta, Media o Baja** según la categoría.

6. **Generación de sugerencias**  
   Recomienda acciones según el tipo de incidente (ej. derivar a guardia, notificar médico).

7. **Respuesta formateada**  
   Muestra al usuario un resumen claro con toda la información.

---

## ⚙️ Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tuusuario/agente_clinica.git
   cd agente_clinica
   ```

2. Instalar dependencias (ejemplo con scikit-learn y pandas):
   ```bash
   pip install -r requirements.txt
   ```

*(Podés crear un archivo `requirements.txt` con: `pandas`, `scikit-learn`, `pytest`)*

---

## ▶️ Ejecución

Ejecutar el sistema desde la consola:

```bash
python src/main.py
```

Ejemplo de interacción:

```
Ingrese nombre del paciente: benjamin
Ingrese edad del paciente: 18
Ingrese teléfono del paciente: 1136285252
Ingrese fecha del turno (YYYY-MM-DD): 2026-07-01
Ingrese hora del turno (HH:MM): 10:00
Ingrese especialidad: Clínica Médica
Ingrese consulta/incidente: me duele el pecho
```

Salida:

```
✅ Paciente guardado
✅ Turno guardado
✅ Incidente guardado

📌 Consulta recibida: me duele el pecho
🏷️ Categoría: crítica
⚠️ Prioridad: Alta
✅ Sugerencias:
    - Derivar a guardia inmediatamente
    - Notificar al médico de turno
```

---

## 🧪 Tests

Ejecutar pruebas automáticas con:

```bash
pytest
```

Resultado esperado:

```
collected 1 item
tests/test_integracion.py .
[100%]
```

---


👉 Con este README tu repositorio queda **profesional, claro y listo para mostrar**.  

¿Querés que te arme también el archivo `requirements.txt` para que cualquiera pueda instalar las dependencias y correr tu proyecto sin problemas?
