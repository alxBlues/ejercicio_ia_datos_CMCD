import pandas as pd

#Cargar Archivos CSV y JSON
df_csv = pd.read_csv('src/files/paises.csv')
df_json = pd.read_json('src/files/peliculas.json')

#Combinar los dataframes 
df_combinado = pd.concat([df_csv,df_json], ignore_index=True)

#Mostrar las primeras 5 filas
print(df_combinado.head())
#Mostrar tipos de datos y sus valores
print(df_combinado.info())
#Estadisticas Descriptivas 
print(df_combinado.describe())