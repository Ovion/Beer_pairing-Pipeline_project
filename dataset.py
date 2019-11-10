import pandas as pd
import re

# Funciones de limpieza

def DF_drop_by_indx(df, lst, indx):
    return df.drop(lst, inplace = True, axis = indx)


# En primer lugar mi data set consta de 2 .csv
df_beers = pd.read_csv('Inputs/beers.csv')
df_breweries = pd.read_csv('Inputs/breweries.csv')

# Limpieza básica del df_beers
lst_colmn_beers = ['abv', 'ibu', 'Unnamed: 0', 'id']
DF_drop_by_indx (df_beers, lst_colmn_beers, 1)

lst_row_beers = [566, 1554, 1555]
DF_drop_by_indx (df_beers, lst_row_beers, 0)

df_beers.ix[853, 'style'] = 'Scotch Ale'
df_beers.ix[853, 'name'] = 'Kilt Lifter'
df_beers.ix[866, 'style'] = 'Oktoberfest'

# Limpieza básica del df_breweries
df_breweries.rename(columns = {'Unnamed: 0': 'brewery_id',
                              'name': 'brewery_name'}, inplace=True)

df_combine = pd.merge(df_beers, df_breweries, how = 'inner', on = 'brewery_id')
df_combine.to_csv('Outputs/combine.csv')







