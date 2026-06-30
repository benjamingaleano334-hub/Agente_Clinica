import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
import os

# 1. Cargar dataset
data = pd.read_csv("C:/Users/Benja/Downloads/python2/agente_clinica/data/dataset.csv")


# 2. Vectorizar texto
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data["texto"])
y = data["categoria"]

# 3. Entrenar modelo
modelo = MultinomialNB()
modelo.fit(X, y)

os.makedirs("agente_clinica/modelos", exist_ok=True)
with open("agente_clinica/modelos/clasificador.pkl", "wb") as f:
    pickle.dump((modelo, vectorizer), f)


print("Modelo entrenado y guardado en models/clasificador.pkl")
