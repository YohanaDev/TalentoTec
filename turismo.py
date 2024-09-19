from flask import Flask, render_template
import io
import matplotlib.pyplot as plt
import os

app_flask = Flask(__name__)

@app_flask.route('/')
def ir_a_datos():
   
    nombres = [
        'Cundinamarca', 'Antioquía', 'Tolima', 'Casanare', 'Valle del Cauca',
        'Santander', 'Meta', 'Arauca', 'Atlántico', 'Huila'
    ]
    cifras = [42, 34, 21, 13, 13, 11, 10, 7, 7, 6] 
    
    # Crear el gráfico de torta
    fig, ax = plt.subplots()
    colors = plt.cm.tab10(range(len(nombres)))  # Usar una paleta de colores
    wedges, texts, autotexts = ax.pie(
        cifras,
        labels=nombres,
        autopct='%1.1f%%',
        colors=colors,
        startangle=140,
        wedgeprops={'edgecolor': 'black'}
    )
    

    plt.setp(autotexts, size=10, weight="bold")
    plt.setp(texts, size=10)
    ax.set_title('Visitantes en Boyaca')
    
  
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    
   
    static_folder = 'static/imagenes'
    if not os.path.exists(static_folder):
        os.makedirs(static_folder)

    file_path = os.path.join(static_folder, 'grafico_torta.png')
    with open(file_path, 'wb') as f:
        f.write(buf.getvalue())
    
   
    return render_template('datos.html', grafico='imagenes/grafico_torta.png')

if __name__ == '__main__':
    app_flask.run(debug=True, port=5000)
