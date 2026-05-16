import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def limpiar_datos(df):
    print("\n Valores nulos")
    print(df.isnull().sum())
    
    df = df.dropna().drop_duplicates().copy()
    df["Fecha"] = pd.to_datetime(df["Fecha"])
    
    df = df[df["Cantidad"] > 0]
    df = df[df["Precio_Unitario"] > 0]
    df["Mes"] = df["Fecha"].dt.month
    df["Dia_Semana"] = df["Fecha"].dt.day_name()

    if "Ganancia" not in df.columns:
        df["Ganancia"] = df["Total"] * 0.30
    
    print("\n Limpiando datos")
    
    return df


def preparar_datos_ml(df):
    df_modelo = limpiar_datos(df)

    scaler = MinMaxScaler()
    df_modelo["Cantidad_Normalizada"] = scaler.fit_transform(df_modelo[["Cantidad"]])

    if "Metodo_Pago" in df_modelo.columns:
        df_modelo = pd.get_dummies(df_modelo, columns=["Metodo_Pago"], dtype=int)

    return df_modelo, scaler
