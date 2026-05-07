from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import NearestNeighbors

def entrenar_model(df):
    print("\n Modelo para ML")
    le=LabelEncoder()
    df["Producto_ID"]=le.fit_transform(df["Producto"])
    matriz=df.pivot_table(
        index="Cliente",
        columns="Producto_ID",
        values="Cantidad",
        fill_value=0
    )
    
    modelo=NearestNeighbors(metric="cosine")
    modelo.fit(matriz)
    print("Modelo entrenado")
    return modelo,matriz,le