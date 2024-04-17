import streamlit as st
import pandas as pd
import numpy as np
import joblib

from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier(max_depth=10, min_samples_leaf=5, random_state=0)
model=joblib.load('finalized_model.joblib')
@st.cache

def predict(Buying,Maint,Doors,Persons,Lug_boot,Safety):
  if Safety=='med':
    safety=1
  elif Safety=='high':
    safety=2
   elif Safety=='low':
      safety=3
df=pd.DataFrame([[Buying,Maint,Doors,Persons,Lug_boot,Safety]],
  columns=['Buying','Maint','Doors','Persons','Lug_boot','Safety'])
prediction=model.predict([[Buying,Maint,Doors,Persons,Lug_boot,Safety]])
return prediction

st.title("Harsha's Car Evaluation Classification")
st.image("""https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.shutterstock.com%2Fsearch%2Fprogramming&psig=AOvVaw2PVQmQ4EHcEjsVOI9XAHHU&ust=1713420172045000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCMCus9fJyIUDFQAAAAAdAAAAABAE""")
st.header("Enter the Information of the car")
st.text("vhigh=1 high=2 med=3 low=4")
Buying =st.number_input('buying',min_value=1,max_value=4,value=1)
st.text("vhigh=1 high=2 med=3 low=4")
Maint=st.number_input('maint:',min_value=1,max_value=1,value=1)
st.text("2-Doors=1 3-Doors=2 4-Doors=3 5more=4")
Doors=st.number_input('doors:',min_value=1,max_value=1,value=1)
st.text("2-persons=1 4-persons=2 more=3")
Persons=st.number_input('persons:',min_value=1,max_value=1,value=1)
st.text("small=1 med=2 big=3")
Lug_boot=st.number_input('lug_boot:',min_value=1,max_value=1,value=1)
Safety=st.radio('safety:',('med','high','low'))

if st.button('Submit_Car_Infos'):
  cal_eval=predict(Buying,Maint,Doors,Persons,Lub_boot,Safety)
  st.success(f'The Evaluation of Car:{cal_eval[0]}')
