# Mini Proyecto: Analisis de Ventas para Ferreteria

Proyecto en Python para cargar, validar, limpiar y analizar ventas de una ferreteria a partir de un archivo Excel. Tambien incluye un modelo sencillo de recomendacion basado en clientes similares usando Machine Learning.

## Objetivo

El proyecto permite revisar informacion clave del negocio, como:

- Ventas por producto.
- Ventas por categoria.
- Mejores clientes.
- Producto mas vendido.
- Cliente que mas compra.
- Categoria que mas genera ingresos.
- Clientes potenciales con recomendacion personalizada.
- Recomendaciones de productos nuevos usando un modelo de vecinos cercanos.

## Estructura del proyecto

```text
Ferreteria/
+-- data/
|   +-- ventas.xlsx
+-- src/
|   +-- analisis.py
|   +-- load_data.py
|   +-- model_ML.py
|   +-- procesamiento.py
|   +-- recomendacion.py
+-- main.py
+-- README.md
+-- INFORME_PROYECTO.md
```

## Requisitos

Instala las dependencias necesarias:

```bash
pip install pandas openpyxl matplotlib scikit-learn
```

## Como ejecutar

Desde la carpeta principal del proyecto, ejecuta:

```bash
python main.py
```

El programa carga el archivo `data/ventas.xlsx`, valida que tenga las columnas necesarias, limpia los datos, muestra reportes en consola y genera recomendaciones para los clientes principales.

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

Si falta alguna columna, el programa detiene la ejecucion y muestra un mensaje indicando cuales columnas faltan.

## Modulos principales

- `load_data.py`: carga el archivo Excel, valida las columnas requeridas y muestra informacion inicial del dataset.
- `procesamiento.py`: limpia valores nulos, convierte fechas y filtra cantidades o precios invalidos.
- `analisis.py`: contiene funciones para analizar ventas, clientes, productos y categorias.
- `model_ML.py`: entrena un modelo `NearestNeighbors` para encontrar clientes similares sin modificar el DataFrame original.
- `recomendacion.py`: genera recomendaciones de productos para un cliente filtrando productos que ya compro.
- `main.py`: coordina todo el flujo del proyecto.

## Correcciones implementadas

- El modelo de Machine Learning trabaja con una copia interna del DataFrame, por lo que ya no agrega la columna `Producto_ID` a los datos originales.
- Las recomendaciones ahora excluyen productos que el cliente ya compro.
- La carga de datos ahora valida que el Excel tenga todas las columnas requeridas antes de continuar.
- El proyecto se mantiene como aplicacion de consola. Una interfaz grafica o una base de datos pueden agregarse como mejoras futuras.

## Resultado

Al ejecutar el proyecto se obtiene un resumen en consola con los indicadores principales de ventas y recomendaciones para clientes potenciales.

Si un cliente ya compro todos los productos disponibles en el dataset, el sistema muestra el mensaje `no hay productos nuevos para recomendar`.
