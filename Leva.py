import streamlit as st
from PIL import Image

# Cargar la imagen de fondo
image = Image.open('background.jpg')

# Personalización de los estilos CSS
st.markdown(
    """
    <style>
        body {
            background-image: url('background.jpg');
            background-size: cover;
            background-position: center;
            color: white;
            font-family: 'Arial', sans-serif;
        }
        .css-1y4h6k4 {
            background-color: rgba(0, 0, 0, 0.5);
        }
        .css-1a4ffcx {
            background-color: rgba(0, 0, 0, 0.6);
            border-radius: 8px;
        }
        h1 {
            color: #ffcc00;
        }
        .stButton>button {
            background-color: #ff6600;
            color: white;
            border-radius: 8px;
        }
        .stTextInput>div>input {
            background-color: #2c3e50;
            color: white;
            border-radius: 4px;
        }
        .stSelectbox>div>div>input {
            background-color: #2c3e50;
            color: white;
            border-radius: 4px;
        }
    </style>
    """, unsafe_allow_html=True)

# Título de la aplicación con estilo
st.title("Cálculo de Levadura para Inoculación de Lote de Cerveza")

# Estilo dinámico con fondo y botones personalizados
st.subheader("Calcula el volumen y peso de levadura necesario para tu cerveza")

# Selección de estilo de cerveza
estilo = st.selectbox("Selecciona el estilo de cerveza:", ["Golden Ale", "Blonde Ale Maracuyá", "Trigo", 
                                                         "Vienna Lager", "Session IPA", "Amber Ale", 
                                                         "Brown Ale Café", "Sweet Stout", "IPA", 
                                                         "Barley Wine", "Catharina Sour", "Cold IPA", 
                                                         "Imperial IPA", "Gose", "Imperial Stout"])

# Densidades para los estilos
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
