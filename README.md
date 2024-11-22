<div style="text-align: center;">
  <img src="https://github.com/Hack-io-Data/Imagenes/blob/main/01-LogosHackio/logo_naranja@4x.png?raw=true" alt="esquema" />
</div>


# Proyecto: Predicción de Precios de Casas 🏠

## Introducción

La predicción de precios de bienes inmuebles es un área clave en la intersección de los negocios y la ciencia de datos. En este proyecto, abordarás el desafío de estimar el precio de las casas. Trabajaras con un conjunto de datos real, que contiene información detallada sobre propiedades en Madrid, como su tamaño, ubicación, número de habitaciones, tipo de propiedad, y más. El objetivo principal del proyecto es predecir el precio de una casa, 

## Contexto del Problema

El mercado inmobiliario es dinámico y está influenciado por múltiples variables, como la ubicación, las características de la propiedad y las condiciones económicas. Un modelo predictivo preciso puede ser una herramienta poderosa para agentes inmobiliarios, compradores y vendedores. Este proyecto te sumergirá en la complejidad de estos factores y te enseñará cómo transformarlos en conocimiento útil para la toma de decisiones.


## Descripción del Dataset 

Este conjunto de datos contiene información sobre propiedades en alquiler en Madrid. A continuación, se detalla la estructura y contenido de las columnas:

- Columnas principales

    - `propertyCode`: Código único que identifica cada propiedad.

    - `price`: Precio de la propiedad en euros (variable objetivo).

    - `propertyType`: Tipo de propiedad (e.g., piso, ático, chalet, etc.).

    - `size`: Tamaño de la propiedad en metros cuadrados.

    - `rooms`: Número de habitaciones.

    - `bathrooms`: Número de baños.

    - `district`: Distrito donde se encuentra la propiedad (e.g., Centro, Hortaleza).

    - `neighborhood`: Barrio dentro del distrito (datos menos completos que el distrito).

    - `latitude` y `longitude`: Coordenadas geográficas de la propiedad.

    - `address`: Dirección aproximada o descriptiva de la propiedad.

- Atributos adicionales

    - `numPhotos`: Número de fotos disponibles de la propiedad. 

    - `exterior`: Indicador booleano que muestra si la propiedad es exterior (True o False).

    - `hasLift`: Indica si la propiedad tiene ascensor (True o False, con algunos valores nulos).

    - `parkingSpace`: Información sobre espacio de estacionamiento (detallada en formato JSON en algunas filas).

    - `priceByArea`: Precio por metro cuadrado en euros.

    - `floor`: Piso en el que se encuentra la propiedad (e.g., bajo, 1, ático).

    - `description`: Descripción textual de la propiedad.

- Columnas de características del anuncio

    - `hasVideo`: Indica si el anuncio incluye un video (True o False).

    - `has3DTour`: Indica si el anuncio tiene un tour 3D disponible.

    - `newDevelopment`: Booleano que indica si la propiedad es una nueva construcción.

    - `superTopHighlight` y `topNewDevelopment`: Indicadores booleanos de la importancia o destaque del anuncio en la plataforma.

-  Características menos completas

    - `neighborhood` y `district`: Aunque importantes, contienen valores nulos y pueden necesitar limpieza.

    - `parkingSpace` y `labels`: Información limitada a unas pocas propiedades.

    - `newDevelopmentFinished`: Solo incluye datos en propiedades específicas, con baja representación.

**Nota:** El dataset tiene 40 columnas en total. Antes de construir el modelo, es importante realizar una limpieza y selección de características relevantes.


## Pasos para el Desarrollo 

1. **Carga y Exploración del Dataset**

   - Comprende las variables del dataset y realiza un análisis exploratorio para identificar patrones y posibles valores atípicos.

2. **Preprocesamiento de Datos**

   - Limpia el dataset eliminando valores nulos o duplicados.

   - Realiza una codificación de variables categóricas si es necesario.

   - Escala las variables numéricas.

   - Gestiona los nulos y *outliers*

3. **Construcción del Modelo**

   - Divide el dataset en conjuntos de entrenamiento y prueba.

   - Prueba diferentes modelos de Machine Learning (e.g., regresión lineal, árboles de decisión, Random Forest, Gradient Boosting).

   - Evalúa el desempeño de cada modelo utilizando métricas como el RMSE (Root Mean Squared Error) o R².


4. **Visualización de Resultados**

   - Muestra gráficos que expliquen la importancia de las variables, errores del modelo y predicciones realizadas.

5. **Optimización**

   - Realiza ajustes en los hiperparámetros para mejorar el desempeño del modelo.


## Métricas de Evaluación 

El desempeño del modelo será evaluado con las siguientes métricas:

- **RMSE (Root Mean Squared Error):** Medirá la precisión del modelo.

- **R² (Coeficiente de Determinación):** Evaluará qué tan bien el modelo explica la variación de los datos.


## Como Entregar el Proyecto

La entrega del proyecto se realizará a través de una **issue en GitHub**, trabajando en un repositorio propio en tu cuenta personal. Los pasos que deberás seguir para hacer la entrega del proyecto son:


- **Crear un nuevo repositorio en tu cuenta de GitHub:**

   - Crea un nuevo repositorio llamado `Proyecto7-NombreProyecto`. Este nombre es obligatorio, no podremos llamarlo de otra forma. 

   - Configuralo como público. 


- **Desarrolla el proyecto:**

   - Implementa el código para la resolución del problema.

   - Recuerda hacer commits regulares mientras avanzas en el desarrollo:

     ```bash
     git add .
     git commit -m "Descripción del avance"
     git push
     ```


- **Crear una issue en el repositorio original del curso:**

   - Ve al repositorio original del curso y dirígete a la pestaña de **Issues**.

- **Abrir una nueva issue para tu entrega:**

   - Haz clic en **New Issue** y llena los siguientes campos:

     - **Título:** Usa el formato "Entrega Proyecto: ProyectoRegresionLineal - [Tu Nombre]".

     - **Descripción:** En la descripción, incluye:

       - Una breve explicación de tu proyecto.

       - Instrucciones para ejecutar tu código (si aplica).

       - Un enlace a tu repositorio personal donde está alojado el proyecto.


## 🚀 Entrega del Proyecto 🚀

**Fecha y hora límite:**

🗓️ **Lunes a las 9:00 AM.**


**Nota importante:**

⚠️ **Todos los proyectos que sean entregados o modificados después de la hora límite (lunes a las 9:00 AM) se considerarán como no entregados.** Por favor, asegúrate de completar y enviar tu trabajo a tiempo para evitar problemas.


# 🎤 Presentación de Proyectos 🎤

El lunes tendremos las **presentaciones de los proyectos**. La dinámica será la siguiente:

- De forma **aleatoria**, seleccionaremos entre **3 y 5 alumnos** para presentar su proyecto.

- Cada alumno tendrá **5 minutos** para explicar su proyecto y hacer una demo en vivo. Durante este tiempo podrán mostrar cómo funciona su juego y resaltar las características principales.

**Detalles importantes:**

- Es importante que lleguéis puntuales, ya que comenzaremos las presentaciones de inmediato.

- Asegúrate de que tu código esté listo y funcional para la demo.

- Todos debemos estar preparados para presentar, ya que la selección será completamente aleatoria.
