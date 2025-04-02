import os
import base64
import streamlit as st

# Función para calcular el volumen de levadura necesario
def calcular_volumen_levadura(conteo_neubauer, pitch_rate, volumen_lote):
    if conteo_neubauer <= 0 or pitch_rate <= 0 or volumen_lote <= 0:
        st.error("⚠️ Los valores de conteo de células, pitch rate o volumen de lote no pueden ser cero o negativos.")
        return None
    billones_celulas = pitch_rate * volumen_lote
    volumen_levadura = billones_celulas / (conteo_neubauer * 1e6)  # Conversión adecuada
    return volumen_levadura

# Función para calcular el peso de levadura necesario
def calcular_peso_levadura(volumen_levadura, densidad):
    if volumen_levadura <= 0 or densidad <= 0:
        return 0
    peso_levadura = volumen_levadura * 1000 * densidad
    return peso_levadura / 1000  # Convertir gramos a kilogramos

# Configuración de fondo
if os.path.exists("background.jpg"):
    with open("background.jpg", "rb") as img:
        encoded = base64.b64encode(img.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url('data:image/jpeg;base64,{encoded}');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.warning("⚠️ No se encontró la imagen de fondo. Asegúrate de que 'background.jpg' esté en la carpeta correcta.")

# Título principal
st.title("🍺 Cálculo de Levadura para Inoculación de Lote")
st.subheader("📌 Calcula el volumen y peso de levadura necesario para tu cerveza")

# Selección de estilo de cerveza
estilo = st.selectbox("🎨 Selecciona el estilo de cerveza:", [
    "Golden Ale 1046", "Blonde Ale Maracuyá 1046", "Trigo 1049", "Vienna Lager 1049",
    "Session IPA 1045", "Amber Ale 1050", "Brown Ale Café 1055", "Sweet Stout 1057",
    "IPA 1059", "Barley Wine 1108", "Catharina Sour 1045", "Cold IPA 1054",
    "Imperial IPA 1094", "Gose 1045", "Imperial Stout 1123"
])

# Densidades
pitch_rates = {"Ale": 0.75, "Lager": 1.5, "Lager > 1060": 2.0}

densidades = {
    "Golden Ale 1046": 1046, "Blonde Ale Maracuyá 1046": 1046, "Trigo 1049": 1049,
    "Vienna Lager 1049": 1049, "Session IPA 1045": 1045, "Amber Ale 1050": 1050,
    "Brown Ale Café 1055": 1055, "Sweet Stout 1057": 1057, "IPA 1059": 1059,
    "Barley Wine 1108": 1108, "Catharina Sour 1045": 1045, "Cold IPA 1054": 1054,
    "Imperial IPA 1094": 1094, "Gose 1045": 1045, "Imperial Stout 1123": 1123
}

grados_plato = densidades[estilo]
pitch_rate_selected = pitch_rates["Lager > 1060"] if grados_plato > 1060 else pitch_rates["Ale"]

# Entrada de datos
conteo_neubauer = st.number_input("🧫 Conteo de células (M Células/mL):", min_value=0.0, step=0.1)
volumen_lote = st.number_input("📦 Volumen del lote (L):", min_value=1.0, step=0.1)
peso_200ml = st.number_input("⚖️ Peso de 200mL de levadura (g):", min_value=0.0, step=0.1)

densidad = peso_200ml / 200 if peso_200ml > 0 else 0

if conteo_neubauer > 0:
    volumen_levadura = calcular_volumen_levadura(conteo_neubauer, pitch_rate_selected, volumen_lote)
    peso_levadura = calcular_peso_levadura(volumen_levadura, densidad) if densidad > 0 else 0
    
    if volumen_levadura > 0:
        st.markdown("""
        ### 📊 **Resultados del cálculo**
        """)
        st.success(
            f"""
            🏷️ **Estilo:** {estilo}\n
            📏 **Densidad:** {grados_plato}\n
            🔬 **Pitch Rate:** {pitch_rate_selected} M células/mL °P\n
            💧 **Volumen necesario:** `{volumen_levadura:.4f} L`\n
            ⚖️ **Peso estimado:** `{peso_levadura:.4f} kg`
            """
        )
    else:
        st.warning("⚠️ Ingresa valores válidos para realizar el cálculo correctamente.")
else:
    st.error("🚨 Ingresa un conteo de células válido (mayor a 0).")
