class Vehiculo:
    color='rojo'
    ruedas=4
    puertas=4
 
class Coche(Vehiculo):
    velocidad=150
    cilindrada=20
  

a = Coche()
print("Color del auto",a.color)
print("Cantidad de ruedas es ",a.ruedas)
print("Cantidad de puertas es ",a.puertas)
print("La velocidad es ",a.velocidad)
print("Cilindrada es",a.cilindrada)

