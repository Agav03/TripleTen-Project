import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('/Users/angelgabrielalvarezvalenzuela/TripleTen-Project/vehicles_us.csv')

st.header('SPRINT 5 - DATA ANALYST PROJECT')

hist_price_button = st.button('Construir Histograma de Precio')

if hist_price_button:
    st.write('Procesando...') 
    fig_price = px.histogram(car_data, x="price")
    st.plotly_chart(fig_price, use_container_width=True)

hist_year_button = st.button('Construir Histograma de Año')

if hist_year_button:
    st.write('Procesando...') 
    fig_year = px.histogram(car_data, x="year")
    st.plotly_chart(fig_year, use_container_width=True)

scatter_price_year_button = st.button('Construir Gráfico de Dispersión de Precio vs Año')

if scatter_price_year_button:
    st.write('Procesando...') 
    fig_price_year = px.scatter(car_data, x="year", y="price")
    st.plotly_chart(fig_price_year, use_container_width=True)

scatter_price_odometer_button = st.button('Construir Gráfico de Dispersión de Precio vs Odómetro')

if scatter_price_odometer_button:
    st.write('Procesando...') 
    fig_price_odometer = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_price_odometer, use_container_width=True)
