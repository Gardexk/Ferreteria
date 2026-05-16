from pathlib import Path
import sys

import plotly.express as px
import streamlit as st


BASE_DIR = Path(__file__).resolve().parent
SRC_DIR = BASE_DIR / "src"
sys.path.insert(0, str(SRC_DIR))

from analisis import clientes_con_mayor_gasto, productos_mas_rentables, ventas_por_mes
from forecasting import predecir_ventas_futuras
from load_data import cargar_datos
from procesamiento import limpiar_datos
from recomendacion import recomendar_contextual


st.set_page_config(page_title="Dashboard Ferreteria IA", layout="wide")


@st.cache_data
def obtener_datos():
    return limpiar_datos(cargar_datos())


df = obtener_datos()

st.title("Dashboard Ferreteria IA")

total_ventas = df["Total"].sum()
clientes = df["Cliente"].nunique()
productos = df["Producto"].nunique()
ticket_promedio = df["Total"].mean()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Ventas", f"${total_ventas:,.2f}")
col2.metric("Clientes", clientes)
col3.metric("Productos", productos)
col4.metric("Ticket promedio", f"${ticket_promedio:,.2f}")

ventas_mes = ventas_por_mes(df).reset_index()
fig_ventas = px.bar(ventas_mes, x="Mes", y="Total", title="Ventas por mes")
st.plotly_chart(fig_ventas, use_container_width=True)

col_izq, col_der = st.columns(2)

with col_izq:
    clientes_top = clientes_con_mayor_gasto(df).head(10).reset_index()
    fig_clientes = px.bar(clientes_top, x="Cliente", y="Total", title="Clientes top")
    st.plotly_chart(fig_clientes, use_container_width=True)

with col_der:
    productos_top = productos_mas_rentables(df).head(10).reset_index()
    columna_valor = productos_top.columns[-1]
    fig_productos = px.bar(productos_top, x="Producto", y=columna_valor, title="Productos top")
    st.plotly_chart(fig_productos, use_container_width=True)

predicciones = predecir_ventas_futuras(df, meses=6)
if not predicciones.empty:
    fig_pred = px.line(
        predicciones,
        x="Fecha",
        y="Prediccion_Total",
        markers=True,
        title="Prediccion de ventas futuras",
    )
    st.plotly_chart(fig_pred, use_container_width=True)

cliente = st.selectbox("Cliente para recomendacion", sorted(df["Cliente"].unique()))
recomendaciones = recomendar_contextual(df, cliente)
st.subheader("Recomendaciones IA")
if recomendaciones:
    for producto in recomendaciones:
        st.write(f"- {producto}")
else:
    st.write("No hay recomendaciones disponibles para este cliente.")
