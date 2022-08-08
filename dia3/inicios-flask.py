from flask import Flask, request
from datetime import datetime
from flask_cors import CORS


# __name__ > variable propia de python que muestra si el archivo que estamos utilizando es el archivo principal del proyecto, si es el archivo principal su valorr era '__main__' caso contrario indicara otro valor
app = Flask(__name__)

#la clase CORS si solamente le pasamos la instancia de nuestra clase Flask entonces modificara las CORS para que puedar ser accedidos por todo el mundo (cualquier origen, cualquier metodo y cualquier cabecera)
CORS(app=app)

productos = []
#Endpoint
#decorador es un patron de software que modifica el comportamiento de un metodo de una clase
@app.route('/')
def rutaInicial():
    print('Ingreso al endpoint inicial')
    return 'Bienvenido a tu primera API de Codigo de Backend :D'

@app.route('/estado')
def estadoAPI():
    return{
        'hora': datetime.now().strftime('%Y-%m-%d %H:%M:%S') #string from time
    }

@app.route('/producto', methods=['POST'])
def gestionProductos():
    # get_json() > convierte el json que el cliente envia a un diccionario para que python lo pueda entender
    print(request.get_json())
    producto = request.get_json()
    productos.append(producto)
    return{
        'message': 'Producto creado exitosamente',
        'content': producto
    }
# levantamos nuestro servidor para que se quede a la espera de posibles peticiones durante un tiempo indeterminado
#reiniciar
app.run(debug=True)


