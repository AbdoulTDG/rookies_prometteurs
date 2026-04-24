# api.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Chargement du modèle
model = joblib.load("xgb_final.pkl")

# Colonnes dans l’ordre exact
FEATURES = [
    "GP", "OREB", "FG%", "3P%", "FTM", 
    "FGM", "BLK", "FT%", "PTS", "MIN", "REB"
]

app = FastAPI(title="NBA Potential Predictor API")

# Format des données reçues
class Player(BaseModel):
    GP: float
    OREB: float
    FG_percent: float
    TP_percent: float
    FTM: float
    FGM: float
    BLK: float
    FT_percent: float
    PTS: float
    MIN: float
    REB: float

@app.post("/predict")
def predict(player: Player):

    # Transformer en matrice pour le modèle
    x = np.array([[
        player.GP,
        player.OREB,
        player.FG_percent,
        player.TP_percent,
        player.FTM,
        player.FGM,
        player.BLK,
        player.FT_percent,
        player.PTS,
        player.MIN,
        player.REB
    ]])

    # Prédiction
    proba = model.predict_proba(x)[0][1]
    label = int(proba >= 0.5)

    return {
        "probability": float(proba),
        "promising": label
    }
