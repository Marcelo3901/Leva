import streamlit as st

# Título de la aplicación
st.title("Calculadora de Levadura para Cervecería")

# Definir los estilos de cerveza con sus respectivos grados Plato
estilos = {
    "Golden Ale": 1046,
    "Blonde Ale Maracuya": 1046,
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

# Selección del estilo de cerveza
estilo_Seleccionado = st.selectbox("Selecciona el estilo de cerveza:", list(estilos.keys()) + ["Otro estilo"])

# Si el usuario elige "Otro estilo", permitir ingresar el grado Plato
if estilo_Seleccionado == "Otro estilo":
    densidad_P = st.number_input("Ingresa la densidad en °P de la cerveza (Grados Plato):", min_value=0.0, step=0.1)
else:
    densidad_P = estilos[estilo_Seleccionado]  # Usar la densidad predefinida del estilo seleccionado

# Ingreso del conteo de células vivas en la cámara de Neubauer (células/mL), en millones de células
conteo_neubauer = st.number_input("Ingresa el conteo de células vivas en la cámara de Neubauer (M Células):", min_value=0.0, step=0.1)
conteo_neubauer *= 1e6  # Convertir a células por mL (1 M Células = 1e6 células)

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

