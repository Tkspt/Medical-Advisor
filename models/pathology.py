# Importer les bibliothèques requises
import os
import flet as ft  # Utiliser ft pour la compatibilité avec Flet
import numpy as np
import pandas as pd

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Embedding, GRU, Dense
from keras.preprocessing.text import tokenizer_from_json

# Désactiver TF_ENABLE_ONEDNN_OPTS si nécessaire
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

def load_data(fichier = "assets\docs\Liste_maladies.xlsx"):
    data = pd.read_excel(fichier)

    # Convertir les colonnes de pathologie en chaînes de caractères
    for i in range(1, 6):
        data[f"Pathologie {i}"] = data[f"Pathologie {i}"].astype(str)
    return data

def build_model():
        # Charger les données
    data = load_data()    
    # Créer le tokenizer
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(data["Pathologie 1"] + data["Pathologie 2"] + data["Pathologie 3"] + data["Pathologie 4"] + data["Pathologie 5"])

    # Construire le modèle GRU
    model = Sequential()
    model.add(Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=100))  # Ajouter 1 pour gérer les mots inconnus
    model.add(GRU(128))
    model.add(Dense(5, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    # Sauvegarder le tokenizer en JSON
    tokenizer_json = tokenizer.to_json()
    with open('tokenizer.json', 'w', encoding='utf-8') as json_file:
        json_file.write(tokenizer_json)
    model.save('assets\models\pathologie.h5')

def load_tokenizer(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = file.read()
        tokenizer = tokenizer_from_json(data)
    return tokenizer

# Fonction pour prédire les informations en fonction des pathologies saisies
def predire_maladie(pathologies):
    model = load_model('assets\models\pathologie.h5')
    tokenizer = load_tokenizer('tokenizer.json')
    data = load_data() 
    
    sequences = tokenizer.texts_to_sequences([pathologies])
    padded_sequences = pad_sequences(sequences, maxlen=5)
    predictions = model.predict(padded_sequences)
	
    index_prediction = np.argmax(predictions)

    nom_maladie = data.loc[index_prediction, "Maladie"]
    nom_famille = data.loc[index_prediction, "Famille"]
    nom_remede = data.loc[index_prediction, "Remede"]
    nom_medicament = data.loc[index_prediction, "Medicament"]
    nom_effet_secondaire = data.loc[index_prediction, "Effet_Secondaire_Medicament"]
    
    return f"$Votre maladie est susceptible d'être {nom_maladie} de la famille ${nom_famille}. On vous recomande le remède ${nom_remede} ainsi que le médicament ${nom_medicament}. les potentiels effets secondaire sont ${nom_effet_secondaire}"

    # print(nom_maladie)
    # print(nom_famille)
    # print(nom_remede)
    # print(nom_medicament)
    # print(nom_effet_secondaire)

# Fonction principale pour créer l'interface Flet
# def main(page: ft.Page):

#     labels_pathologies = [ft.TextField(label=f"Pathologie {i}") for i in range(1, 6)]
#     bouton_validation = ft.ElevatedButton(
#         text="Validation", 
#         on_click=lambda _: predire_maladie(' '.join([label.value for label in labels_pathologies])))
#     page.add(
#         ft.Column(
#             [
#                 ft.Text("Entrez jusqu'à 5 pathologies :"),
#                 *labels_pathologies,
#                 bouton_validation,
#             ],
#             spacing=10
#         )
#     )

# build_model()
# # Exécuter l'application Flet
# ft.app(target=main)
