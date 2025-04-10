import os
import base64
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Función para calcular el volumen de levadura necesario
def calcular_volumen_levadura(conteo_neubauer, pitch_rate, volumen_lote, gravedad_especifica):
    """
    Calcula el volumen de levadura necesario en litros, basado en el conteo de células, el pitch rate, 
    el volumen del lote y la densidad convertida a grados Plato.
    """
    if conteo_neubauer <= 0 or pitch_rate <= 0 or volumen_lote <= 0:
        st.error("⚠️ Los valores de conteo de células, pitch rate o volumen de lote no pueden ser cero o negativos.")
        return None
    
    # Convertir gravedad específica a grados Plato
    grados_plato = (259 - (259 / gravedad_especifica))
    
    # Calcular billones de células necesarias (pitch_rate * volumen_lote * °P)
    billones_celulas = pitch_rate * volumen_lote * grados_plato
    
    # Calcular el volumen de levadura necesario (en litros)
    volumen_levadura = billones_celulas / conteo_neubauer
    return volumen_levadura

# Función para calcular el peso de levadura necesario
def calcular_peso_levadura(volumen_levadura, densidad):
    """
    Calcula el peso de levadura necesario en kilogramos, dado el volumen y la densidad de la levadura.
    """
    if volumen_levadura <= 0 or densidad <= 0:
        return 0  # Si el volumen o densidad son inválidos, retorna 0
    
    # El peso se calcula multiplicando el volumen por la densidad (en g/ml) y luego convirtiendo a kilogramos
    peso_levadura = volumen_levadura * 1000 * densidad  # 1 L = 1000 mL
    return peso_levadura / 1000  # Convertir gramos a kilogramos

# Verifica si el archivo de imagen existe
if os.path.exists("background.jpg"):
    with open("background.jpg", "rb") as img:
        encoded = base64.b64encode(img.read()).decode()
    
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
        html, body, [class*="st"] {{
            font-family: 'Roboto', sans-serif;
            color: #fff3aa;
        }}
        .stApp {{
            background-image: url('data:image/jpeg;base64,{encoded}');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        .stTextInput > div > div > input,
        .stSelectbox > div > div,
        .stTextArea > div > textarea {{
            background-color: #ffffff10 !important;
            color: #fff3aa !important;
            border-radius: 10px;
        }}
        .stButton > button {{
            background-color: #55dcad !important;
            color: #fff3aa !important;
            border: none;
            border-radius: 10px;
            font-weight: bold;
        }}
        .stDataFrame, .stTable {{
            background-color: rgba(0,0,0,0.6);
            border-radius: 10px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.warning("⚠️ No se encontró la imagen de fondo. Asegúrate de que 'background.jpg' esté en la carpeta correcta.")

# Título de la aplicación con estilo
st.title("🧫 Cálculo de Levadura para Inoculación de Lote de Cerveza  CASTIZA 🍺")
st.subheader("📊 Calcula el volumen y peso de levadura necesario para tu cerveza")

# Selección de estilo de cerveza
estilo = st.selectbox("🎨 Selecciona el estilo de cerveza:", [
    "Golden Ale 1046", "Blonde Ale Maracuyá 1046", "Trigo 1049", "Vienna Lager 1049", 
    "Session IPA 1045", "Amber Ale 1050", "Brown Ale Café 1055", "Sweet Stout 1057", 
    "IPA 1059", "Barley Wine 1108", "Catharina Sour 1045", "Cold IPA 1054", 
    "Imperial IPA 1094", "Gose 1045", "Imperial Stout 1123"])

# Densidades para los estilos (convertidas a gravedad específica)
densidades = {
    "Golden Ale 1046": 1.046,
    "Blonde Ale Maracuyá 1046": 1.046,
    "Trigo 1049": 1.049,
    "Vienna Lager 1049": 1.049,
    "Session IPA 1045": 1.045,
    "Amber Ale 1050": 1.050,
    "Brown Ale Café 1055": 1.055,
    "Sweet Stout 1057": 1.057,
    "IPA 1059": 1.059,
    "Barley Wine 1108": 1.108,
    "Catharina Sour 1045": 1.045,
    "Cold IPA 1054": 1.054,
    "Imperial IPA 1094": 1.094,
    "Gose 1045": 1.045,
    "Imperial Stout 1123": 1.123
}

# Pitch rates
pitch_rates = {"Ale": 0.75, "Lager": 1.5, "Lager > 1058": 2.0}

conteo_neubauer = st.number_input("🔬 Ingresa el conteo de células (M Células/mL 1e6):", min_value=0.0, step=0.1)
volumen_lote = st.number_input("🛢️🍺 Ingresa el volumen de lote (L):", min_value=1.0, step=0.1)
peso_200ml = st.number_input("⚖️ Pesa 200 mL de muestra de levadura (g):", min_value=0.0, step=0.1)

densidad = peso_200ml / 200 if peso_200ml > 0 else 0
gravedad_especifica = densidades[estilo]
pitch_rate_selected = pitch_rates["Lager > 1058"] if gravedad_especifica > 1.058 else pitch_rates["Ale"]

if conteo_neubauer > 0:
    volumen_levadura = calcular_volumen_levadura(conteo_neubauer, pitch_rate_selected, volumen_lote, gravedad_especifica)
    peso_levadura = calcular_peso_levadura(volumen_levadura, densidad) if densidad > 0 else 0
    
    st.success(f"✅🧪 Volumen de levadura necesario: {volumen_levadura:.4f} L")
    st.success(f"✅🧪 Peso estimado de levadura necesario: {peso_levadura:.4f} kg")
else:
    st.error("⚠️ El conteo de células no puede ser cero.")


####


# Función para calcular el volumen de levadura necesario
def calcular_volumen_levadura(conteo_neubauer, pitch_rate, volumen_lote, gravedad_especifica):
    if conteo_neubauer <= 0 or pitch_rate <= 0 or volumen_lote <= 0:
        st.error("⚠️ Los valores de conteo de células, pitch rate o volumen de lote no pueden ser cero o negativos.")
        return None
    
    grados_plato = (259 - (259 / gravedad_especifica))
    billones_celulas = pitch_rate * volumen_lote * grados_plato
    volumen_levadura = billones_celulas / conteo_neubauer
    return volumen_levadura

# Función para calcular el peso de levadura necesario
def calcular_peso_levadura(volumen_levadura, densidad):
    if volumen_levadura <= 0 or densidad <= 0:
        return 0  
    peso_levadura = volumen_levadura * 1000 * densidad  
    return peso_levadura / 1000  

# Datos de densidades y pitch rates
densidades = {
    "Golden Ale 1046": 1.046,
    "Blonde Ale Maracuyá 1046": 1.046,
    "Trigo 1049": 1.049,
    "Vienna Lager 1049": 1.049,
    "Session IPA 1045": 1.045,
    "Amber Ale 1050": 1.050,
    "Brown Ale Café 1055": 1.055,
    "Sweet Stout 1057": 1.057,
    "IPA 1059": 1.059,
    "Barley Wine 1108": 1.108,
    "Catharina Sour 1045": 1.045,
    "Cold IPA 1054": 1.054,
    "Imperial IPA 1094": 1.094,
    "Gose 1045": 1.045,
    "Imperial Stout 1123": 1.123
}

pitch_rates = {"Ale": 0.75, "Lager": 1.5, "Lager > 1058": 2.0}

# Configuración de Streamlit
st.title("🍺 Cálculo y Propagación de Levadura")
st.subheader("📊 Calcula el volumen, peso y crecimiento de levadura en tu cervecería")

# Selección de parámetros
fecha_inicio = st.date_input("📅 Fecha de inicio de propagación")
estilo = st.selectbox("🎨 Estilo de cerveza", list(densidades.keys()))
tipo_levadura = st.selectbox("🧫 Tipo de levadura", [
    "US-05 Fermentis", "S-04 Fermentis", "Star Party Omega Yeast", 
    "German Lager Omega Yeast", "Hornindal Kviek Omega Yeast", 
    "West Coast I DKO", "W-3470 Fermentis"])
volumen_lote = st.number_input("🛢️ Volumen de cerveza a fermentar (L)", min_value=1.0, step=0.1)
conteo_neubauer = st.number_input("🔬 Conteo de células inicial (M Células/mL)", min_value=0.0, step=0.1)
peso_200ml = st.number_input("⚖️ Pesa 200 mL de levadura (g)", min_value=0.0, step=0.1)

densidad = peso_200ml / 200 if peso_200ml > 0 else 0
gravedad_especifica = densidades[estilo]
pitch_rate_selected = pitch_rates["Lager > 1058"] if gravedad_especifica > 1.058 else pitch_rates["Ale"]

# Cálculo de levadura
if conteo_neubauer > 0:
    volumen_levadura = calcular_volumen_levadura(conteo_neubauer, pitch_rate_selected, volumen_lote, gravedad_especifica)
    peso_levadura = calcular_peso_levadura(volumen_levadura, densidad) if densidad > 0 else 0
    st.success(f"✅ Volumen de levadura necesario: {volumen_levadura:.4f} L")
    st.success(f"✅ Peso estimado de levadura necesario: {peso_levadura:.4f} kg")
else:
    st.error("⚠️ El conteo de células no puede ser cero.")

# Propagación de levadura
pasos = [
    ("📌 Paso 1", "Erlenmeyer 250mL (60mL mosto)", 60, 0.25),
    ("📌 Paso 2", "Erlenmeyer 500mL (400mL mosto)", 400, 0.5),
    ("📌 Paso 3", "Erlenmeyer 5L (2L mosto)", 2000, 5),
    ("📌 Paso 4", "Propagador 50L (12L mosto)", 12000, 50),
    ("📌 Paso 5", "Propagador 50L (40L mosto)", 28000, 50)
]

dias = []
celulas = []
for i, (nombre, equipo, volumen, capacidad) in enumerate(pasos):
    st.subheader(f"{nombre} - {equipo}")
    conteo = st.number_input(f"🔬 Ingresa conteo celular en {equipo} (M Células/mL)", min_value=0.0, step=0.1, key=f"conteo_{i}")
    dias.append(i)
    celulas.append(conteo)

df = pd.DataFrame({"Día": dias, "Millones de Células": celulas})

# Gráfico de propagación
st.subheader("📈 Crecimiento Celular en Propagación")
fig, ax = plt.subplots()
ax.plot(df["Día"], df["Millones de Células"], marker='o', linestyle='-', color='orange')
ax.set_xlabel("Días")
ax.set_ylabel("Millones de Células")
ax.set_title("Evolución de la Propagación")
ax.grid()
st.pyplot(fig)





