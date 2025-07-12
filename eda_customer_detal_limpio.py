
"""
Limpieza automática y EDA para customer-details.xlsx
Cambio nombre de columnas para hacerlas más legibles y utilizo como variable objetivo el ingreso anual.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Primer paso: Cargar los datos desde el archivo y renombras columans paraa hacerlas más legibles

df = pd.read_excel('customer-details.xlsx')


df = df.rename(columns={
    'Income': 'Ingreso Anual',
    'Kidhome': 'Niños Hogar',
    'Teenhome': 'Adoles. Hogar',
    'NumWebVisitsMonth': 'V. Web Mes',
  
})

# Segundo paso: Remplazamos los valores nulos por N/A en las columnas que tengan más de un 10% de 
# valores nulos entrre sus datos, y convertimos las columnas numéricas a tipo float, sin tocar las columna de 
# Id, para conservar los datos de identificación.
cols_con_nulos = df.columns[df.isnull().mean() > 0.10].tolist()
for col in cols_con_nulos:
    df[col] = df[col].fillna('N/A')


for col in ['Ingreso Anual', 'Niños Hogar', 'Adoles. Hogar', 'V. Web Mes']:
    df[col] = pd.to_numeric(df[col], errors='coerce')


print('--- Información general ---')
print(df.info())
print('\n--- Porcentaje de valores nulos ---')
print(df.isnull().mean().sort_values(ascending=False))
print('\n--- Estadística descriptiva ---')
print(df.describe(include='all'))

# Tercer paso: Hacemos un análisis de los datos. Visualizamos la distribución de las variables numéricas
# y observamos las relaciones entre nuestra variable objetivo 'Ingreso Anual' y el resto de variables
# numéricas.

# Histograma de Ingreso Anual
plt.figure(figsize=(8,4))
sns.histplot(df['Ingreso Anual'].dropna(), bins=30, kde=True)
plt.title('Distribución de Ingreso Anual')
plt.xlabel('Ingreso Anual')
plt.show()

# Histogramas para el resto de las columnas numéricas. Reducimos el tamaño de los gráficos
# para que a un número manejable de columnas, para que el gráfico sea legible.
for col in ['Niños Hogar', 'Adoles. Hogar', 'V. Web Mes']:
    plt.figure(figsize=(8,4))
    sns.histplot(df[col].dropna(), bins=15, kde=False)
    plt.title(f'Distribución de {col}')
    plt.xlabel(col)
    plt.show()


# Relación Ingreso Anual contra Niños Hogar
plt.figure(figsize=(6,4))
sns.boxplot(x='Niños Hogar', y='Ingreso Anual', data=df)
plt.title('Ingreso Anual según Niños Hogar')
plt.show()

# Relación Ingreso Anual contra Adoles. Hogar
plt.figure(figsize=(6,4))
sns.boxplot(x='Adoles. Hogar', y='Ingreso Anual', data=df)
plt.title('Ingreso Anual según Adoles. Hogar')
plt.show()

# Relación Ingreso Anual contra V. Web Mes
plt.figure(figsize=(6,4))
sns.boxplot(x='V. Web Mes', y='Ingreso Anual', data=df)
plt.title('Ingreso Anual según Visitas Web al Mes')
plt.show()

plt.figure(figsize=(6,4))
sns.scatterplot(x='V. Web Mes', y='Ingreso Anual', data=df)
plt.title('Dispersión entre Ingreso Anual y Visitas Web al Mes')
plt.show()

# Relación entre 'ingreso anual' y las demás variables numércias  
corrs = df[['Ingreso Anual', 'Niños Hogar', 'Adoles. Hogar', 'V. Web Mes']].corr()
plt.figure(figsize=(5,4))
sns.heatmap(corrs, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlación entre Ingreso Anual y otras variables')
plt.show()

# Pruebo una relación cruzada entre 'ingreso anual' y el resto de variables
print('\n--- Media de Ingreso Anual por Niños Hogar ---')
print(df.groupby('Niños Hogar')['Ingreso Anual'].mean())
print('\n--- Media de Ingreso Anual por Adoles. Hogar ---')
print(df.groupby('Adoles. Hogar')['Ingreso Anual'].mean())
print('\n--- Media de Ingreso Anual por V. Web Mes ---')
print(df.groupby('V. Web Mes')['Ingreso Anual'].mean())

# Cuarto Paso: Guardo el conjunto de datos limpio para poder cargarlo con
# el resto de datos a evaluar.
df.to_excel('customer-details-limpio.xlsx', index=False)