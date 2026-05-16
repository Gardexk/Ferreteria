import pandas as pd
from sklearn.linear_model import LinearRegression


def preparar_ventas_mensuales(df):
    ventas = (
        df.assign(Fecha=pd.to_datetime(df["Fecha"]))
        .set_index("Fecha")
        .resample("MS")["Total"]
        .sum()
        .reset_index()
    )
    ventas["Periodo"] = range(len(ventas))
    return ventas


def predecir_ventas_futuras(df, meses=3):
    ventas = preparar_ventas_mensuales(df)
    if len(ventas) < 2:
        return pd.DataFrame(columns=["Fecha", "Prediccion_Total"])

    modelo = LinearRegression()
    modelo.fit(ventas[["Periodo"]], ventas["Total"])

    ultimo_periodo = int(ventas["Periodo"].max())
    fechas_futuras = pd.date_range(
        ventas["Fecha"].max() + pd.offsets.MonthBegin(1),
        periods=meses,
        freq="MS",
    )
    periodos = pd.DataFrame({"Periodo": range(ultimo_periodo + 1, ultimo_periodo + meses + 1)})
    predicciones = modelo.predict(periodos[["Periodo"]])

    return pd.DataFrame(
        {
            "Fecha": fechas_futuras,
            "Prediccion_Total": predicciones,
        }
    )
