# 🎓 Projet ING 4 — Collection de Mini-Applications Python

> Projet réalisé dans le cadre de la 4ème année d’ingénierie. Ce dépôt regroupe plusieurs mini-applications Python couvrant des domaines variés : santé, finance et data science.

-----

## 📁 Structure du projet

```
projet_ing_4/
├── best_app/             # Application principale / vitrine
├── dashboard/            # Tableau de bord de visualisation de données
├── india_ka/             # Application dédiée à des données indiennes
├── prediction_medicale/  # Prédiction médicale par machine learning
├── stock_forecast_app/   # Prévision de cours boursiers
└── bmi.py                # Calculateur d'IMC (Indice de Masse Corporelle)
```

-----

## 🚀 Modules

### 🏥 `prediction_medicale/`

Application de prédiction médicale basée sur des algorithmes de machine learning.

- Analyse de données médicales
- Modèle de classification / régression
- Visualisation des résultats

### 📈 `stock_forecast_app/`

Application de prévision de cours boursiers.

- Récupération de données financières historiques
- Modèle de prévision (séries temporelles)
- Visualisation des tendances et prédictions

### 📊 `dashboard/`

Tableau de bord interactif pour la visualisation de données.

- Interface graphique de synthèse
- Graphiques et indicateurs clés

### 🌏 `india_ka/`

Module dédié à l’analyse de données en lien avec le marché ou les données indiennes.

### ⭐ `best_app/`

Application principale ou point d’entrée du projet.

### ⚖️ `bmi.py`

Script simple de calcul de l’Indice de Masse Corporelle (IMC).

- Saisie du poids et de la taille
- Calcul et interprétation de l’IMC

-----

## 🛠️ Technologies utilisées

- **Langage :** Python 3.x
- **Librairies probables :** `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `streamlit` / `dash`, `yfinance`

-----

## ⚙️ Installation

```bash
# Cloner le dépôt
git clone https://github.com/bslik001/projet_ing_4.git
cd projet_ing_4

# (Recommandé) Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Windows : venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt
```

> ⚠️ Si aucun `requirements.txt` n’est présent, installez les dépendances manuellement selon le module utilisé.

-----

## ▶️ Utilisation

### Lancer le calculateur IMC

```bash
python bmi.py
```

### Lancer une application spécifique

```bash
cd stock_forecast_app
streamlit run app.py
# ou
python main.py
```

> Référez-vous au dossier de chaque module pour des instructions spécifiques.

-----

## 👤 Auteur

- **bslik001** — [GitHub](https://github.com/bslik001)

-----

## 📄 Licence

Ce projet est réalisé dans un cadre académique. Aucune licence commerciale n’est associée.