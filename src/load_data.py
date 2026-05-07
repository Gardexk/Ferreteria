import pandas as pd
from pathlib import Path

from analisis import mostrar_reporte_completo
from procesamiento import limpiar_datos


BASE_DIR = Path(__file__).resolve().parents[1]


def cargar_datos(ruta_archivo=BASE_DIR / "data" / "ventas.xlsx"):
    df=pd.read_excel(ruta_archivo)
    print("\nRegistros ")
    print(df.head())
    
    print("Informacion de datos")
    df.info()
    
    return df


if __name__ == "__main__":
    datos = cargar_datos()
    datos = limpiar_datos(datos)
    mostrar_reporte_completo(datos)
