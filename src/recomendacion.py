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
