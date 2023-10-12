
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


file_path = 'PRSA_Data_20130301-20170228/PRSA_Data_Aotizhongxin_20130301-20170228.csv'
df = pd.read_csv(file_path)

df['Date'] = df['year'].astype(str) + '-' + df['month'].astype(str) + '-' + df['day'].astype(str)
df['Date'] = pd.to_datetime(df['Date'])

df.set_index(['Date'])
monthly_avg = df.groupby('month')[['PM2.5','PM10','SO2','NO2','O3']].mean()

summary = df.describe()
features = ['PM2.5','PM10','SO2','NO2','O3']
total_summary = []

for feat in features:
  total_summary.append(summary.loc["max",feat] - summary.loc["min",feat])
  

st.header('Dicoding Air Quality Dashboard :sparkles:')



st.title("Perubahan kualitas air berdasarkan PM2.5, PM10, SO2, NO2, dan O3")

fig, ax = plt.subplots(figsize=(30, 12))
ax.plot(monthly_avg.index, monthly_avg['PM2.5'], label='PM2.5')
ax.plot(monthly_avg.index, monthly_avg['PM10'], label='PM10')
ax.plot(monthly_avg.index, monthly_avg['SO2'], label='SO2')
ax.plot(monthly_avg.index, monthly_avg['NO2'], label='NO2')
ax.plot(monthly_avg.index, monthly_avg['O3'], label='O3')

ax.legend(loc='upper left')
ax.set_xlabel("Bulan")
ax.set_ylabel("Kualitas Udara")

st.pyplot(fig)

st.title("Perbedaan jumlah partikel selama 4 tahun")

fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(features, total_summary)

st.pyplot(fig)

