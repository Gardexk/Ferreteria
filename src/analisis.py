def ventas_por_producto(df, mostrar_grafica=True):
    resumen = df.groupby("Producto")["Cantidad"].sum().sort_values(ascending=False)
    print(resumen)

    if mostrar_grafica:
        import matplotlib.pyplot as plt

        resumen.plot(kind="bar")
        plt.title("Ventas por producto")
        plt.xticks(rotation=45)
        plt.show()
    
def mejores_clientes(df):
    clientes = clientes_con_mayor_gasto(df)
    print("\n Mejores clientes")
    print(clientes.head(10))
    return clientes


def ventas_por_mes(df):
    ventas = df.groupby("Mes")["Total"].sum().sort_index()
    print("\nVentas por mes")
    print(ventas)
    return ventas


def clientes_con_mayor_gasto(df):
    return df.groupby("Cliente")["Total"].sum().sort_values(ascending=False)


def productos_mas_rentables(df):
    columna = "Ganancia" if "Ganancia" in df.columns else "Total"
    productos = df.groupby("Producto")[columna].sum().sort_values(ascending=False)
    print("\nProductos mas rentables")
    print(productos.head(10))
    return productos


def ventas_por_categoria(df):
    resumen = (
        df.groupby("Categoria")
        .agg(Cantidad=("Cantidad", "sum"), Total=("Total", "sum"))
        .sort_values("Total", ascending=False)
    )
    print("\nVentas por categoria")
    print(resumen)
    return resumen


def producto_mas_vendido(df):
    productos = (
        df.groupby("Producto")
        .agg(Cantidad=("Cantidad", "sum"), Total=("Total", "sum"))
        .sort_values(["Cantidad", "Total"], ascending=False)
    )
    producto = productos.iloc[0]
    nombre = productos.index[0]
    print("\nProducto que mas vende")
    print(f"{nombre} - {producto['Cantidad']:.0f} unidades vendidas - ${producto['Total']:,.2f}")
    return nombre, producto


def cliente_que_mas_compra(df):
    clientes = (
        df.groupby("Cliente")
        .agg(Compras=("ID_Venta", "count"), Cantidad=("Cantidad", "sum"), Total=("Total", "sum"))
        .sort_values("Total", ascending=False)
    )
    cliente = clientes.iloc[0]
    nombre = clientes.index[0]
    print("\nCliente que mas compra")
    print(f"{nombre} - {cliente['Compras']:.0f} compras - {cliente['Cantidad']:.0f} unidades - ${cliente['Total']:,.2f}")
    return nombre, cliente


def categoria_que_mas_genera(df):
    categorias = df.groupby("Categoria")["Total"].sum().sort_values(ascending=False)
    nombre = categorias.index[0]
    total = categorias.iloc[0]
    print("\nCategoria que mas genera")
    print(f"{nombre} - ${total:,.2f}")
    return nombre, total


def _recomendar_para_cliente(df, cliente):
    compras_cliente = df[df["Cliente"] == cliente]
    categorias_cliente = compras_cliente.groupby("Categoria")["Total"].sum().sort_values(ascending=False)
    categoria_favorita = categorias_cliente.index[0]
    productos_comprados = set(compras_cliente["Producto"])

    candidatos = (
        df[(df["Categoria"] == categoria_favorita) & (~df["Producto"].isin(productos_comprados))]
        .groupby("Producto")
        .agg(Cantidad=("Cantidad", "sum"), Total=("Total", "sum"))
        .sort_values(["Cantidad", "Total"], ascending=False)
    )

    if candidatos.empty:
        candidatos = (
            df[~df["Producto"].isin(productos_comprados)]
            .groupby("Producto")
            .agg(Cantidad=("Cantidad", "sum"), Total=("Total", "sum"))
            .sort_values(["Cantidad", "Total"], ascending=False)
        )

    if candidatos.empty:
        producto = compras_cliente.groupby("Producto")["Cantidad"].sum().idxmax()
        return f"Reforzar recompra de {producto}, porque ya es uno de sus productos frecuentes."

    producto = candidatos.index[0]
    return f"Ofrecer {producto}, porque compra mucho en la categoria {categoria_favorita} y aun no aparece en su historial."


def potenciales_clientes(df, top_n=3):
    clientes = (
        df.groupby("Cliente")
        .agg(Compras=("ID_Venta", "count"), Cantidad=("Cantidad", "sum"), Total=("Total", "sum"))
        .sort_values(["Total", "Compras"], ascending=False)
        .head(top_n)
    )

    print(f"\n{top_n} potenciales clientes y recomendacion personalizada")
    for cliente, fila in clientes.iterrows():
        recomendacion = _recomendar_para_cliente(df, cliente)
        print(
            f"- {cliente}: ${fila['Total']:,.2f} en {fila['Compras']:.0f} compras. "
            f"Recomendacion: {recomendacion}"
        )
    return clientes


def mostrar_reporte_completo(df):
    ventas_por_mes(df)
    ventas_por_producto(df, mostrar_grafica=False)
    ventas_por_categoria(df)
    mejores_clientes(df)
    productos_mas_rentables(df)
    producto_mas_vendido(df)
    cliente_que_mas_compra(df)
    categoria_que_mas_genera(df)
    potenciales_clientes(df)


def graficar_heatmap_correlacion(df):
    import matplotlib.pyplot as plt
    import seaborn as sns

    correlacion = df.corr(numeric_only=True)
    sns.heatmap(correlacion, annot=True, cmap="viridis")
    plt.title("Correlacion de variables numericas")
    plt.tight_layout()
    plt.show()


def graficar_distribucion_ventas(df):
    import matplotlib.pyplot as plt
    import seaborn as sns

    sns.histplot(df["Total"], kde=True)
    plt.title("Distribucion de ventas")
    plt.xlabel("Total")
    plt.tight_layout()
    plt.show()
