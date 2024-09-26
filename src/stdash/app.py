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

# TODO
# request_time, prediction_time 이용하여 '%Y-%m-%d %H' 형식
# 즉, 시간별 GROUP BY COUNT하여 matplotlib 차트 그려보기

#df['request_time']=pd.to_datetime()
#df['request_time'].dt.strftime('%Y-%m-%d %H')
#df.groupby('').size()

#plt.bar()
#plt.plot()
#plt.xlabel()

#화면에 그리기
#st.pyplot(plt)

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
