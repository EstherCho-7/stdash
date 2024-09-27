import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests

st.title('CNN JOB MON')

def load_data():
    url='http://43.202.66.118:8015/all'
    r=requests.get(url)
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
plt.bar(requestt.index, requestt.values, width=0.4, label='request', color='blue', align='center')
plt.plot(predictiont.index, predictiont.values, marker='^', label='predicton', color='red')

plt.title('Request and Prediction Counts over Time')
plt.xlabel('time')
plt.ylabel('count')

st.pyplot(plt)

df['request_user']=df['request_user'].astype(str)
requestu=df.groupby('request_user').size()

df['prediction_model']=df['prediction_model'].astype(str)
predictionm=df.groupby('prediction_model').size()


plt.figure(figsize=(16, 8))
plt.bar(requestu.index, requestu.values, width=0.4, label='request', color='blue', align='center')
plt.bar(predictionm.index, predictionm.values, width=0.4, label='predicton', color='red', align="edge")

plt.title('Request user(BLUE) and Prediction(RED) Counts over Time')
plt.xlabel('time')
plt.ylabel('count')

st.pyplot(plt)
