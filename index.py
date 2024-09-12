from flask import Flask, render_template
# import web_scraping_biodiversidad 
#aqui el objeto 
app = Flask (__name__)
#aqui las rutas
@app.route('/Nabr')
def ir_a_Nabr():
   return render_template('Nabr.html')

@app.route('/fauna')
def ir_a_fauna():
   return render_template('fauna.html')

# @app.route('/fauna')
# def ir_a_fauna():
#     fauna_data = web_scraping_biodiversidad.scrape_fauna()
#     return render_template('fauna.html', fauna=fauna_data)

@app.route('/flora')
def ir_a_flora():
   return render_template('flora.html')

@app.route('/protege')
def ir_a_protege():
   return render_template('protege.html')

@app.route('/map')
def ir_a_map():
    return render_template('map.html')


if __name__ == '__main__':
   app.run(debug=True,port=5000)
