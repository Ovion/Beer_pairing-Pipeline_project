import pandas as pd
import re

# 3º archivo .py En este archivo realizo la limpieza del dataset ya combinado

# Más funciones de limpieza:
def sub_to_nothing (df, column, lstcc):
    '''Función para eliminar directamente de un dataframe'''
    for e in lstcc:
        df[column] = df[column].str.replace (e, '')
    return df

def change_val (df, column, lst_ch, ch_lst):
    '''Dado un df, una columna y dos listas, una con los valores que quieremos cambiar y otra con lo que queremos, cambio los valores
    se hace con el fin de que nuestro ds se parezca a lo que etengo scrappeado'''
    for i, e in enumerate (lst_ch):
        df.loc[(df[column] == e), column] = ch_lst[i]
    return df

def other_beers (df, column, lst_uni):
    '''Como tengo más tipos de cerveza en este ds que en el scrapp hice una función que elimine los tipos de cerveza que no tengo'''
    for e in df[column]:
        if e not in lst_uni:
            df.loc[(df[column] == e), column] = 'Others'
    return df

# No me funciona value_counts así que me la creo:
def unique_val_count (df, column):
    dicti={}
    for e in df[column]:
        dicti[e]=dicti.get(e,0)+1
    sort_dicti = sorted(dicti.items(), key=lambda kv: kv[1], reverse=True)
    return sort_dicti

# Cojo el df combinado
df_combine = pd.read_csv('Outputs/combine.csv')

# Esta es una lista que contiene 'cosas' que quiero quitar de la columna de estilo de cerveza
lst_cc = ['\(.+\)','American','Belgian','Baltic','Berliner','English',
          'German','Czech','Euro','Munich','Irish','Russian','^\s','\s$']

df_combine = sub_to_nothing(df_combine, 'style', lst_cc)

# A continuación hay dos listas, la primera contiene lo que quiero cambiar, la segunda por lo que lo quiero cambiar
lst_change = ['IPA', 'Pilsener', 'Pale Wheat Ale', 'Extra Special / Strong Bitter', 'Irish Red Ale',
             'Scottish Ale', 'Scotch Ale', 'Tripel', 'Dark Ale', 'Milk / Sweet Stout',
             'Double / Imperial Stout', 'Maibock / Helles Bock', 'Vienna Lager', 'Dunkel Lager', 'Dunkelweizen',
             'Bock']

change_lst = ['India Pale Ale', 'Pilsner', 'Wheat Ale', 'British-Style Bitter', 'Amber / Red Ale',
             'Scotch Ale / Wee Heavy', 'Scotch Ale / Wee Heavy', 'Abbey Tripel', 'Old Ale', 'Sweet Stout',
             'Imperial Stout', 'Helles', 'Vienna', 'Dunkel', 'Dunkel',
             'Maibock / Pale Bock']

change_val(df_combine, 'style', lst_change, change_lst)

# Maldita columna de states, me llevó por el camino de la amargura... por el espacio, aquí se lo quito
lst_cc_state = ['^\s']
df_combine = sub_to_nothing(df_combine, 'state', lst_cc_state)

# Aquí cojo el csv del scrapp para filtar el ds de cervezas a los estilos scrappeados
df_scrpp = pd.read_csv('Outputs/scrapp_code.csv')

list_uniq = [e for e in df_scrpp['Estilo']]

df_clean = other_beers(df_combine, 'style', list_uniq)

df_clean.to_csv('Outputs/combine_code_cc.csv', index = False)