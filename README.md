<img width="178" height="150" alt="image" src="https://github.com/user-attachments/assets/db49c61b-2501-4223-bcba-a90fd6e80024" />

# DATA ANALYTICS CON PYTHON.
Trabajo para el análisis de dos conjuntos de datos mediante Python.

# 1. Descripción del proyecto.

El proyecto encomendado consiste en analizar dos archivos en diferentes formatos, CSV y Excel, mediante Python. Realizaremos una limpieza de los datos originales
y analizaremos esos datos para encontrar posibles valores relevantes.

# 2. Estructura del proyecto:

Inicialmente, contamos con los siguientes archivos:

 - Bank-additional: es un archivo CSV con los datos en crudo. Estos datos hacen referencia a las campañas y contactos que ha realizado el banco con
   diferentes clientes.

 - Customer-details: es un archivo excel con los datos en crudo. El archivo hace referencia a los datos personales de varios clientes.

Una vez realizado el análisis sobre estos archivos iniciales, tenemos los siguientes archivos para evaluar:

- Bank-additional-limpio: Archivo final con los cambios realizados.

- eda_Bank_additional_limpio: Archivo Python con el análisis del archivo inicial. En este mismo Script se generan los gráficos del análisis, que guardamos    en una carpeta a parte para su carga por separado.

- customer-details-limpio-multisheet: Archivo final después de realizar el análisis sobre el archivo inicial "customer-details".

- eda_cust_detal_limpio: Archivo Python con el análisis del archivo inicial. En este caso, y para no sobresaturar de información, los gráficos generados en   el análisis, se guardan en una carpeta aparte, que he subido al repositorio.

- eda_bank_add_output: carpeta de archivos en donde guardamos los gráficos generados por el script "eda_bank_additional_limpio"

- eda_multisheet_output: carpeta de archivos en donde guardamos los gráficos generados por el script "eda_cust_detal_limpio"

Una vez que hemos visto los archivos con los que he trabajado y los que he obtenido, revisamos los scripts que he realizado para llevar a cabo el análisis:

Para comenzar el análisis, seleccionamos el archivo que queremos analizar, en mi caso empiezo por el "bank_additional", y cargamos la ruta. El primer paso que realizo es cambiar los nombres de las columnas para hacerlos más legibles o intuitivos para mi. Con estos nombres, será más fácil trabajar.


<img width="670" height="223" alt="image" src="https://github.com/user-attachments/assets/58baa6fa-571f-402b-a180-eaccade08d60" />

Después de modificar los nombres de las columnas, comienzo a modificar el formato de los datos para adaptarlos al análisis que quiero realizar. Cambio el "puno" por la "coma" para la separación de decimales, las variables de tipo string las paso a mayúsculas, para darles más visibilidad y tomo como referencia para el análisis, la columna denominada 'y', ya que esta indica si el cliente del banco ya tiene un depósito o no lo tiene.


<img width="731" height="440" alt="image" src="https://github.com/user-attachments/assets/bb7f3621-af5d-456e-a696-73ca33f5c029" />


Una vez que hemos modificado el formato de los datos que nos interesan, paso a revisar los valores nulos del conjunto de datos. Considero que si hay más de un 10% de valores nulos en una columna, son demasiados, por lo que los reemplazo por N/A.


<img width="658" height="208" alt="image" src="https://github.com/user-attachments/assets/fd03ec30-9e7d-47c7-86db-0ea0b85a35a5" />


Con los pasos anteriores, termino con la modificación de los datos, y comienzo a realizar un análisis de los mismos. Primero me centro en nuestra variable de referencia, 'y'. Hago un análisis para ver su distribución


<img width="597" height="136" alt="image" src="https://github.com/user-attachments/assets/1b04b2f3-dc4b-4ceb-8f4f-bcfde80109b6" />

<img width="498" height="58" alt="image" src="https://github.com/user-attachments/assets/c4b9a02a-10d4-49fb-b77d-fc9e7169226e" />

Después de esto, comienzo a realizar un análisis de las diferentes variables y a comprobar las relaciones que existen entre ellas y también con la variable de referencia.


<img width="607" height="105" alt="image" src="https://github.com/user-attachments/assets/b4d27831-207b-41b8-b03f-7f51224ff612" />


<img width="714" height="181" alt="image" src="https://github.com/user-attachments/assets/216ba4eb-fab3-4440-aa33-09d0e736ba1a" />


<img width="580" height="471" alt="image" src="https://github.com/user-attachments/assets/494d5aa9-0c22-4205-9904-bee15bc5ba40" />


<img width="605" height="260" alt="image" src="https://github.com/user-attachments/assets/981edf8e-7298-48ef-bc05-6911b40e3229" />


<img width="776" height="227" alt="image" src="https://github.com/user-attachments/assets/2d40ce37-3ebb-4cbe-8e04-3767193cccf0" />


<img width="839" height="327" alt="image" src="https://github.com/user-attachments/assets/7049ec6d-1cda-44f5-9102-4c96ebd82570" />


Una vez que termino con el análisis del archivo 'bank-additional', comienzo a realizar un análisis similar con el archivo 'customer-details'. Para este caso, es un poco diferente, porque el archivo que tengo que analizar es un archivo Excel y además los datos están agrupados por años en tres hojas diferentes, por lo que tengo que realizar el análisis en esas tres hojas.

Al igual que el anterior, comienzo por cargar el archivo, en este caso también le doy un nombre al archivo final que se extraerá después del análisis y cambio el nombre de las columnas para hacerlas más legibles o intuitivas para poder analizarlas.


<img width="832" height="325" alt="image" src="https://github.com/user-attachments/assets/f98eaf24-9854-4e49-b032-03d4cbcb23e8" />


En esta ocasión, comienzo con el análisis de los valores nulos. Siguiendo el mismo método que el archivo anterior, entiendo que más de un 10% de valores nulos en una columna son demasiados, y los cambio por N/A.


<img width="684" height="87" alt="image" src="https://github.com/user-attachments/assets/d98d7159-42a5-4a1e-a55d-adf9d92692d3" />


Posteriormente comienzo a convertir los datos de las columnas a valores numéricos exceto la columna de id, que la dejo sin modificar para mantenerla como referencia de identificación, y realizao un resumen general de los datos.

<img width="772" height="338" alt="image" src="https://github.com/user-attachments/assets/d274cea4-1c4f-404c-8ae5-2c7e3040e7c5" />

Una vez modificado los datos, procedo a realizar el análisis de los mismos mediante diferentes gráficos que guardo en una carpeta a parte para no sobrecargar el script.


<img width="821" height="429" alt="image" src="https://github.com/user-attachments/assets/821c9b98-cd9a-475d-b71e-1ae9490f6ac8" />


<img width="825" height="300" alt="image" src="https://github.com/user-attachments/assets/2be297ed-e405-465f-ad99-cddf117329e5" />


<img width="886" height="330" alt="image" src="https://github.com/user-attachments/assets/79397b17-1efa-454e-bcb8-c676c9bd3133" />


Una vez realizados estos gráficos, guardamos el análisis.


# 3. Instalación y requisitos.

Para la realización de este proyecto, he utilizado las siguientes herramientas:

- Archivo CSV y Excel dados para analizar.

- Visual Studio Code, con la instalación de las siguientes librerías:

    -- Para el archivo "bank-additional":

    <img width="304" height="99" alt="image" src="https://github.com/user-attachments/assets/29a5c26b-2bbb-4227-a5ae-e436e6025c44" />


    -- Para el archivo "customer-details":

    <img width="338" height="105" alt="image" src="https://github.com/user-attachments/assets/8dbbbcbb-7bcd-4247-a884-21531646266c" />


# 4. Contribuciones y autor.

Cualquier tipo de contribución a este trabajo es bienvenida para mejorarlo en todo lo posible.

Óscar Pérez Chico

<img width="174" height="33" alt="image" src="https://github.com/user-attachments/assets/a1edacb1-e22d-467e-96e9-2142379615d1" />


