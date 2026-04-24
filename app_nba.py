# app.py
import streamlit as st
import requests

import streamlit as st
import requests
import os

# On lit l'URL de l'API depuis une variable d'environnement
API_URL = os.getenv("API_URL", "http://localhost:8000/predict")

st.title("Prédiction des joeurs prometteurs en NBA")
# st.write("L'application interroge une API FastAPI qui contient le modèle XGBoost.")

# Formulaire dans Streamlit
st.subheader("Entrer les statistiques du joueur")

col1, col2 = st.columns(2)

with col1:
    GP = st.number_input("GP", 0, 100, 60)
    OREB = st.number_input("OREB", 0.0, 10.0, 1.0)
    FG_percent = st.number_input("FG%", 0.0, 100.0, 45.0)
    TP_percent = st.number_input("3P%", 0.0, 100.0, 35.0)
    FTM = st.number_input("FTM", 0.0, 10.0, 2.0)

with col2:
    FGM = st.number_input("FGM", 0.0, 15.0, 3.0)
    BLK = st.number_input("BLK", 0.0, 5.0, 0.5)
    FT_percent = st.number_input("FT%", 0.0, 100.0, 75.0)
    PTS = st.number_input("PTS", 0.0, 40.0, 10.0)
    MIN = st.number_input("MIN", 0.0, 48.0, 20.0)

REB = st.number_input("REB total", 0.0, 20.0, 5.0)

if st.button("Prédiction"):
    payload = {
        "GP": GP,
        "OREB": OREB,
        "FG_percent": FG_percent,
        "TP_percent": TP_percent,
        "FTM": FTM,
        "FGM": FGM,
        "BLK": BLK,
        "FT_percent": FT_percent,
        "PTS": PTS,
        "MIN": MIN,
        "REB": REB
    }

    response = requests.post(API_URL, json=payload)

    if response.status_code == 200:
        result = response.json()
        proba = result["probability"]
        promising = result["promising"]

        st.subheader("Résultat :")
        if promising == 1:
            st.success(f"Joueur prometteur ! Probabilité : {proba:.2f}")
        else:
            st.error(f"Joueur NON prometteur. Probabilité : {proba:.2f}")
    else:
        st.error("Erreur lors de la connexion à l'API.")
