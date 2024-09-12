
import requests
from bs4 import BeautifulSoup

#Seleccionar el sitio web origen de los datos 
sitioweb = "https://www.radionacional.co/actualidad/medio-ambiente/animales-endemicos-cinco-especies-que-solo-se-ven-en-colombia"

resultado = requests.get(sitioweb)
print (f"El Requests obtenido :: {resultado}")

print (f"Tipo de objeto requests:: {type (resultado)}")

print ("Resultado.estatus_code:: " + str (resultado.status_code))

if(resultado.status_code == 200):
    contenido = resultado.content
    print ("Contenido no estrcuturado del sitio web")
    print (contenido)
    #Parsear el contenido del archivo 
    soup = BeautifulSoup (contenido, "html.parser")
    print ("Contenido ya estructurado del sitio web")
    print (soup)

    subtitulos = soup.find_all ("h2")
    print ("todoso los h2 del sitio web")
    print (Subtitulos)
