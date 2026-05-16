from sklearn.metrics import (
    accuracy_score,
    f1_score,
    mean_squared_error,
    precision_score,
    recall_score,
)


def evaluar_clasificacion(y_test, predicciones):
    return {
        "accuracy": accuracy_score(y_test, predicciones),
        "precision": precision_score(y_test, predicciones, average="weighted", zero_division=0),
        "recall": recall_score(y_test, predicciones, average="weighted", zero_division=0),
        "f1_score": f1_score(y_test, predicciones, average="weighted", zero_division=0),
    }


def evaluar_regresion(y_test, predicciones):
    return {
        "rmse": mean_squared_error(y_test, predicciones) ** 0.5,
    }


def evaluar_modelos(resultados_modelos):
    metricas = {}
    for nombre, resultado in resultados_modelos.items():
        if resultado["tipo"] == "clasificacion":
            metricas[nombre] = evaluar_clasificacion(resultado["y_test"], resultado["predicciones"])
        else:
            metricas[nombre] = evaluar_regresion(resultado["y_test"], resultado["predicciones"])
    return metricas
