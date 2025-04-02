import os
import base64
import streamlit as st

def calcular_volumen_levadura(conteo_neubauer, pitch_rate, volumen_lote, densidad):
    """
    Calcula el volumen de levadura necesario en litros, basado en el conteo de células, 
    el pitch rate y el volumen del lote.
    """
    if conteo_neubauer <= 0 or pitch_rate <= 0 or volumen_lote <= 0 or densidad <= 0:
        st.error("⚠️ Los valores ingresados deben ser mayores a cero.")
        return None, None
    
    # Cálculo del total de células necesarias (en miles de millones)
    billones_celulas_necesarias = pitch_rate * volumen_lote
    
    # Cálculo del volumen de levadura necesario (L)
    volumen_levadura = billones_celulas_necesarias / (conteo_neubauer / 1000)  # Convertimos a billones/ml
    
    # Cálculo del peso de levadura necesario (kg)
    peso_levadura = volumen_levadura * densidad  # En kg, ya que densidad es g/mL y volumen en L
    
    return volumen_levadura, peso_levadura

st.title("🍺 Cálculo de Levadura para Inoculación de Cerveza CASTIZA")
st.subheader("📊 Calcula el volumen y peso de levadura necesario")

# Selección de estilo de cerveza
estilo = st.selectbox("🎨 Selecciona el estilo de cerveza:", ["Golden Ale 1046", "Blonde Ale Maracuyá 1046", "Trigo 1049", 
                                                         "Vienna Lager 1049", "Session IPA 1045", "Amber Ale 1050", 
                                                         "Brown Ale Café 1055", "Sweet Stout 1057", "IPA 1059", 
                                                         "Barley Wine 1108", "Catharina Sour 1045", "Cold IPA 1054", 
                                                         "Imperial IPA 1094", "Gose 1045", "Imperial Stout 1123"])

densidades = {
    "Golden Ale 1046": 1046,
    "Blonde Ale Maracuyá 1046": 1046,
    "Trigo 1049": 1049,
    "Vienna Lager 1049": 1049,
    "Session IPA 1045": 1045,
    "Amber Ale 1050": 1050,
    "Brown Ale Café 1055": 1055,
    "Sweet Stout 1057": 1057,
    "IPA 1059": 1059,
    "Barley Wine 1108": 1108,
    "Catharina Sour 1045": 1045,
    "Cold IPA 1054": 1054,
    "Imperial IPA 1094": 1094,
    "Gose 1045": 1045,
    "Imperial Stout 1123": 1123
}

pitch_rates = {
    "Ale": 0.75, 
    "Lager": 1.5, 
    "Lager > 1058": 2.0
}

conteo_neubauer = st.number_input("🦠 Ingresa el conteo de células en la cámara de Neubauer (millones/mL):", min_value=0.0, step=0.1)
volumen_lote = st.number_input("📏 Ingresa el volumen de lote (L):", min_value=1.0, step=0.1)
peso_200ml = st.number_input("⚖️ Pesa 200 mL de muestra de levadura en gramos e ingresa el valor aquí:", min_value=0.0, step=0.1)

densidad = peso_200ml / 200 if peso_200ml > 0 else 0
grados_plato = densidades[estilo]
pitch_rate_selected = pitch_rates["Lager > 1058"] if grados_plato > 1058 else pitch_rates["Ale"]

if conteo_neubauer > 0 and densidad > 0:
    volumen_levadura, peso_levadura = calcular_volumen_levadura(conteo_neubauer, pitch_rate_selected, volumen_lote, densidad)
    
    if volumen_levadura and peso_levadura:
        st.success("✅ Cálculo exitoso!")
        st.write(f"🎯 **Estilo de cerveza seleccionado:** {estilo}")
        st.write(f"📊 **Densidad de la cerveza:** {grados_plato}")
        st.write(f"🧪 **Pitch Rate seleccionado:** {pitch_rate_selected} M Células/mL °P")
        st.write(f"⚗️ **Volumen de levadura necesario:** {volumen_levadura:.3f} L")
        st.write(f"⚖️ **Peso estimado de levadura necesario:** {peso_levadura:.3f} kg")
else:
    st.warning("🔍 Ingresa todos los valores correctamente para obtener el cálculo.")
