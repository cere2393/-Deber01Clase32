usuarios={}


def mostrar_menu():
    print("bienvenido al sistema de la caja de banco")
    print("1. Registrar Uuario")
    print("2. Deposito")
    print("3. Retiro")
    print("4. Salir")


def Registar_usuario():
    nombre=input("ingrese nombre de usuario")
    if nombre in usuarios:
        print ("El usuario ya esta registrado")
    else:
        usuarios(nombre)=0
        print(f"Usuario{nombre} registrado con exito")        


def despositar():
    
    nombre=input("ingrese nombre de usuario")
    if nombre in usuarios:
        monto=float(input("ingrese el valor a depositar"))
        usuarios(nombre)+= monto
        print(f"deposito de{monto} realizado con exito, nuevo saldo :{usuarios[nombre]}")
    else:
        print("el usuario no existe") 
        
def retiro():
    nombre=input("ingrese nombre de usuario")
    if nombre in usuarios:
        monto=float(input("ingrese valor a retirar"))
        if monto >=usuarios[nombre]:
            usuarios[nombre]-=monto
            print(f"retiro de{monto} realizado con exito.Nuevo saldo es de {usuarios[nombre]}")
        else:
            print("fondos insuficientes")
    else:
        print("usuario no existe")

def main():
    while True:
        mostrar_menu()
        opcion=input("selecione una opcion") 
        if opcion=="1":
            Registar_usuario()
        elif opcion=="2":
            despositar()
        elif opcion=="3":
            retiro()
        elif opcion=="4":
            print("gracias por usar el sistema")
        else:
            print ("opcion no valida , intente de nuevo")


if __name__ == "__main__":
    main()                                                             