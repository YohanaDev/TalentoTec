from flask import Flask, render_template
# import web_scraping_biodiversidad 
#aqui el objeto 
app = Flask (__name__)
#aqui las rutas
@app.route('/')
def ir_a_Nabr():
   return render_template('Nabr.html')

@app.route('/fauna')
def ir_a_fauna():
   return render_template('fauna.html')


@app.route('/flora')
def ir_a_flora():
   return render_template('flora.html')

@app.route('/protege')
def ir_a_protege():
   return render_template('protege.html')

@app.route('/map')
def ir_a_map():
   return render_template('map.html')

@app.route('/informacion')
def ir_a_informacion():
   return render_template('informacion.html')

@app.route('/estadistica')
def ir_a_estadistica():
   return render_template('estadistica.html')

if __name__ == '__main__':
   app.run(debug=True,port=5000)

