# Cuenta de Banco

# Crear usuario
class CuentaBanco():
    def __init__(self,nombre,contraseña,dinero):
            self.nombre = nombre
            self.contraseña = contraseña
            self.dinero = dinero
    
    def ingresar(self):
        self.dinero = money
        print(f"{self.dinero} euros ingresados correctamente")

    def retirar(self):
         self.dinero = money - retiar_dinero
         print(f"{self.dinero} euros retirados")    




# Pedir datos para crear usuarios 
NombreCompleto  =  input("Ingresa tu nombre: ")
ContraseñaBanco =  input("Ingresa la contraseña que quieres crear: ")
money = ""

# Menu y funcionamiento de Imagen Teens
cuenta = CuentaBanco(NombreCompleto,ContraseñaBanco,money)
print(f"Imagen Teens ")

contra = input("Ingresa su contraseña: ")
if contra == cuenta.contraseña:
     print(f"\nHola de nuevo {cuenta.nombre}")
else:
    print("Contraseña incorrecta")    

if contra == cuenta.contraseña:
     ingresar = input("Quieres ingresar dinero s/n: ")
     if ingresar == "s":
       money = float(input("Cuanto dinero quieres ingresar"))
       cuenta.ingresar()

if contra == cuenta.contraseña:
  retiar_dinero = input("Quieres retirar dinero? s/n: ")
  if retiar_dinero == "s":
    retiar_dinero = float(input("Cuanto dinero quieres retirar?"))
    cuenta.retirar()