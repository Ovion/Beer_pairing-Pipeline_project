import pandas as pd
import re
import os

# 1º .py En este archivo partiendo de 2 datasets los combino en uno solo que será el de partida
# Además hago una pequeña limpieza muy concreta para los data set

print ('dirección: ', os.getcwd())
# Funciones de limpieza
def DF_drop_by_indx(df, lst, indx):
    ''' Realizada únicamente con el fin de practicar más funciones'''
    return df.drop(lst, inplace = True, axis = indx)


# En primer lugar mi data set consta de 2 .csv
df_beers = pd.read_csv('Inputs/beers.csv') # En este tengo datos de cerveza, tipo, graduación y en qué cervecería se hace (por brewery id)
df_breweries = pd.read_csv('Inputs/breweries.csv') # En este otro dataset tengo la id de la cervecería, e información de la cervecería (ciudad y estado de EEUU)

# Limpieza básica del df_beers
lst_colmn_beers = ['abv', 'ibu', 'Unnamed: 0', 'id'] # Elimino algunas columnas que no voy a usar
DF_drop_by_indx (df_beers, lst_colmn_beers, 1)

lst_row_beers = [566, 1554, 1555] # Elimino algunas filas que tenían valores extraños
DF_drop_by_indx (df_beers, lst_row_beers, 0)

# En este apartado cambio manualmente un par de valores ya que en el nombre de la cerveza tenían el nombre
df_beers.loc[853, 'style'] = 'Scotch Ale'
df_beers.loc[853, 'name'] = 'Kilt Lifter'
df_beers.loc[866, 'style'] = 'Oktoberfest' # Este estaba vacío pero sé que es una que se sirve en el Oktober

# Limpieza básica del df_breweries, cambio algunos nombres de las columnas para poder hacer bien el merge a continuación
df_breweries.rename(columns = {'Unnamed: 0': 'brewery_id',
                              'name': 'brewery_name'}, inplace=True)

# Creación del nuevo dataset, mediante la función merge, y relacionando la id de las cervecerías
df_combine = pd.merge(df_beers, df_breweries, how = 'inner', on = 'brewery_id')
DF_drop_by_indx (df_combine, 'brewery_id', 1)

# Finalmente lo paso a un nuevo .csv con toda la información que necesito
df_combine.to_csv('Outputs/combine_code.csv', index = False)








