import pandas as pd


def limpiar_datos(df):
    print("\n Valores nulos")
    print(df.isnull().sum())
    
    df = df.dropna().copy()
    df["Fecha"] = pd.to_datetime(df["Fecha"])
    
    df=df[df["Cantidad"]>0]
    df=df[df["Precio_Unitario"]>0]
    
    print("\n Limpiando datos")
    
    return df
