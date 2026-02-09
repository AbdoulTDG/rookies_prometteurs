# Objectif du projet

L’objectif principal de ce projet est de développer un modèle de Machine Learning capable de prédire si un joueur NBA a une forte probabilité de durer plus de 5 ans dans la ligue.
Cette prédiction permettrait aux investisseurs d’identifier des profils prometteurs tôt dans leur carrière, afin de miser sur des talents à fort potentiel de longévité.
Le dataset fourni contient les statistiques individuelles des joueurs, ainsi qu’un label binaire indiquant si leur carrière a dépassé ou non 5 saisons.

# Modèle Final & Résultats
Après une phase complète d’exploration, de feature engineering, de sélection de variables (via SHAP) et de comparaison de plusieurs algorithmes (Logistic Regression, Random Forest, XGBoost), le modèle retenu est le XGBoost avec 11 features sélectionnées.
Ce modèle offre un excellent compromis entre performance, simplicité et interprétabilité.

# Performances du modèle final :
    • Recall (classe “prometteur”) : 0.90
    • ROC-AUC : 0.77
    • Exactitude (accuracy) : 0.74
Ce recall élevé est cohérent avec le besoin métier qui est de maximiser la détection des joueurs ayant réellement un potentiel élevé.
Le modèle final est enregistré au format xgb_final.pkl et utilisé dans l’API.

# Architecture logicielle
Le projet comprend :
    • Un notebook complet (best_rookies.ipynb) retraçant toute l’analyse et le développement du modèle
    • Le dataset (nba_logreg.csv)
    • Les packages nécessaires au déploiement de l’API (requirements_api.txt) et de l’interface Streamlit (requirements_ui.txt)
    • Les packages nécessaire pour l’entraînement du modèle (requirements.txt)
    • Une API FastAPI (api_nba.py) permettant d'appeler le modèle via une requête JSON
    • Une interface utilisateur Streamlit (app_nba.py) permettant de tester la prédiction facilement
    • Une dockerisation complète (API + UI) pour une exécution locale ou future mise en production
        ◦ dockerfile.api : contient les informations de l’image de l’API contenant le modèle
        ◦ dockerfile.ui : contient les informations de l’image de l’interface streamlit
        ◦ docker-compose.yml : contient les instructions de construction et de déploiement des services. 

# Comment lancer l’application locale (Docker Compose)
Tout le projet est dockerisé afin de simplifier le déploiement.
Deux conteneurs sont créés :
    • nba-api : API FastAPI qui charge le modèle
    • nba-ui : Interface Streamlit qui communique avec l’API
1) Prérequis
Avoir Docker et Docker Compose installés.
2) Lancement de l’application
Dans le répertoire du projet, exécuter : docker-compose up --build

# Accéder aux services
    • Interface Streamlit : http://localhost:8001
    • Documentation API (Swagger) : http://localhost:8000/docs
L'interface  permet de renseigner les statistiques d’un joueur et d’obtenir une prédiction de si le joueur a une longévité supérieure à 5 ans ou pas. 
