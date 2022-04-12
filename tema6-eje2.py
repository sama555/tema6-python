
class Alumnos:

    nombre = ' '
    nota = 0.0

    def __init__(self, nombre, nota):
        self.nombre=nombre
        self.nota=nota

    def mostrar(self):
        return self.nombre, self.nota

    def resultado(self):
        if self.nota>=6:
            return self.nota , 'Aprobado'
        else:
            return self.nota, 'Desaprobado'

a = Alumnos('Maria', 6)
print(a.mostrar())
print(a.resultado())

a = Alumnos('juan', 3)
print(a.mostrar())
print(a.resultado())



