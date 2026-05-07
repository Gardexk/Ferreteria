def recomendar(cliente,modelo,matriz,le,top_n=3):
    if cliente not in matriz.index:
        return "cliente no existe"
    vector=matriz.loc[cliente].values.reshape(1,-1)
    distancia, indices=modelo.kneighbors(vector,n_neighbors=top_n+1)
    vecinos=matriz.index[indices.flatten()[1:]]
    recomendaciones=matriz.loc[vecinos].mean().sort_values(ascending=False)
    productos=le.inverse_transform(recomendaciones.index.astype(int))
    return productos[:top_n]
