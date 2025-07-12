
'''''
EDA y Limpieza del archivo bank-additional.csv
Incluyo cambio de nombre de columnas para hacerlas más legibles  y reemplazo de nulos por 'N/A' donde haya muchos.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Primer paso. Cargamos y hacemos un primer renombrado de columnas para que sean más 
# intuitivas.

# Ruta del archivo
df = pd.read_csv('bank-additional.csv', sep=',', encoding='utf-8', low_memory=False)

# Renombramos columnas con nombres más intiutivos
df = df.rename(columns={
    'default': 'incumplimiento',
    'housing': 'préstamo hipotecario',
    'emp.var.rate': 'variación empleo',
    'campaign': 'contactos campaña',
    'poutcome': 'campaña anterior'
})

# Formato de números. Indicamos la coma par separar decimales y el punto para los miles. También revisamos variables 
# booleannas y de fecha, así como las variables strings que las pasamoa a mayúsculas.
# Utilizamos  la columna 'y' como variable objetivo para indicar si el cliente tiene depósito o no.
cols_coma_decimal = ['variación empleo', 'cons.price.idx', 'cons.conf.idx', 'euribor3m']
for col in cols_coma_decimal:
    df[col] = df[col].astype(str).str.replace('"','').str.replace(',','.').replace('nan', np.nan)
    df[col] = pd.to_numeric(df[col], errors='coerce')


for col in ['age', 'duration', 'contactos campaña', 'pdays', 'previous', 'nr.employed', 'latitude', 'longitude']:
    df[col] = pd.to_numeric(df[col], errors='coerce')


for col in ['préstamo hipotecario', 'loan', 'incumplimiento']:
    df[col] = df[col].replace({'': np.nan, 'nan': np.nan}).astype(float)


df['date'] = pd.to_datetime(df['date'], errors='coerce', dayfirst=True)


cat_cols = ['job', 'marital', 'education', 'contact', 'campaña anterior', 'y']
for col in cat_cols:
    df[col] = df[col].astype(str).str.upper().replace('NAN', np.nan)


df['y'] = df['y'].replace({'YES':1, 'NO':0})

# Segundo paso. Remplazamos los valores nulos en columnas donde hay muchos
# y los sustituimos por N/A. Comenzamos a consiferar muchos nulos en aquellas columnas donde
# mñas del 10% de los datos son valores nulos.


umbral_nulos = 0.10
porc_nulos = df.isnull().mean()
cols_muchos_nulos = porc_nulos[porc_nulos > umbral_nulos].index.tolist()

for col in cols_muchos_nulos:
    # Ojo, si la variable es numérica, lo convertimos a string para poner 'N/A'
    if df[col].dtype != object:
        df[col] = df[col].astype('object')
    df[col] = df[col].fillna('N/A')

# Tercer paso. Nos centramos en la variable que hemos definido como objetivo, 'y', y hacemos un análisis
# para ver su distribución así como los otros datos que nos pueden interesar como comparación.

def plot_count(col, title):
    plt.figure(figsize=(8,4))
    sns.countplot(data=df, x=col, order=df[col].value_counts().index)
    plt.title(title)
    plt.xticks(rotation=45)
    plt.show()

# Distribución de la variable 'y'
plot_count('y', 'Distribución de la variable objetivo (y)')

# Hacemos un histograma por edad
plt.figure(figsize=(8,4))
sns.histplot(df['age'][df['age'] != 'N/A'].astype(float), bins=20, kde=True)
plt.title('Distribución de Edad')
plt.show()

# Otro histograma para ver las duraciones de los últimos conactos
# Convertimos 'duration' en númerico e ignoramos 'N/A'
plt.figure(figsize=(8,4))
sns.histplot(df['duration'][df['duration'] != 'N/A'].astype(float), bins=20, kde=True)
plt.title('Duración del último contacto')
plt.show()

# Distribución por profesiones
plot_count('job', 'Distribución de Profesiones')

# Distribución por nivel educativo

plot_count('education', 'Nivel Educativo')

# Datos del estado civil
# convertimos 'marital' a string para evitar problemas con el 'N/A'
plot_count('marital', 'Estado Civil')

# Cuarto paso. Hacemos un análisis de las relaciones que puede haber entre la variable 'y',
# y las demás variables del conjunto de datos.

# Relación de edad contra y
plt.figure(figsize=(8,4))
sns.boxplot(data=df[df['age'] != 'N/A'], x='y', y='age')
plt.title('Edad vs. Variable Objetivo')
plt.xticks([0,1], ['No', 'Sí'])
plt.show()

# Realación de Profesión contra y
plt.figure(figsize=(10,6))
sns.barplot(x='job', y='y', data=df, ci=None)
plt.title('Tasa de respuesta por profesión')
plt.xticks(rotation=45)
plt.show()

# Relación de Educación contra y
plt.figure(figsize=(10,6))
sns.barplot(x='education', y='y', data=df, ci=None)
plt.title('Tasa de respuesta por nivel educativo')
plt.xticks(rotation=45)
plt.show()

# Relación de Préstamo hipotecario contra y
plt.figure(figsize=(6,4))
sns.barplot(x='préstamo hipotecario', y='y', data=df, ci=None)
plt.title('Tasa de respuesta según si tiene préstamo hipotecario')
plt.xticks([0,1], ['No', 'Sí'])
plt.show()

# Relación entre variables numéricas y objetivo
num_cols = ['age', 'duration', 'contactos campaña', 'pdays', 'previous', 'variación empleo', 
            'cons.price.idx', 'cons.conf.idx', 'euribor3m', 'nr.employed']

# Tenemos que asegurarnos de que las columnas numéricas están en el formato correcto
df_corr = df[num_cols + ['y']].replace('N/A', np.nan)
corrs = df_corr.astype(float).corr()
plt.figure(figsize=(10,8))
sns.heatmap(corrs, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlación entre variables numéricas y objetivo')
plt.show()


# Relación entre contactos campaña contra y
plt.figure(figsize=(8,4))
sns.boxplot(x='y', y='contactos campaña', data=df[df['contactos campaña'] != 'N/A'])
plt.title('Número de contactos en campaña vs. respuesta')
plt.xticks([0,1], ['No', 'Sí'])
plt.show()

# Relación entre previous contra y
plt.figure(figsize=(8,4))
sns.boxplot(x='y', y='previous', data=df[df['previous'] != 'N/A'])
plt.title('Número de contactos previos vs. respuesta')
plt.xticks([0,1], ['No', 'Sí'])
plt.show()

# Quinto paso. Sacamos la información de los valores nulos.
print("\nValores nulos por columna:\n", df.isnull().mean().sort_values(ascending=False))

# Por último, guardamos este archivo con la limpieza que hemos hecho, para poder cargarlo en la documentación
# a entregar.
df.to_csv('bank-additional-limpio.csv', index=False)