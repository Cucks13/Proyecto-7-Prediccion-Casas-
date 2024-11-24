# Proyecto 7 - Predicción de Precios de Casas

Este repositorio contiene el desarrollo completo de un proyecto orientado a predecir los precios de propiedades en las ciudades de Madrid y Toledo. A través de un análisis exhaustivo de datos y el desarrollo de modelos de machine learning, se busca obtener predicciones precisas basadas en múltiples características.

---

## 📂 Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

├── datos/
├── notebooks/
│   ├── Toledo/
│   ├── Madrid/
│   ├── 01_EDA_GENERAL.ipynb
│   └── CONCLUSIONES.ipynb
├── src/
├── .gitignore
└── README.md
  
## Notebooks

Para realizar el análisis exploratorio y los modelos, sigue este orden:

1. **`01_EDA_GENERAL.ipynb`**  
   - Este notebook contiene un análisis exploratorio general sobre los datos combinados de Madrid y Toledo.

2. **`02_EDA_ETL_MADRID.ipynb` y `02_EDA_ETL_TOLEDO.ipynb`**  
   - `02_EDA_ETL_MADRID.ipynb`: Análisis exploratorio y transformación de datos específicos para Madrid.  
   - `02_EDA_ETL_TOLEDO.ipynb`: Análisis exploratorio y transformación de datos específicos para Toledo.

3. **Notebooks de modelos por ciudad**  
   - **Madrid**:
     - `03_MODELO_1.ipynb`: Primer modelo desarrollado para Madrid.  
     - `04_MODELO_2.ipynb`: Segundo modelo desarrollado para Madrid.  
     - `05_MODELO_3.ipynb`: Tercer modelo desarrollado para Madrid.  

   - **Toledo**:
     - `03_MODELO_1.ipynb`: Primer modelo desarrollado para Toledo.  
     - `04_MODELO_2.ipynb`: Segundo modelo desarrollado para Toledo.  
     - `05_MODELO_3.ipynb`: Tercer modelo desarrollado para Toledo.  

Sigue este orden para garantizar que los datos y modelos estén correctamente alineados con el flujo de trabajo.

## 🔧 Funciones Relevantes

La carpeta `src/` contiene las siguientes herramientas:

- **[`soporte_ajuste.py`](./src/soporte_ajuste.py)**: Métodos para ajuste de hiperparámetros y optimización.
- **[`soporte_encoding.py`](./src/soporte_encoding.py)**: Funciones para encoding de variables categóricas (one-hot, target, ordinal, etc.).
- **[`soporte_nulos.py`](./src/soporte_nulos.py)**: Manejo de valores nulos (imputación y análisis).
- **[`soporte_outliers.py`](./src/soporte_outliers.py)**: Métodos para detección y manejo de outliers.
- **[`soporte_preprocesamiento.py`](./src/soporte_preprocesamiento.py)**: Preprocesamiento general de los datos.

---

## ✨ Resultados Destacados

Se desarrollaron modelos predictivos con un rendimiento sobresaliente en términos de **RMSE** y **R²**:

- **Madrid**:
  - Mejor modelo: RMSE = 5.24, R² = 0.99
- **Toledo**:
  - Mejor modelo: RMSE = 30.30, R² = 0.91

Consulta los notebooks de modelos para más detalles.

## 📊 Conclusiones

Todas las conclusiones obtenidas del análisis y los modelos están documentadas en el archivo [CONCLUSIONES.ipynb](./notebooks/CONCLUSIONES.ipynb).  
Consulta este archivo para entender los resultados y las decisiones tomadas durante el proyecto.

## 🚀 Next Steps

A continuación, se detallan los próximos pasos sugeridos para mejorar y expandir este proyecto:

1. **Optimización del Modelo**:
   - Probar modelos más avanzados como **Gradient Boosting**, **CatBoost**, o **LightGBM** para mejorar las métricas actuales.
   - Realizar un análisis de sensibilidad sobre los hiperparámetros más relevantes.

2. **Incorporar Nuevas Variables**:
   - Analizar nuevas fuentes de datos que puedan enriquecer el dataset, como datos socioeconómicos, ambientales o del mercado inmobiliario.
   - Evaluar la incorporación de interacciones entre variables existentes.

3. **Despliegue del Modelo**:
   - Desplegar el modelo en una aplicación interactiva utilizando **Streamlit** para permitir predicciones en tiempo real.
   - Documentar una interfaz clara y amigable para facilitar el uso del modelo por usuarios finales.

4. **Visualización Interactiva**:
   - Desarrollar dashboards interactivos con **Streamlit** para explorar los datos y las predicciones.
   - Visualizar métricas clave y los factores más influyentes en las predicciones del modelo.

5. **Expansión del Proyecto**:
   - Añadir más ciudades al análisis, enfocándose en otros mercados inmobiliarios relevantes.
   - Adaptar el pipeline existente para procesar datos específicos de cada nueva ciudad.

6. **Exploración de Técnicas Avanzadas**:
   - Aplicar técnicas de **Feature Engineering** más complejas como embeddings para variables categóricas.
   - Evaluar el uso de técnicas de **Deep Learning**, especialmente si se incluyen grandes volúmenes de datos no estructurados.

---

Con estos pasos, el proyecto puede continuar mejorando y adaptándose a las necesidades del análisis y predicción en el mercado inmobiliario.
