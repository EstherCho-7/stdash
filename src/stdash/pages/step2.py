import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import requests

st.markdown("# STEP 2 😍")
st.sidebar.markdown("# STEP 2 😍")

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


plt.figure(figsize=(16, 8))
plt.bar(requestu.index, requestu.values, width=0.4, label='request', color='blue', align='center')
plt.bar(predictionm.index, predictionm.values, width=0.4, label='predicton', color='red', align="edge")

plt.title('Request user(BLUE) and Prediction(RED) Counts')
plt.xlabel('time')
plt.xticks(rotation=45)
plt.ylabel('count')

st.pyplot(plt)
