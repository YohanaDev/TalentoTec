import requests
import pandas as pd

url = "https://api.gbif.org/v1/occurrence/search"


params = {
    "country": "CO",  
    "stateProvince": ["Cundinamarca", "Boyacá"],  
    "limit": 200,  
}


response = requests.get(url, params=params)


if response.status_code == 200:
    data = response.json()  

   
    tipos = []
    especies = []
    lugares = []
    departamentos = []

 
    for record in data['results']:
        tipo = record.get("class", "No disponible")
        especie = record.get('species', 'Especie no disponible')
        lugar = record.get('country', 'Lugar no disponible')
        departamento = record.get('stateProvince', 'Fecha no disponible')

        tipos.append(tipo)
        especies.append(especie)
        lugares.append(lugar)
        departamentos.append(departamento)

 
    df = pd.DataFrame({
        'Tipo': tipos,
        'Especie': especies,
        'Lugar': lugares,
        'Departamento': departamentos
    })

 
    df.to_csv('resultados_especies.csv', index=False)
    import os
    print(os.getcwd())

    print(df.head(200))
    
else:
    print(f"Error: {response.status_code}")



