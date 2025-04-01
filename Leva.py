import streamlit as st

# Título de la aplicación
st.title("Calculadora de Levadura para Cervecería")

# Ingreso del conteo de células vivas en la cámara de Neubauer (células por mL)
conteo_neubauer = st.number_input("Ingresa el conteo de células vivas en la cámara de Neubauer (células/mL):", min_value=0.0, step=1.0)

# Ingreso de la densidad en °P para calcular el pitch rate
densidad_P = st.number_input("Ingresa la densidad en °P de la cerveza (Grados Plato):", min_value=0.0, step=0.1)

# Ingreso del volumen de producción en litros
volumen_litros = st.number_input("Ingresa el volumen de cerveza a producir (L):", min_value=0.0, step=0.1)

# Definir el pitch rate según el tipo de cerveza (según grados Plato)
if densidad_P > 1060:
    # Pitch rate para cervezas con densidad mayor a 1060 (Lager con alta densidad o Ale con alta densidad)
    pitch_rate = 2 * densidad_P  # Para Lager o Ale con alta densidad
else:
    # Pitch rate para cervezas con densidad baja (Ale normal o Lager normal)
    pitch_rate = 1.5 * densidad_P  # Para cervezas normales

# Calcular las células necesarias (en billones)
m_celulas_ml = pitch_rate  # Millones de células por mL (pitch rate)
b_celulas = (m_celulas_ml * volumen_litros) / 1000  # Billones de células necesarias

# Cálculo de la cantidad de levadura necesaria (en litros)
# Utilizando el conteo de células para determinar el volumen necesario
volumen_levadura = b_celulas / (conteo_neubauer / 1e6)  # El conteo de células está en células/mL

# Calcular el peso de la levadura necesario, suponiendo que 150 mL pesan 90 g para levadura recuperada
peso_levadura = volumen_levadura * 0.6  # Se usa 0.6 porque 150 mL pesan 90g (90g/150mL = 0.6 g/mL)

# Mostrar los resultados
st.subheader("Resultados")
st.write(f"Billones de células necesarias: {b_celulas:.2f} B Células")
st.write(f"Volumen de levadura necesario: {volumen_levadura:.2f} L")
st.write(f"Peso estimado de levadura (kg): {peso_levadura:.2f} kg")

# Ejemplo de verificación de cálculo
st.subheader("Ejemplo de Cálculo")
# Parámetros del ejemplo:
volumen_litros_ejemplo = 100  # Volumen de producción (en litros)
conteo_neubauer_ejemplo = 1e6  # Conteo de células en la cámara de Neubauer (1 millón de células/mL)
densidad_P_ejemplo = 1046  # Densidad en °P de la cerveza (ejemplo: Golden Ale con 1046 °P)

# Cálculo para el ejemplo
pitch_rate_ejemplo = 1.5 * densidad_P_ejemplo if densidad_P_ejemplo <= 1060 else 2 * densidad_P_ejemplo
b_celulas_ejemplo = (pitch_rate_ejemplo * volumen_litros_ejemplo) / 1000
volumen_levadura_ejemplo = b_celulas_ejemplo / (conteo_neubauer_ejemplo / 1e6)
peso_levadura_ejemplo = volumen_levadura_ejemplo * 0.6  # Peso estimado de levadura (en kg)

# Mostrar el cálculo de ejemplo
st.write(f"Para un volumen de producción de {volumen_litros_ejemplo} L,")
st.write(f"con un conteo de {conteo_neubauer_ejemplo} células/mL y una densidad de {densidad_P_ejemplo} °P:")
st.write(f"Billones de células necesarias: {b_celulas_ejemplo:.2f} B Células")
st.write(f"Volumen de levadura necesario: {volumen_levadura_ejemplo:.2f} L")
st.write(f"Peso estimado de levadura: {peso_levadura_ejemplo:.2f} kg")
