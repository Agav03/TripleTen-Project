import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('/Users/angelgabrielalvarezvalenzuela/TripleTen-Project/vehicles_us.csv')

st.header('SPRINT 5 - DATA ANALYST PROJECT')
st.subheader('Creación de un histograma')

hist_button = st.button('Construir Histograma')

if hist_button:
    st.write('Procesando...') 
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

st.subheader('Creación de un gráfico de dispersión')

scatter_button = st.button('Construir Gráfico de Dispersión')

if scatter_button:
    st.write('Procesando...') 
    fig = px.scatter(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)