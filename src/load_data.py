import pandas as pd
from pathlib import Path

from analisis import mostrar_reporte_completo
from procesamiento import limpiar_datos


BASE_DIR = Path(__file__).resolve().parents[1]
COLUMNAS_REQUERIDAS = {
    "ID_Venta",
    "Cliente",
    "Producto",
    "Categoria",
    "Cantidad",
    "Precio_Unitario",
    "Fecha",
    "Total",
}


def validar_columnas(df):
    columnas_faltantes = COLUMNAS_REQUERIDAS.difference(df.columns)

    if columnas_faltantes:
        faltantes = ", ".join(sorted(columnas_faltantes))
        raise ValueError(f"El archivo Excel no tiene las columnas requeridas: {faltantes}")


def cargar_datos(ruta_archivo=BASE_DIR / "data" / "ventas.xlsx"):
    df=pd.read_excel(ruta_archivo)
    validar_columnas(df)

    print("\nRegistros ")
    print(df.head())
    
    print("Informacion de datos")
    df.info()
    
    return df


if __name__ == "__main__":
    datos = cargar_datos()
    datos = limpiar_datos(datos)
    mostrar_reporte_completo(datos)
