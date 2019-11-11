import pandas as pd
import re

# Más funciones de limpieza:
def sub_to_nothing (df, column, lstcc):
    for e in lstcc:
        df[column] = df[column].str.replace (e, '')
    return df

def change_val (df, column, lst_ch, ch_lst):
    for i, e in enumerate (lst_ch):
        df.loc[(df[column] == e), column] = ch_lst[i]
    return df

def other_beers (df, column, lst_uni):
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

df_combine = pd.read_csv('Outputs/combine.csv')

lst_cc = ['\(.+\)','American','Belgian','Baltic','Berliner','English',
          'German','Czech','Euro','Munich','Irish','Russian','^\s','\s$']

df_combine = sub_to_nothing(df_combine, 'style', lst_cc)

lst_change = ['IPA', 'Pilsener', 'Pale Wheat Ale', 'Extra Special / Strong Bitter', 'Irish Red Ale',
             'Scottish Ale', 'Scotch Ale', 'Tripel', 'Dark Ale', 'Milk / Sweet Stout',
             'Double / Imperial Stout', 'Maibock / Helles Bock', 'Vienna Lager', 'Dunkel Lager', 'Dunkelweizen',
             'Bock']

change_lst = ['India Pale Ale', 'Pilsner', 'Wheat Ale', 'British-Style Bitter', 'Amber / Red Ale',
             'Scotch Ale / Wee Heavy', 'Scotch Ale / Wee Heavy', 'Abbey Tripel', 'Old Ale', 'Sweet Stout',
             'Imperial Stout', 'Helles', 'Vienna', 'Dunkel', 'Dunkel',
             'Maibock / Pale Bock']

change_val(df_combine, 'style', lst_change, change_lst)

df_scrpp = pd.read_csv('Outputs/scrapp_code.csv')

list_uniq = [e for e in df_scrpp['Estilo']]

df_clean = other_beers(df_combine, 'style', list_uniq)




df_clean.to_csv('Outputs/combine_code_cc.csv')