class usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def info(self):
        return {
            'nombre':self.nombre,
            'apellido':self.apellido
        }

class Alumno(usuario):
    def __init__(self, nombre, apellido, anio, seccion):
        self.anio = anio
        self.seccion = seccion
        #es un metodo que sirve para utilizar los metodos y atributos de la clase a clases que estamos heredando
        super().__init__(nombre, apellido)

    def info(self):
        infousuario = super().info()
        data = {
            'anio': self.anio,
            'seccion': self.seccion,
        }
        return {**data, **infousuario }

alumnoEduardo = Alumno('Eduardo', 'de Rivero', 'Sexto', 'A')

usuarioRaul = usuario('Raul', 'Mendoza')

informacion = alumnoEduardo.info()
print(informacion)

print(usuarioRaul.info())

