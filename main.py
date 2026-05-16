from pathlib import Path
import sys


BASE_DIR = Path(__file__).resolve().parent
SRC_DIR = BASE_DIR / "src"
sys.path.insert(0, str(SRC_DIR))

from analisis import (
    categoria_que_mas_genera,
    cliente_que_mas_compra,
    mejores_clientes,
    potenciales_clientes,
    producto_mas_vendido,
    productos_mas_rentables,
    ventas_por_categoria,
    ventas_por_mes,
    ventas_por_producto,
)
from evaluation import evaluar_modelos
from forecasting import predecir_ventas_futuras
from load_data import cargar_datos
from model_ML import entrenar_model, entrenar_modelos_supervisados
from procesamiento import limpiar_datos
from recomendacion import recomendar, recomendar_contextual


def main():
    df = cargar_datos()
    df = limpiar_datos(df)

    print("\n===== ANALISIS DE VENTAS =====")
    ventas_por_mes(df)
    ventas_por_producto(df, mostrar_grafica=False)
    ventas_por_categoria(df)
    mejores_clientes(df)
    productos_mas_rentables(df)
    producto_mas_vendido(df)
    cliente_principal, _ = cliente_que_mas_compra(df)
    categoria_que_mas_genera(df)
    clientes_recomendacion = potenciales_clientes(df, top_n=3)

    print("\n===== MODELO DE RECOMENDACION =====")
    modelo, matriz, le = entrenar_model(df)

    for cliente in clientes_recomendacion.index:
        productos = recomendar(cliente, modelo, matriz, le)

        print(f"\nRecomendaciones con ML para {cliente}")
        if isinstance(productos, str):
            print(f"- {productos}")
            continue

        for producto in productos:
            print(f"- {producto}")

        contextuales = recomendar_contextual(df, cliente)
        if contextuales:
            print("Recomendaciones contextuales:")
            for producto in contextuales:
                print(f"- {producto}")

    print(f"\nCliente principal detectado: {cliente_principal}")

    print("\n===== MODELOS SUPERVISADOS =====")
    resultados_modelos = entrenar_modelos_supervisados(df)
    metricas = evaluar_modelos(resultados_modelos)
    for nombre, valores in metricas.items():
        print(f"\n{nombre}")
        for metrica, valor in valores.items():
            print(f"- {metrica}: {valor:.4f}")

    print("\n===== PRONOSTICO DE VENTAS =====")
    predicciones = predecir_ventas_futuras(df, meses=3)
    if predicciones.empty:
        print("No hay suficientes datos para pronosticar.")
    else:
        print(predicciones.to_string(index=False))


if __name__ == "__main__":
    main()
