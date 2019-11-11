import pandas as pd

# Este es el dataset limpio
df_cc = pd.read_csv ('Outputs/combine_code_cc.csv')
df_cc.drop('Unnamed: 0', inplace = True, axis = 1)
# Este es el data set 'scrappeado' y limpio
df_scrapp = pd.read_csv ('Outputs/scrapp_code.csv')


def get_ds_maridaje (tipo, df=df_scrapp):
    '''Dado un tipo de cerveza, te devuelve un dataframe con su maridaje'''
    df_out = df.loc[(df['Estilo'] == tipo)]
    return df_out

def get_ds_cerveceria (tipo, estado, df=df_cc):
    '''Dado un estado y un tipo de cerveza te devuelve un dataframe
    con las cervezas del tipo presentes en una cervecería'''
    df_out = df_cc.loc [(df_cc['state']==estado)&(df_cc['style']==tipo)]
    return df_out

def get_lst_states (df=df_cc):
    lst_states = set([e for e in df['state']])
    return lst_states

def get_lst_beers (df=df_cc):
    lst_beers = set([e for e in df['style']])
    return lst_beers