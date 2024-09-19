import requests

# URL del PDF
pdf_url = 'https://situr.boyaca.gov.co/wp-content/uploads/2022/08/ESTADISTICAS-PUNTOS-PIT.pdf'
pdf_path = 'archivo.pdf'


response = requests.get(pdf_url)
with open(pdf_path, 'wb') as f:
    f.write(response.content)





