# Mini Proyecto: Analisis de Ventas para Ferreteria

Proyecto en Python para cargar, limpiar y analizar ventas de una ferreteria a partir de un archivo Excel. Tambien incluye un modelo sencillo de recomendacion basado en clientes similares usando Machine Learning.

## Objetivo

El proyecto permite revisar informacion clave del negocio, como:

- Ventas por producto.
- Ventas por categoria.
- Mejores clientes.
- Producto mas vendido.
- Cliente que mas compra.
- Categoria que mas genera ingresos.
- Clientes potenciales con recomendacion personalizada.
- Recomendaciones de productos con un modelo de vecinos cercanos.

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

El programa carga el archivo `data/ventas.xlsx`, limpia los datos, muestra reportes en consola y genera recomendaciones para los clientes principales.

## Datos esperados

El archivo Excel debe incluir columnas como:

- `ID_Venta`
- `Fecha`
- `Cliente`
- `Producto`
- `Categoria`
- `Cantidad`
- `Precio_Unitario`
- `Total`

## Modulos principales

- `load_data.py`: carga el archivo Excel y muestra informacion inicial del dataset.
- `procesamiento.py`: limpia valores nulos, convierte fechas y filtra cantidades o precios invalidos.
- `analisis.py`: contiene funciones para analizar ventas, clientes, productos y categorias.
- `model_ML.py`: entrena un modelo `NearestNeighbors` para encontrar clientes similares.
- `recomendacion.py`: genera recomendaciones de productos para un cliente.
- `main.py`: coordina todo el flujo del proyecto.

## Resultado

Al ejecutar el proyecto se obtiene un resumen en consola con los indicadores principales de ventas y una lista de productos recomendados para clientes potenciales.
