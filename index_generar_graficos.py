from flask import Flask, render_template, send_file
import io
import matplotlib.pyplot as plt
import os

app_flask = Flask(__name__)

@app_flask.route('/')
def ir_a_datos():
   
    nombres = ['Zonotrichia capensis', 'Tyrannus melancholicus', 'Turdus fuscater', 'Coragyps atratus', 'Troglodytes aedon', 'Campomanesia lineatifolia', 'Vaccinium meridionale']
    cifras = [7.733, 7.441, 7.267, 5.683, 5.329, 2.663, 2.402,]  # Ajusta los valores según tus datos
    
    # Crear el gráfico de barras
    fig, ax = plt.subplots()
    ax.bar(nombres, cifras)
    ax.set_xlabel('Elementos')
    ax.set_ylabel('Cifras')
    ax.set_title('Datos Importantes de Biodiversidad en Boyacá')
    plt.xticks(rotation=45, ha='right')

   
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

   
    url1 = 'static/imagenes/grafico2.png'
    if not os.path.exists('static/imagenes'):
        os.makedirs('static/imagenes')
    
    with open(url1, 'wb') as f:
        f.write(buf.getvalue())

    
    return render_template('datos_importantes.html', grafico=url1)

if __name__ == '__main__':
    app_flask.run(debug=True, port=5000)



