# Coche 

class Coche:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.arrancado = False

    def arrancar(self):
        self.arrancado = True
        print(f"El {self.marca} {self.modelo} esta arrancado")
    
    def parado(self):
        self.arrancado = False
        print(f"El {self.marca} {self.modelo} no esta arrancado")


marca = input("Di la marca de coche que quieres ingresar:")
modelo = input("Di el modelo de coche que quieres ingresar:")

coche = Coche(marca,modelo)        
print(f"Marca del coche: {coche.marca} \nModelo del coche: {coche.modelo}" )  


coche.arrancar()
coche.parado()