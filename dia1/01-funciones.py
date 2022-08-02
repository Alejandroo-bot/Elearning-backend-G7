from operator import truediv


def saludar():
    print("Buenas tardes")

saludar()

def saludarConNombre(nombre):
    print("Hola {}, como te va?".format(nombre))

saludarConNombre('Alejandro')

electrodomesticos = []
def registrarElectrodomesticos(nombre, precio, almacen='Las Malvinas'):
    electrodomesticos.append({'nombre': nombre, 'precio': precio, 'almacen': almacen})
    return True

registrarElectrodomesticos('Licuadora 12v', 115.00)
registrarElectrodomesticos('Freidora de aire', 100, 'Cercado')
registrarElectrodomesticos('Secador de cabello', 140)

print(electrodomesticos)

def contarElectrodomesticosPorAlmacen():
    

   malvinas = 0
   cercado = 0
   otro = 0

   for electrodomestico in electrodomesticos:
    if electrodomestico['almacen'] == 'Las Malvinas':
       malvinas += 1
    elif electrodomestico['almacen'] == 'Cercado':
       cercado += 1
    else:
        otro += 1

   print('En las Malvinas hay {}, en Cercado hay {} y en otros hay {} electrodomesticos'.format(malvinas, cercado, otro))
contarElectrodomesticosPorAlmacen()

def recibirAlumnos(clase, *alumnos):
    print(type(alumnos))
    print(alumnos)
    alumnos_lista = list(alumnos)
    print(type(alumnos_lista))
    alumnos_lista[0] = 'Rigoberto'
    print(clase)

recibirAlumnos('Eduardo','Juan', 'Jenny', 'Lily', 'Manuel')
