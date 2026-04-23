import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
import time
import pickle
#chargement
with open('./prediction_medicale/reg.pkl','rb') as file:
    model = pickle.load(file)


#Titre et mise en page
st.set_page_config(page_title="Predicteur de charges Medicales")
st.title("Prediction de charges medicales")
st.markdown("Remplir les informations ci-dssous pour predire les charges medicales")

# ajout d'animation

with st.spinner('Chargement du modèle...'):
    time.sleep(1)  # Simulate loading time

#Entrees utilisateur
col1,col2= st.columns(2)
with col1:
    age = st.slider("'Age", 18, 100, 30)

with col2:
    sex = st.selectbox("Sexe", ["Masculin", "Feminin"])

col3,col4 = st.columns(2)
with col3:
    bmi = st.number_input('BMI(Indice de masse corporelle)',10,50,25)

with col4:
    sex = st.slider("Nombre d'enfants à charge", 0, 5, 1)

col5,col6 = st.columns(2)
with col5:
    smoker = st.selectbox("Fumeur", ["Oui", "Non"])

with col6:
    region = st.selectbox("Region", ["Nord-Est", "Nord-Ouest", "Sud-Est", "Sud-Ouest"])

#eNCODAGE

sex_encoded = 1 if sex == 'male' else 0
smoker_encoded = 1 if smoker == "yes" else 0
region_dict = {"Nord-Est":0.24308153 , "Nord-Ouest":0.24442709 , "Sud-Est":0.24677265 , "Sud-Ouest":0.26569973}
region_encoded = region_dict[region]




#Preparation des données
input_data = [[age, sex_encoded, bmi, sex, smoker_encoded, region_encoded]]

#prediction
if st.button('Prediction des charges medicales'):
    with st.spinner("Calcul en cours ....."):
        prediction = model.predict(input_data)
        time.sleep(1)
    st.success("Prediction terminée")
    st.markdown(f"#### chares medicales Estimees:  **${prediction:,.2f}**")
    st.balloons()
