# 🏥 Agente de Clínica

Aplicación en **Python** con interfaz gráfica en **Tkinter** que permite registrar pacientes, consultas e incidentes médicos.  
El sistema clasifica automáticamente los incidentes, asigna prioridad y genera sugerencias para el paciente.

---

## 📌 Características principales
- Registro de **pacientes** con nombre, edad y teléfono.
- Registro de **consultas** con especialidad y fecha/hora automáticas.
- Registro de **incidentes** con texto, categoría, prioridad y sugerencias.
- Clasificación automática de incidentes según el texto ingresado.
- Generación de respuestas claras y visuales con emojis.
- Interfaz gráfica simple y amigable en Tkinter.
- Persistencia de datos en archivos JSON (`pacientes.json`, `consultas.json`, `incidentes.json`).

---

## 📂 Estructura del proyecto
```
agente_clinica/
│
├── src/
│   ├── pacientes.py       # Guardar pacientes
│   ├── consultas.py       # Guardar consultas
│   ├── incidentes.py      # Guardar incidentes
│   ├── clasificacion.py   # Clasificar incidentes
│   ├── prioridad.py       # Asignar prioridad
│   ├── sugerencias.py     # Generar sugerencias
│   ├── respuesta.py       # Generar respuesta final
│   └── main.py            # Interfaz gráfica Tkinter
│
├── data/
│   ├── pacientes.json
│   ├── consultas.json
│   └── incidentes.json
│
└── tests/
    └── test_flujo.py      # Test de integración con pytest
```

---

## ⚙️ Instalación
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/usuario/agente_clinica.git
   cd agente_clinica
   ```
2. Crear entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```
3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

*(Si no tenés `requirements.txt`, basta con Python 3 y Tkinter que ya viene incluido en la mayoría de instalaciones).*

---

## 🚀 Uso
Ejecutar la aplicación:
```bash
python src/main.py
```

La ventana permite:
- Ingresar datos del paciente.
- Seleccionar especialidad.
- Escribir el incidente/consulta.
- Registrar todo en el sistema y recibir una respuesta automática.

---

## 🧪 Tests
El proyecto incluye pruebas con **pytest** para verificar el flujo completo:

```bash
pytest tests/
```

Esto valida que:
- Se guarden pacientes correctamente.
- Se registren consultas con fecha/hora.
- Se guarden incidentes con categoría, prioridad y sugerencias.
- Los archivos JSON se creen y contengan datos.

---


👉 Este README.md ya está listo para subir a tu repositorio. ¿Querés que te prepare también un **requirements.txt** con las librerías mínimas necesarias para que todo funcione sin problemas?
