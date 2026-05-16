# Mini Proyecto: Analisis de Ventas para Ferreteria

Proyecto en Python para cargar, validar, limpiar, analizar y predecir ventas de una ferreteria a partir de un archivo Excel. Incluye analisis de negocio, recomendaciones inteligentes, modelos de Machine Learning, evaluacion matematica, pronostico de ventas y un dashboard interactivo con Streamlit.

## Objetivo

El proyecto permite revisar informacion clave del negocio, como:

- Ventas por producto.
- Ventas por categoria.
- Ventas por mes.
- Mejores clientes.
- Clientes con mayor gasto.
- Producto mas vendido.
- Productos mas rentables.
- Cliente que mas compra.
- Categoria que mas genera ingresos.
- Clientes potenciales con recomendacion personalizada.
- Recomendaciones por clientes similares usando KNN.
- Recomendaciones contextuales y productos complementarios.
- Metricas de modelos de clasificacion y regresion.
- Pronostico de ventas futuras.
- Dashboard interactivo para explorar ventas, clientes, productos, predicciones y recomendaciones.

## Estructura del proyecto

```text
Ferreteria/
+-- data/
|   +-- ventas.xlsx
+-- src/
|   +-- analisis.py
|   +-- evaluation.py
|   +-- forecasting.py
|   +-- load_data.py
|   +-- model_ML.py
|   +-- procesamiento.py
|   +-- recomendacion.py
+-- dashboard.py
+-- main.py
+-- requirements.txt
+-- README.md
```

## Requisitos

El proyecto usa un entorno virtual local `.venv`. Para activarlo en PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Si necesitas reinstalar las dependencias:

```powershell
pip install -r requirements.txt
```

Librerias principales:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `openpyxl`
- `plotly`
- `streamlit`
- `joblib`
- `scipy`
- `statsmodels`
- `xgboost`

## Como ejecutar el reporte de consola

Desde la carpeta principal del proyecto:

```powershell
.\.venv\Scripts\python.exe main.py
```

El programa carga `data/ventas.xlsx`, valida el dataset, limpia los datos, ejecuta analisis de ventas, genera recomendaciones, entrena modelos, calcula metricas y muestra un pronostico de ventas.

## Como ejecutar el dashboard

Desde la carpeta principal del proyecto:

```powershell
.\.venv\Scripts\streamlit.exe run dashboard.py
```

El dashboard muestra:

- Ventas totales.
- Numero de clientes.
- Numero de productos.
- Ticket promedio.
- Ventas por mes.
- Clientes top.
- Productos top.
- Predicciones de ventas futuras.
- Recomendaciones IA por cliente.

## Datos esperados

El archivo Excel debe incluir estas columnas:

- `ID_Venta`
- `Cliente`
- `Producto`
- `Categoria`
- `Cantidad`
- `Precio_Unitario`
- `Fecha`
- `Total`

Columnas opcionales:

- `Metodo_Pago`: si existe, se codifica con variables dummy para modelos.
- `Ganancia`: si no existe, el sistema calcula una ganancia estimada usando el 30% del total.

Si falta alguna columna requerida, el programa detiene la ejecucion y muestra un mensaje indicando cuales columnas faltan.

## Modulos principales

- `load_data.py`: carga el archivo Excel, valida columnas requeridas y muestra tipos de datos, valores nulos y duplicados.
- `procesamiento.py`: limpia valores nulos y duplicados, convierte fechas, filtra cantidades/precios invalidos, agrega `Mes`, `Dia_Semana`, `Ganancia` y prepara datos para ML con `MinMaxScaler`.
- `analisis.py`: contiene analisis de ventas por producto, categoria y mes; clientes top; productos rentables; heatmap de correlacion y distribucion de ventas.
- `model_ML.py`: conserva el modelo KNN con `NearestNeighbors` para clientes similares y agrega modelos supervisados: Decision Tree, Random Forest, Logistic Regression cuando aplica y Linear Regression.
- `recomendacion.py`: genera recomendaciones por similitud, productos complementarios y recomendaciones contextuales por historial del cliente.
- `evaluation.py`: evalua modelos con `accuracy`, `precision`, `recall`, `f1_score` y `rmse`.
- `forecasting.py`: predice ventas futuras usando regresion lineal sobre ventas mensuales.
- `dashboard.py`: construye el panel interactivo con Streamlit y graficas de Plotly.
- `main.py`: coordina todo el flujo del proyecto en consola.

## Modelos incluidos

| Modelo | Uso |
| --- | --- |
| KNN / NearestNeighbors | Similitud entre clientes |
| Decision Tree | Clasificacion |
| Random Forest | Prediccion robusta |
| Logistic Regression | Clasificacion binaria, si los datos tienen dos clases |
| Linear Regression | Pronostico y regresion |

## Metricas incluidas

| Metrica | Objetivo |
| --- | --- |
| Accuracy | Precision general del modelo |
| Precision | Exactitud de predicciones positivas |
| Recall | Capacidad de deteccion correcta |
| F1 Score | Balance entre precision y recall |
| RMSE | Error de modelos de regresion |

## Resultado

Al ejecutar `main.py`, se obtiene un reporte en consola con indicadores principales, recomendaciones, metricas de modelos y pronostico de ventas.

Si un cliente ya compro todos los productos disponibles en el dataset, el sistema muestra el mensaje `no hay productos nuevos para recomendar`.

Al ejecutar `dashboard.py`, se abre un panel web local para explorar el negocio de forma visual e interactiva.
