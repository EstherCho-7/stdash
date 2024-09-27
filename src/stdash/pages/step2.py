import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import requests

st.markdown("# STEP 2 / Request user and Prediction model 😍")
st.sidebar.markdown("# STEP 2 / Request user and Prediction model 😍")

def load_data():
    url='http://43.202.66.118:8015/all'
    r=requests.get(url, timeout=10)
    d=r.json()
    return d

data=load_data()
df=pd.DataFrame(data)

df['request_user']=df['request_user'].astype(str)
requestu=df.groupby('request_user').size()

df['prediction_model']=df['prediction_model'].astype(str)
predictionm=df.groupby('prediction_model').size()

st.bar_chart(requestu, x_label='request user', y_label='count', color='#02ccfe')
st.bar_chart(predictionm, x_label='prediction model', y_label='count', color='#fb6f92')
