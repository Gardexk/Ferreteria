import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

def entrenar_model(df):
    print("\n Modelo para ML")
    le=LabelEncoder()
    df_modelo = df.copy()
    df_modelo["Producto_ID"]=le.fit_transform(df_modelo["Producto"])
    matriz=df_modelo.pivot_table(
        index="Cliente",
        columns="Producto_ID",
        values="Cantidad",
        fill_value=0
    )
    
    modelo=NearestNeighbors(metric="cosine")
    modelo.fit(matriz)
    print("Modelo entrenado")
    return modelo, matriz, le


def preparar_features_modelos(df):
    df_modelo = df.copy()
    df_modelo["Fecha_Ordinal"] = pd.to_datetime(df_modelo["Fecha"]).map(pd.Timestamp.toordinal)
    columnas_base = ["Cantidad", "Precio_Unitario", "Total", "Mes", "Fecha_Ordinal"]
    columnas = [columna for columna in columnas_base if columna in df_modelo.columns]
    X = df_modelo[columnas]
    return X, df_modelo


def entrenar_modelos_supervisados(df):
    X, df_modelo = preparar_features_modelos(df)
    resultados = {}

    if len(df_modelo) < 5:
        return resultados

    y_categoria = df_modelo["Categoria"]
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y_categoria,
        test_size=0.25,
        random_state=42,
        stratify=y_categoria if y_categoria.value_counts().min() > 1 else None,
    )

    clasificadores = {
        "decision_tree": DecisionTreeClassifier(random_state=42),
        "random_forest": RandomForestClassifier(n_estimators=100, random_state=42),
    }

    if y_categoria.nunique() == 2:
        clasificadores["logistic_regression"] = LogisticRegression(max_iter=1000)

    for nombre, modelo in clasificadores.items():
        modelo.fit(X_train, y_train)
        resultados[nombre] = {
            "modelo": modelo,
            "X_test": X_test,
            "y_test": y_test,
            "predicciones": modelo.predict(X_test),
            "tipo": "clasificacion",
        }

    X_reg = X.drop(columns=["Total"], errors="ignore")
    y_reg = df_modelo["Total"]
    X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(
        X_reg,
        y_reg,
        test_size=0.25,
        random_state=42,
    )
    regresion = LinearRegression()
    regresion.fit(X_train_r, y_train_r)
    resultados["linear_regression"] = {
        "modelo": regresion,
        "X_test": X_test_r,
        "y_test": y_test_r,
        "predicciones": regresion.predict(X_test_r),
        "tipo": "regresion",
    }

    print("\nModelos supervisados entrenados")
    print(", ".join(resultados.keys()))
    return resultados
