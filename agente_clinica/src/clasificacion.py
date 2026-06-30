import pickle

def clasificar_incidente(texto):
    # Cargar modelo y vectorizador
    with open("agente_clinica/modelos/clasificador.pkl", "rb") as f:
        modelo, vectorizer = pickle.load(f)

    # Transformar texto
    X = vectorizer.transform([texto])

    # Predecir categoría
    categoria = modelo.predict(X)[0]
    return categoria
