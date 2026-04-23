import streamlit as st 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
import numpy as np
import base64

@st.cache_data
def load_data(dataset):
    df = pd.read_csv(dataset)
    return df

st.sidebar.image('./best_app/diabets.jpg',width=200)
def main():
    st.markdown("<h1 style='text-align:center;color: brown;'>Streamlit Diabetis App</h1>",unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center;color: black;'>Diabetis study in Cameroon</h2>",unsafe_allow_html=True)
    
    menu = ['Home','Analysis','Data Visualisation','Machine Learning']
    choice = st.sidebar.selectbox('Select Menu',menu)

    if choice == 'Home':
        left,middle,right = st.columns((2,3,2))
        with middle:
            st.image('téléchargement.jpeg',width=300)
        st.write("This is an app that will analyse diabetes Datas with some python tools that can optimize decisions")
        st.subheader('Diabetis Informations')
        st.write("In Cameroon, the prevalence of diabetes in adults in urban areas is currently estimated at 6 – 8%, with as much as 80% of people living with diabetes who are currently undiagnosed in the population. Further, according to data from Cameroon in 2002, only about a quarter of people with known diabetes actually had adequate control of their blood glucose levels. The burden of diabetes in Cameroon is not only high but is also rising rapidly. Data in Cameroonian adults based on three cross-sectional surveys over a 10-year period (1994–2004) showed an almost 10-fold increase in diabetes prevalence.")
    data = load_data('./best_app/data/diabetes.csv')
    if choice == 'Analysis':
        st.subheader('Diabetis Dataset')
        #data = load_data('./best_app/data/diabetes.csv')
        st.write(data.head())

        if st.checkbox('Summary'):
            st.write(data.describe())
        elif st.checkbox('Correlation'):
            fig = plt.figure(figsize=(15,15))
            st.write(sns.heatmap(data.corr(),annot=True))
            st.pyplot(fig)
    
    elif choice == 'Data Visualisation':
        if st.checkbox('Countplot'):
            fig = plt.figure(figsize=(5,5))
            sns.countplot(x='Age',data=data)
            st.pyplot(fig)

        elif st.checkbox('Scatterplot'):
            fig = plt.figure(figsize=(8,8))
            sns.scatterplot(x='Glucose',y='Age',data=data,hue='Outcome')
            st.pyplot(fig)
    
    elif choice == 'Machine Learning':
        tab1, tab2, tab3 = st.tabs([":clipboard: Data",":bar_chart:✅ Visualisation", ":mask: :smile: Prediction"])
        uploaded_file = st.sidebar.file_uploader('Upload your input CSV file',type=["csv"])
        if uploaded_file:
            df = load_data(uploaded_file)

            with tab1:
                st.subheader('loaded dataset')
                st.write(df)
            
            with tab2:
                st.subheader('Histogram Glucose')
                fig = plt.figure(figsize=(8,8))
                sns.histplot(x='Glucose',data=df)
                st.pyplot(fig)

            with tab3:
                model = pickle.load(open('./best_app/model_dump.pkl', 'rb'))
                #df.drop(['Outcome'],axis=1)
                prediction = model.predict(df)
                st.subheader('prediction')
                pp = pd.DataFrame(prediction,columns=['Prediction'])
                ndf = pd.concat([df,pp],axis=1)
                ndf.Prediction.replace(0,'No Diabete Risk',inplace=True)
                ndf.Prediction.replace(1,'Diabete Risk',inplace=True)
                st.write(ndf)

            

if __name__ == '__main__':
    main()
