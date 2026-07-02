# 1.Importar pickle, que sirve para deserializar (cargar) objetos guardados en un archivo .pkl.
import pickle

# 2. Crear funcion que recibe texto(la consulta/incidente del usuario)
def clasificar_incidente(texto):

    # 3. Cargar modelo y vectorizador
    with open("agente_clinica/modelos/clasificador.pkl", "rb") as f:

       # 4. pickle.load(f) los deserializa (los reconstruye en memoria) y los asigna a las variables modelo y vectorizer.
        modelo, vectorizer = pickle.load(f)

    # 5. Transformar texto
    X = vectorizer.transform([texto])

    # 6. Predecir categoría
    categoria = modelo.predict(X)[0]

    # 7. Devolver categoria
    return categoria
