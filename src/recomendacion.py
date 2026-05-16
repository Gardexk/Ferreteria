PRODUCTOS_RELACIONADOS = {
    "Taladro": ["Brocas", "Extensiones", "Tornillos"],
    "Martillo": ["Clavos", "Cinta metrica", "Guantes"],
    "Pintura": ["Brochas", "Rodillos", "Cinta adhesiva"],
    "Destornillador": ["Tornillos", "Taquetes", "Caja de herramientas"],
}


def recomendar(cliente,modelo,matriz,le,top_n=3):
    if cliente not in matriz.index:
        return "cliente no existe"

    vector=matriz.loc[cliente].values.reshape(1,-1)
    n_vecinos = min(top_n + 1, len(matriz))
    distancia, indices=modelo.kneighbors(vector,n_neighbors=n_vecinos)
    vecinos=matriz.index[indices.flatten()[1:]]

    if len(vecinos) == 0:
        return "no hay clientes similares suficientes para recomendar"

    recomendaciones=matriz.loc[vecinos].mean().sort_values(ascending=False)

    productos_comprados = matriz.loc[cliente][matriz.loc[cliente] > 0].index
    recomendaciones = recomendaciones.drop(productos_comprados, errors="ignore")

    if recomendaciones.empty:
        return "no hay productos nuevos para recomendar"

    productos=le.inverse_transform(recomendaciones.index.astype(int))
    return productos[:top_n]


def recomendar_productos_complementarios(producto, top_n=3):
    return PRODUCTOS_RELACIONADOS.get(producto, [])[:top_n]


def recomendar_contextual(df, cliente, top_n=3):
    compras = df[df["Cliente"] == cliente]
    if compras.empty:
        return []

    producto_frecuente = compras.groupby("Producto")["Cantidad"].sum().idxmax()
    complementarios = recomendar_productos_complementarios(producto_frecuente, top_n=top_n)
    if complementarios:
        return complementarios

    categoria = compras.groupby("Categoria")["Total"].sum().idxmax()
    comprados = set(compras["Producto"])
    candidatos = (
        df[(df["Categoria"] == categoria) & (~df["Producto"].isin(comprados))]
        .groupby("Producto")["Total"]
        .sum()
        .sort_values(ascending=False)
    )
    return list(candidatos.head(top_n).index)
