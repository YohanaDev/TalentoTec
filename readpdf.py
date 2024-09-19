import pdfplumber
import re

# Ruta al archivo PDF
pdf_path = 'archivo.pdf'

# Expresión regular para detectar cifras
regex_cifras = re.compile(r'\d+[\.,]?\d*')

# Lista para almacenar datos con cifras
datos_con_cifras = []

# Leer el PDF
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        texto = page.extract_text()
        if texto:
            for linea in texto.split('\n'):
                if regex_cifras.search(linea):
                    datos_con_cifras.append(linea)

# Guardar los datos en un archivo HTML
html_content = "<html><head><title>Datos Importantes</title></head><body>"
html_content += "<h1>Datos con Cifras</h1><ul>"

for i, dato in enumerate(datos_con_cifras):
    html_content += f"<li>{dato}</li>"

html_content += "</ul></body></html>"

with open("datos.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("Datos guardados en 'datos.html'.")
