from flask import Flask

# __name__ > variable propia de python que muestra si el archivo que estamos utilizando es el archivo principal del proyecto, si es el archivo principal su valorr era '__main__' caso contrario indicara otro valor
app = Flask(__name__)

#Endpoint
#decorador es un patron de software que modifica el comportamiento de un metodo de una clase
@app.route('/')
def rutaInicial():
    print('Ingreso al endpoint inicial')
    return 'Bienvenido a tu primera API de Codigo de Backend :D'
# levantamos nuestro servidor para que se quede a la espera de posibles peticiones durante un tiempo indeterminado
#reiniciar
app.run(debug=True)