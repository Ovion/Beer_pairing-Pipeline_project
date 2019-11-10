import pandas as pd
import re

# Más funciones de limpieza:
def sub_to_nothing (df, column, lstcc):
    for e in lstcc:
        df[column] = df[column].str.replace (e, '')
    return df

def change_val (df, column, lst_ch, ch_lst):
    for i, e in enumerate (lst_ch):
        df.loc[(df[column] == e)] = ch_lst[i]
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
          'German','Czech','Euro','Munich','Viena','^\s','\s$']

df_combine = sub_to_nothing(df_combine, 'style', lst_cc)

lst_change = ['IPA', 'Pilsener', 'Pale Wheat Ale']
change_lst = ['India Pale Ale', 'Pilsner', 'Wheat Ale']
change_val(df_combine, 'style', lst_change, change_lst)

