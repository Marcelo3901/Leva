import streamlit as st

# Función para calcular el volumen de levadura necesario
def calcular_volumen_levadura(conteo_neubauer, pitch_rate, volumen_lote):
    if conteo_neubauer == 0:
        st.error("El conteo de células no puede ser cero. Por favor, ingresa un valor válido.")
        return 0  # Retorna 0 si el conteo es 0 para evitar la división por cero.
    billones_celulas = pitch_rate * volumen_lote / 1000  # Billones de células necesarias
    volumen_levadura = billones_celulas / conteo_neubauer  # Volumen necesario en litros
    return volumen_levadura

# Función para calcular el peso de la levadura a partir del volumen y la densidad
def calcular_peso_levadura(volumen_levadura, densidad):
    if volumen_levadura == 0:
        return 0  # Si el volumen de levadura es 0, retornamos 0 como peso
    # El volumen_levadura está en litros, convertir a mililitros (1L = 1000mL)
    volumen_levadura_ml = volumen_levadura * 1000
    # Calcular el peso en gramos: densidad (g/mL) * volumen (mL)
    peso_levadura_g = densidad * volumen_levadura_ml
    # Convertir gramos a kilogramos
    peso_levadura_kg = peso_levadura_g / 1000
    return peso_levadura_kg

# Título de la aplicación
st.title("Cálculo de Levadura para Inoculación de Lote de Cerveza")

# Selección de estilo de cerveza
estilo = st.selectbox("Selecciona el estilo de cerveza:", ["Golden Ale", "Blonde Ale Maracuyá", "Trigo", 
                                                         "Vienna Lager", "Session IPA", "Amber Ale", 
                                                         "Brown Ale Café", "Sweet Stout", "IPA", 
                                                         "Barley Wine", "Catharina Sour", "Cold IPA", 
                                                         "Imperial IPA", "Gose", "Imperial Stout"])

# Densidad de la cerveza en grados Plato para cada estilo
densidades = {
    "Golden Ale": 1046,
    "Blonde Ale Maracuyá": 1046,
    "Trigo": 1049,
    "Vienna Lager": 1049,
    "Session IPA": 1045,
    "Amber Ale": 1050,
    "Brown Ale Café": 1055,
    "Sweet Stout": 1057,
    "IPA": 1059,
    "Barley Wine": 1108,
    "Catharina Sour": 1045,
    "Cold IPA": 1054,
    "Imperial IPA": 1094,
    "Gose": 1045,
    "Imperial Stout": 1123
}

# Pitch rates
pitch_rates = {
    "Ale": 0.75, 
    "Lager": 1.5, 
    "Lager > 1060": 2.0
}

# Ingreso del conteo de células en la cámara de Neubauer (en millones de células/mL)
conteo_neubauer = st.number_input("Ingresa el conteo de células en la cámara de Neubauer (en M Células/mL):", min_value=0.0, step=0.1)

# Ingreso del volumen de lote de cerveza (en litros)
volumen_lote = st.number_input("Ingresa el volumen de lote (en litros):", min_value=1.0, step=0.1)

# Densidad experimental a través del peso de 200 mL de muestra
peso_200ml = st.number_input("Pesa 200 mL de muestra de levadura en gramos y entra el valor aquí:", min_value=0.0, step=0.1)

# Cálculo de la densidad
if peso_200ml > 0:
    densidad = peso_200ml / 200  # Densidad en g/mL
else:
    densidad = 0  # Si no se ha ingresado el peso, se muestra como 0

# Estilo de cerveza seleccionado
grados_plato = densidades[estilo]

# Determinación del pitch rate según el tipo de cerveza
if grados_plato > 1060:
    pitch_rate_selected = pitch_rates["Lager > 1060"]
else:
    pitch_rate_selected = pitch_rates["Ale"]

# Verificación de conteo de células antes de proceder
if conteo_neubauer == 0:
    st.error("El conteo de células no puede ser cero. Por favor, ingresa un valor válido.")
else:
    # Cálculo del volumen de levadura necesario
    volumen_levadura = calcular_volumen_levadura(conteo_neubauer, pitch_rate_selected, volumen_lote)

    # Cálculo del peso de levadura necesario
    if densidad > 0:
        peso_levadura = calcular_peso_levadura(volumen_levadura, densidad)
    else:
        peso_levadura = 0

    # Mostrar los resultados
    if volumen_levadura > 0:
        st.write(f"Estilo de cerveza seleccionado: {estilo}")
        st.write(f"Grados Plato de la cerveza: {grados_plato}")
        st.write(f"Pitch Rate seleccionado: {pitch_rate_selected} millones de células/mL °P")
        st.write(f"Volumen de levadura necesario: {volumen_levadura:.4f} L")
        st.write(f"Peso estimado de levadura necesario: {peso_levadura:.4f} kg")
    else:
        st.warning("Por favor, asegúrate de ingresar un conteo de células válido mayor que cero.")
