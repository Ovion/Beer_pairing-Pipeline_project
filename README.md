Pipeline_Project
================

Este proyecto tenía como fin utilizar distintos archivos con funciones definidas dentro de ellos y encadenarlos en una función principal. Dicha función se debe ejecutar desde la terminal con dos argumentos y que te de una respuesta.

Maridaje de cervezas
--------------------

En este proyecto partí de dos dataset, uno con nombres, tipos, graduación... de la cerveza y otro con las cerveceras donde hay dichas cervezas, con información adicional de la ciudad y el estado de EEUU en el que se encuentra. Dichos dataset se pueden encontrar [aquí](https://www.kaggle.com/nickhould/craft-cans)

Para ampliar información realicé un 'scrappeo' de una [página web de maridajes de cerveza](https://www.thebeertimes.com/maridaje-con-cerveza/). Tuve que utilizar Selenium para poder acceder a todos los datos que quería.

Una vez sacados todos los datos realicé una limpieza de dichos datos, el orden de ejecución sería el siguiente:
1. combine_dataset.py  
En este combino los dos dataset de nombres de cerveza y cervecerías en único dataset  

2. scrapping.py  
En este otro realizo el scrapp de la página web  

3. cleaning_ds.py  
Aquí realizo la limpieza de ambos dataset

Hasta aquí todo es crear una serie de datos que utilizaré en mi función main.py

### main.py
Esta función toma una "función" en este caso -c o --cerv y toma dos valores:
1. **state**: el cual debe ser las siglas de un estado de EEUU, los parámetros válidos son:  
'DC', 'TN', 'CO', 'ID', 'MA', 'DE', 'MI', 'AK', 'ND', 'TX', 'NC', 'NV', 'MS', 'AL', 'MO', 'CA', 'WI', 'VA', 'KY', 'VT', 'AZ', 'MN', 'ME', 'PA', 'OR', 'WA', 'NY', 'NE', 'UT', 'HI', 'RI', 'MT', 'WV', 'SC', 'WY', 'NJ', 'MD', 'LA', 'KS', 'OH', 'OK', 'IL', 'NM', 'SD', 'CT', 'IA', 'FL', 'IN', 'AR', 'NH', 'GA'

2. **style**: ha de ser un tipo de cerveza, se puede elegir entre:  
'Doppelbock', 'Schwarzbier', 'Sweet Stout', 'Dark Lager', 'Amber / Red Ale', 'Dunkel', 'Imperial Stout', 'Helles', 'Hefeweizen', 'Brown Ale', 'Maibock / Pale Bock', 'British-Style Bitter', 'Blonde Ale', 'Others', 'Dry Stout', 'Scotch Ale / Wee Heavy', 'Old Ale', 'Oatmeal Stout', 'Double / Imperial IPA', 'Altbier', 'Wheat Ale', 'Pilsner', 'Cream Ale', 'Strong Ale', 'Vienna', 'Witbier', 'Oktoberfest', 'Porter', 'India Pale Ale', 'Pale Ale', 'Abbey Tripel'

Hay que mencionar que los estilos que están separados por / deben ser introducidos juntos, ya que se considera una fusión de tipos.

En el propio main.py se verifica si la entrada de valores es correcta, asíque en caso de fallar, no te preocupes que te indicará que ha habido un error.  

También cabe destacar que igual hay alguna combinación de estado y estilo que no produce ningún resultado.
  
### datasets.py (dentro de Src)
Este archivo recibe los datos de main para devolver un resultado filtrado.

### ToDo in future
Creé el archivo pdf.py pero no me funciona bien ya que al introducir caracteres raros me da un error. Intentaré solucionarlo en el futuro.  

También me gustaría añadir un archivo.py con el que mandar un correo electrónico, pero después de tener el pdf creado para adjuntarlo.  

No obstante, hay una prueba en .txt con la salida de pantalla de la terminal


