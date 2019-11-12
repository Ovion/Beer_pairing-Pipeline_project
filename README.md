Pipeline_Project
================

Este proyecto tenía como fin utilizar distintos archivos con funciones definidas dentro de ellos y encadenarlos en una función principal. Dicha función se debe ejecutar desde la terminal con dos argumentos y que te de una respuesta.

Maridaje de cervezas
--------------------

En este proyecto partí de dos dataset, uno con nombres, tipos, graduación... de la cerveza y otro con las cerveceras donde hay dichas cervezas, con información adicional de la ciudad y el estado de EEUU en el que se encuentra. Dichos dataset se pueden encontrar [aquí](https://www.kaggle.com/nickhould/craft-cans)

Para ampliar información realicé un 'scrappeo' de una [página web de maridajes de cerveza](https://www.thebeertimes.com/maridaje-con-cerveza/). Tuve que utilizar Selenium para poder acceder a todos los datos que quería.

Una vez sacados todos los datos realicé una limpieza de dichos datos, el orden de ejecución sería el siguiente:
1. combine_dataset.py.
   En este combino los dos dataset de nombres de cerveza y cervecerías en único dataset
2. scrapping.py
  En este otro realizo el scrapp de la página web
3.cleaning_ds.py
  Aquí realizo la limpieza de ambos dataset

Hasta aquí todo es crear una serie de datos que utilizaré en mi función main.py

### main.py
Esta función toma una "función" en este caso -c o --cerv y toma dos valores:
state: el cual debe ser las siglas de un estado de EEUU, los parámetros válidos son:
  



