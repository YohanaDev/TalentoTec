
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://colombia.inaturalist.org/places/boyaca-co"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

tabla = soup.find("table")
filas = tabla.get("tr")
datos = []
for fila in filas:
    celdas = fila.find_all("td")
    fila_datos = [celda.text.strip() for celda in celdas]
    datos.append(fila_datos)

df = pd.DataFrame(datos)
print (df)
df.to_csv("datos.csv", index=False)