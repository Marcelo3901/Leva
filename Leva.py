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
if peso_muestra > 0:  # Se corrigió el error aquí agregando ":" al final
    densidad = peso_muestra / 200  # Densidad en g/mL
    st.write(f"Densidad de la levadura: {densidad:.3f} g/mL")
else:
    densidad = 0

# Selección del volumen de producción en litros
volumen_litros = st.number_input("Ingresa el volumen de cerveza a producir (L):", min_value=0.0, step=0.1)

# Ingreso de la densidad en °P para calcular el pitch rate
densidad_P = st.number_input("Ingresa la densidad en °P de la cerveza (Grados Plato):", min_value=0.0, step=0.1)

# Cálculo del Pitch Rate en M células/mL
if levadura == "Levadura Recuperada":
    pitch_rate = 0.75 * densidad_P  # Pitch rate para levadura recuperada
else:
    if densidad_P > 1060:
        pitch_rate = 2 * densidad_P  # Pitch rate para levadura propagada (si densidad > 1060)
    else:
        pitch_rate = 1.5 * densidad_P  # Pitch rate para levadura propagada normal

# Cálculo de las células necesarias en billones
m_celulas_ml = pitch_rate  # Millones de células por mL (pitch rate)
b_celulas = (m_celulas_ml * volumen_litros) / 1000  # Billones de células necesarias

# Cálculo del volumen de levadura necesario
volumen_levadura = b_celulas / densidad if densidad > 0 else 0

# Cálculo del peso total de levadura necesario según tipo de levadura
if levadura == "Levadura Recuperada":
    peso_levadura = volumen_levadura * 0.6  # Para levadura recuperada
else:
    peso_levadura = volumen_levadura * 1.03  # Para levadura propagada

# Mostrar resultados
st.subheader("Resultados")
st.write(f"Billones de células necesarias: {b_celulas:.2f} B Células")
st.write(f"Volumen de levadura necesario: {volumen_levadura:.2f} L")
st.write(f"Peso estimado de levadura (kg): {peso_levadura:.2f} kg")
