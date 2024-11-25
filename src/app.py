import streamlit as st
import pandas as pd
import joblib  # Para cargar los modelos

# Cargar los modelos
modelo_madrid = joblib.load("../notebooks/Madrid/modelo_madrid.pkl")
modelo_toledo = joblib.load("../notebooks/Toledo/modelo_toledo.pkl")

# Función para realizar predicciones
def predecir_precio(modelo, data):
    prediccion = modelo.predict([data])
    return prediccion[0]

# Título de la aplicación
st.title("Predicción de Precios Inmobiliarios")
st.subheader("Prueba los modelos predictivos para Madrid y Toledo")

# Entrada de datos por el usuario
st.sidebar.header("Introduce las características de la propiedad:")
metros_cuadrados = st.sidebar.number_input("Metros cuadrados", min_value=10, max_value=1000, value=100)
habitaciones = st.sidebar.number_input("Número de habitaciones", min_value=1, max_value=10, value=3)
baños = st.sidebar.number_input("Número de baños", min_value=1, max_value=5, value=2)
ascensor = st.sidebar.selectbox("¿Tiene ascensor?", ["Sí", "No"])
tipo_vivienda = st.sidebar.selectbox("Tipo de vivienda", ["Piso", "Ático", "Dúplex", "Chalet"])

# Convertir los datos de entrada en un formato adecuado para el modelo
entrada = [
    metros_cuadrados,
    habitaciones,
    baños,
    1 if ascensor == "Sí" else 0,  # Codificación para ascensor
    tipo_vivienda,  # Puedes convertir esto a un encoding si es necesario
]

# Botón para generar predicciones
if st.button("Predecir"):
    # Realizar predicciones con ambos modelos
    precio_madrid = predecir_precio(modelo_madrid, entrada)
    precio_toledo = predecir_precio(modelo_toledo, entrada)

    # Mostrar resultados
    st.success("Predicciones Generadas:")
    st.write(f"**Precio en Madrid:** {precio_madrid:.2f} €")
    st.write(f"**Precio en Toledo:** {precio_toledo:.2f} €")
