import requests
from bs4 import BeautifulSoup


sitioweb = 'https://cifras.biodiversidad.co/boyaca'
resultado = requests.get(sitioweb)

if resultado.status_code == 200:
    contenido = resultado.content

    soup = BeautifulSoup(contenido, "html.parser")
    elementos = soup.find_all('li')  #
    
    html_content = "<html><head><title>Datos Importantes</title></head><body>"
    html_content += "<h1>Los 10 Datos Más Importantes</h1><ul>"
    
    for i, elemento in enumerate(elementos[:10]):
        html_content += f"<li>{elemento.get_text(strip=True)}</li>"
    
    html_content += "</ul></body></html>"
    
    with open("datos_importantes.html", "w", encoding="utf-8") as file:
        file.write(html_content)
    
    print("Datos guardados en 'datos_importantes.html'.")
else:
    print(f"Error al obtener el contenido: {resultado.status_code}")




