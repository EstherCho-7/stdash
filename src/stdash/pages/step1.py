import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import requests

st.markdown("# STEP 1 / Request time and Prediction time 😊")
st.sidebar.markdown("# STEP 1 / Request time and Predicition time 😊")

def load_data():
    url='http://43.202.66.118:8015/all'
    r=requests.get(url, timeout=10)
    d=r.json()
    return d

data=load_data()
df=pd.DataFrame(data)

df['request_time']=pd.to_datetime(df['request_time'])
df['re_formatted_time']=df['request_time'].dt.strftime('%Y-%m-%d %H')
requestt=df.groupby('re_formatted_time').size()

df['prediction_time']=pd.to_datetime(df['prediction_time'])
df['pre_formatted_time']=df['prediction_time'].dt.strftime('%Y-%m-%d %H')
predictiont=df.groupby('pre_formatted_time').size()

plt.figure(figsize=(12, 6))
plt.plot(predictiont.index, predictiont.values, marker="^", label='request_time', color="black")
plt.bar(requestt.index, requestt.values, width=0.4, label='request', color='blue', align='center')

plt.title('Request and Prediction Counts over Time')
plt.xlabel('time')
plt.xticks(rotation=45)
plt.ylabel('count')

st.pyplot(plt)
