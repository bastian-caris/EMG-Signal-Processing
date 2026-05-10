import pandas as pd
import glob
import os

# Buscar relativo al script, no al directorio actual
base = os.path.dirname(os.path.abspath(__file__))
archivos = sorted(glob.glob(os.path.join(base, "../Data/*Nmar.csv")), 
                  key=lambda x: int(os.path.basename(x).replace("Nmar.csv", "")))

print(f"Archivos encontrados: {archivos}")  # verificar

dfs = []
for path in archivos:
    df = pd.read_csv(path)
    df["sujeto"] = os.path.basename(path).replace(".csv", "")
    dfs.append(df)

datos = pd.concat(dfs, ignore_index=True)
datos = datos[["sujeto", "Time_s", "RF", "BF", "VM", "ST", "FX"]]

datos.to_csv(os.path.join(base, "../Data/datos.csv"), index=False)

print(f"Filas totales: {len(datos)}")
print(f"Sujetos: {datos['sujeto'].unique()}")
print(datos.head())
