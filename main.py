from flask import Flask,redirect,url_for,render_template

app= Flask(__name__)


@app.before_request
def before_request():
    print("Antes de la petición")
@app.after_request
def after_request(response):
    print("Despues de la petición")
    return response
@app.route('/')
def index():
    #encabezado="Encabezado desde Flask"
    print("Accediendo a la página principal")
    diccionario= {'titulo':'Acerca de', 'encabezado':'Acerca de  mi ...'}
    return render_template('index.html',datos=diccionario)
    #return "estamos en el Index o el inicio de la página"

@app.route('/redireccion')
@app.route('/redireccion/<string:sitio>')
def redireccion(sitio=None):
    if sitio is not None:
        return redirect (url_for('index'))
    else:
       return redirect (url_for('acercade'))  


@app.route('/acercade')
def acercade():
    #return "<h1>Acerca de mí:</h1>"
    return render_template('acercade.html')


@app.route('/condicionybucle')
def condicionybucle():
    datos={
        'edad':32,
        'nombres':['Hugo','Pepe','Paco','Luis']
    }
    return render_template('condicionybucle.html',datos=datos)


@app.route('/saludar')
@app.route('/saludar/<string:nombre>')
@app.route('/saludar/<string:nombre>/<int:edad>')
def saludar(nombre, edad):
    if edad!=None:
        return "Hola {} tienes {} años".format(nombre,edad)
    else:
        return f"""
        <h1>Hola,</h1>
        <h3>{nombre}</h3>
    """

@app.route ('/suma/<int:num1>/<int:num2>')
def suma(num1,num2):
    return f"""La suma es igual a : {suma}"""

def pagina_no_encontrada(error):
    return render_template('error/404.html',404)

if __name__== '__main__':
    app.register_error_handler(404,pagina_no_encontrada)
    app.run(debug=True, port=5000)