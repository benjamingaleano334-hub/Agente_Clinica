# 1. Importar librerias correspondientes
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
import os

# 2. Cargar dataset
data = pd.read_csv("C:/Users/Benja/Downloads/python2/agente_clinica/data/dataset.csv")


# 3. Vectorizar texto
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data["texto"])
y = data["categoria"]

# 4. Entrenar modelo
modelo = MultinomialNB()
modelo.fit(X, y)

# 5. Crear la carpeta si no existe
os.makedirs("agente_clinica/modelos", exist_ok=True)

# 6. Abrir archivo clasificador.pkl en modo escritura binaria
with open("agente_clinica/modelos/clasificador.pkl", "wb") as f:

    # 7. Guardar en ese archivo el modelo entrenado y el vectorizador asi luego se usan ambos juntos, sin entrenar de nuevo
    pickle.dump((modelo, vectorizer), f)

# 8. Mostrar mensaje
print("Modelo entrenado y guardado en models/clasificador.pkl")
