"""
Limpieza y análisis del archivo customer-details.xlsx
Al final del análisis, generamos un archvi excel con los resultados y los g´raficos aparte
para no sobrecargar el archivo final ni este script.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Nombres de los archivos de entrada y salida y cambio de nombres en las columnas para hacerlas 
# más legibles.
# Creamos una carpeta separada para guardar los gráficos que hemos generado y no sobrecargar el análisis.
# Para este análisis, cargamos todas las hojas qdel archivo Excel iniicial (2012, 2013 y 2014)
# y hacemos un resumen para cada una de ellas.
INPUT_FILE = "customer-details.xlsx"
OUTPUT_FILE = "customer-details-EDA-multisheet.xlsx"
RENAME_DICT = {
    'Income': 'Ingreso Anual',
    'Kidhome': 'Niños Hogar',
    'Teenhome': 'Adoles. Hogar',
    'NumWebVisitsMonth': 'V. Web Mes',
}

OUTPUT_DIR = "eda_multisheet_output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

xls = pd.ExcelFile(INPUT_FILE)
writer = pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl")


summary_dfs = {}

for sheet_name in xls.sheet_names:
    df = xls.parse(sheet_name)
    df = df.rename(columns=RENAME_DICT)

    # Identificamos nulos y cambiamos por N/A si hay más de un 10% de nulos en la columna
    cols_con_nulos = df.columns[df.isnull().mean() > 0.10].tolist()
    for col in cols_con_nulos:
        df[col] = df[col].fillna('N/A')

    # convertimos los datos de las columans a valores numéricos,
    # excepto la columna id, para mantenerla como referencia de identificación
    for col in ['Ingreso Anual', 'Niños Hogar', 'Adoles. Hogar', 'V. Web Mes']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # Guardamos los datos en una hoja nueva
    df.to_excel(writer, sheet_name=sheet_name[:31], index=False)

    # Hacemos resumen de los datos generales, % de valores nulos y estadística descritiva.
    stats_str = []
    stats_str.append(f"--- Información general ({sheet_name}) ---")
    stats_str.append(str(df.info()))
    stats_str.append('\n--- Porcentaje de valores nulos ---')
    stats_str.append(str(df.isnull().mean().sort_values(ascending=False)))
    stats_str.append('\n--- Estadística descriptiva ---')
    stats_str.append(str(df.describe(include='all')))

    # Guardamos ese resumen para utilizarlo en cada hoja
    summary_dfs[sheet_name] = "\n".join(stats_str)

    # Hacemos el análisis gráfico:

    # Histograma Ingreso Anual (variable de referencia). Hacemos el gráfico con tamaño reducido 
    # para hacerlo más legible y no sobrecargarlo.
    if 'Ingreso Anual' in df.columns:
        plt.figure(figsize=(8,4))
        sns.histplot(df['Ingreso Anual'].dropna(), bins=30, kde=True)
        plt.title(f'Distribución de Ingreso Anual ({sheet_name})')
        plt.xlabel('Ingreso Anual')
        plt.savefig(os.path.join(OUTPUT_DIR, f"hist_ingreso_{sheet_name}.png"))
        plt.close()

    # Hsitogramas para el resto de columnas numéricas. También reducimos el tamaño por cuestión 
    # de legibilidad y saturación de datos.
    for col in ['Niños Hogar', 'Adoles. Hogar', 'V. Web Mes']:
        if col in df.columns:
            plt.figure(figsize=(8,4))
            sns.histplot(df[col].dropna(), bins=15, kde=False)
            plt.title(f'Distribución de {col} ({sheet_name})')
            plt.xlabel(col)
            plt.savefig(os.path.join(OUTPUT_DIR, f"hist_{col}_{sheet_name}.png"))
            plt.close()

    # Hacemos unos nuevos tipos de gráficos: Boxplots y scatter para ver la relación entre ellos.
    if 'Ingreso Anual' in df.columns:
        for col in ['Niños Hogar', 'Adoles. Hogar', 'V. Web Mes']:
            if col in df.columns:
                plt.figure(figsize=(6,4))
                sns.boxplot(x=col, y='Ingreso Anual', data=df)
                plt.title(f'Ingreso Anual según {col} ({sheet_name})')
                plt.savefig(os.path.join(OUTPUT_DIR, f"box_{col}_{sheet_name}.png"))
                plt.close()
        if 'V. Web Mes' in df.columns:
            plt.figure(figsize=(6,4))
            sns.scatterplot(x='V. Web Mes', y='Ingreso Anual', data=df)
            plt.title(f'Dispersión entre Ingreso Anual y Visitas Web al Mes ({sheet_name})')
            plt.savefig(os.path.join(OUTPUT_DIR, f"scatter_webmes_{sheet_name}.png"))
            plt.close()

    # Realizamos un heatmap para ver la correlación entre las variables numéricas y seleccionamos 
    # aquellas columnas que nos interesan más
    corr_cols = [c for c in ['Ingreso Anual', 'Niños Hogar', 'Adoles. Hogar', 'V. Web Mes'] if c in df.columns]
    if len(corr_cols) > 1:
        corrs = df[corr_cols].corr()
        plt.figure(figsize=(5,4))
        sns.heatmap(corrs, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title(f'Correlación entre variables ({sheet_name})')
        plt.savefig(os.path.join(OUTPUT_DIR, f"heatmap_corr_{sheet_name}.png"))
        plt.close()

    # Agrupamos por columnas y realizamos el cálculo de la media del nuestra variable objetivo.
    for col in ['Niños Hogar', 'Adoles. Hogar', 'V. Web Mes']:
        if col in df.columns and 'Ingreso Anual' in df.columns:
            stats_str.append(f"\n--- Media de Ingreso Anual por {col} ---")
            stats_str.append(str(df.groupby(col)['Ingreso Anual'].mean()))

    # Guardamos el resumen realziado para los datos.
    summary_df = pd.DataFrame({"Resumen": [ "\n".join(stats_str) ]})
    summary_df.to_excel(writer, sheet_name=f"{sheet_name[:27]}_EDA", index=False)

writer.close()

print(f"Archivo generado: {OUTPUT_FILE}")
print(f"Gráficos guardados en: {OUTPUT_DIR}")