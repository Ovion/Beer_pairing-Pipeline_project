import argparse
import os
import pandas as pd
import re

import Src.datasets as ds
import Src.pdf as pdf

def valid_state(c):
    '''Validación de un estado perteneciente a los EEUU '''
    lst_state = ds.get_lst_states()
    if c in lst_state:
        return c
    else:
        sms = 'Estado de USA no valido. Use uno de los siguientes: '+str(lst_state)
        raise argparse.ArgumentTypeError(sms)

def valid_beer(c):
    '''Validación de un tipo de cerveza que está en mi base de datos '''
    lst_beer = ds.get_lst_beers()
    if c in lst_beer:
        return c
    else:
        sms = 'Tipo de cerveza no valido, fijese bien en las mayusculas. Use uno de los siguientes: '+str(lst_beer)
        raise argparse.ArgumentTypeError(sms)

def parse():
    parser = argparse.ArgumentParser() #Analizador de argumentos
    grupo = parser.add_mutually_exclusive_group() # grupo mutuamente excluyente (solo una operacion)

#    grupo.add_argument ('-maridaje', help='Dado un tipo de cerveza, te indico con qué va bien', action='store_true')
    grupo.add_argument ('-c', '--cerv', help='Dado un tipo de cerveza y un estado de USA te indico la cervecería y el maridaje de dicha cerveza', action='store_true')

    parser.add_argument('state', help='Siglas del estado de USA (ver reedme), e.g. "CA" para California', type=valid_state)
    parser.add_argument('style', help='Tipo de cerveza (ver reedme), e.g. Pale Ale', type=valid_beer)

    return parser.parse_args()

def main():
    args=parse()
    print(args)
    print ('\n ----- \n')
    if args.cerv:
        df_maridaje = ds.get_ds_maridaje (args.style)
        print ("Tabla de maridaje: \n")
        print (df_maridaje)
        print ('\n ----- \n')
        df_cerv = ds.get_ds_cerveceria (args.style, args.state)
        print ("Tabla de cervecerías: \n")
        print (df_cerv)
        pdf.create_pdf(df_maridaje, df_cerv, args.state)
    else:
        print ('Error: se requiere un argumento para realizar la accion.')

if __name__ == '__main__':
    main()








