import streamlit as st

# Título de la aplicación
st.title("Calculadora de Levadura para Cervecería")

# Selección del tipo de levadura
levadura = st.selectbox(
    "Selecciona el tipo de levadura:",
    ["Levadura Recuperada", "Levadura Propagada"]
)

# Ingreso del peso de 200 mL de muestra en gramos
peso_muestra = st.number_input("Ingresa el peso de 200 mL de muestra (g):", min_value=0.0, step=0.1)

# Si el peso de la muestra es ingresado, calcular la densidad
if peso_muestra >_
