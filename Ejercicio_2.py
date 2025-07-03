import pandas as pd
# Crear un dataframe
datos = {
    'ID': [1, 2, 3, 4, 5],
    'Producto': ['Camiseta', 'Pantalón', 'Zapatos', 'Camiseta', 'Sandalias'],
    'Categoría': ['Ropa', 'Ropa', 'Calzado', 'Ropa', 'Calzado'],
    'Precio': [25.0, 40.0, 60.0, 25.0, 20.0],
    'Cantidad': [2, 1, 1, 3, 5],
    'Fecha': ['2024-06-01', '2024-06-02', '2024-06-02', '2024-06-03', '2024-06-04']
}

df = pd.DataFrame(datos)
df['Fecha'] = pd.to_datetime(df['Fecha'])

print("DataFrame original:")
print(df)



