import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import unicodedata
import re

# Funciones
def getPage(url):
    driver = webdriver.Firefox()
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    driver.quit()
    return soup

norm = lambda x: unicodedata.normalize("NFKD",x)

def cleaning_soup (text):
    list_s = re.split('Platos: | Quesos: | Postres: | Temperatura: | Vaso/Copa: ', norm(text))
    return list_s

def split_heads (text):
    list_s = re.split(', | o | or ', norm(text))
    return list_s

def change_val (df, column, lst_ch, ch_lst):
    for i, e in enumerate (lst_ch):
        df.loc[(df[column] == e), column] = ch_lst[i]
    return df

# Scrapping
soup = getPage('https://www.thebeertimes.com/maridaje-con-cerveza/')

heads = soup.select('#post-2849')[0].find_all('h3')[15:]
contents1 = soup.select('#post-2849')[0].find_all('p')[53:71]
contents2 = soup.select('#post-2849')[0].find_all('p')[72:82]
contents = contents1 + contents2

beers_list = []

for i in range (0, 28):
    texts = cleaning_soup (contents[i].text.strip())
    head_spt = split_heads (heads[i].text.strip())
    for ind in range(0, len(head_spt)):
        beer_dict = {
            'Estilo': head_spt[ind],
            'Platos': texts[1],
            'Quesos': texts[2],
            'Postres': texts[3],
            'Temperatura': texts[4],
            'Vaso/Copa': texts[5]
        }
        beers_list.append(beer_dict)

df_scrapp = pd.DataFrame(beers_list)

list_change = ['Old', 'Sweet', 'American Wheat Ale', 'Double/Imperial IPA',
               'Amber/Red Ale', 'Scotch Ale/Wee Heavy', 'Maibock/Pale Bock']

change_list = ['Old Ale', 'Sweet Stout', 'Wheat Ale', 'Double / Imperial IPA',
               'Amber / Red Ale', 'Scotch Ale / Wee Heavy', 'Maibock / Pale Bock']

change_val(df_scrapp, 'Estilo', list_change, change_list)

df_scrapp.to_csv('Outputs/scrapp_code.csv', index = False)




