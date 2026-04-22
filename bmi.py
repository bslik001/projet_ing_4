import streamlit as st
st.title("Welcome to the BMI Calculator")

weight = st.number_input('Enter your weight in kg')
status = st.radio('Enter your height in cm:',('cms','meters','feet'))

try:

    if status == 'cms':
       height = st.number_input('cms')
       bmi = weight / (height/100)**2
    elif status == 'meters':
        height = st.number_input('meters')
        bmi = weight / height**2
    elif status == 'feet':
        height = st.number_input('feet')
        bmi = weight / (height/3.2808)**2

except:
    print ("zero erreur ")

if(st.button('Calculate BMI')):
    st.write('Your BMI is {}'.format(round(bmi,2)))
    if bmi < 16 :
        st.error('You are extremely underweight')
    elif bmi >= 16 and bmi < 18.5:
        st.warning('You are underweight')
    elif bmi >= 18.5 and bmi < 25:
        st.success('You are healthy')
    else:
        st.error('You are overweight')  
    st.balloons()
