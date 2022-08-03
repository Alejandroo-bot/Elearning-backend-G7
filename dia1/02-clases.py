from mailbox import NoSuchMailboxError


class Persona:
    estatura = 100
    colorOjos = 'Cafe'
    colorCabello = 'Negro'
    fechaNacimiento = '2000-01-01'

    def saludar(self):
        print('Hola buenos dias')


personaEduardo = Persona()
print(personaEduardo.colorCabello)

personaMaria = Persona()
personaMaria.colorOjos = 'Verde'
print(personaMaria.colorOjos)
print(personaEduardo.colorCabello)

personaEduardo.saludar()
personaMaria.saludar()

#constructor
class Mascota:
    def __init__(self, nombre, especie, raza, sexo):
       self.nombre = nombre
       self.especie = especie
       self.raza = raza
       self.sexo = sexo 
    
    def info(self):
       print(self.nombre)
       print(self.especie)
       print(self.raza)
       print(self.sexo)

mascotaPerro = Mascota('Morocha', 'Perro', 'Salchicha', 'Femenino')
mascotaGato = Mascota('Michifus', 'Gato','Siames', 'Masculino')

#print(mascotaPerro.nombre)
#print(mascotaGato.nombre)
mascotaPerro.info()

