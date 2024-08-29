usuarios=[]
saldos=[]

def mostrar_menu():
    print("\nBienvenido al sistema de caja del banco")
    print("1. Registrar usuario")
    print("2. Depósito")
    print("3. Retiro")
    print("4. Salir")
    
 
def registrar_usuario():
    usuario=input("ingrese nombre de usuario")
    
     
    if usuario in usuarios:
        print("Ya esta registrado")  
    else:
        usuarios.append(usuario) 
        print (f"Usuario {usuario} registrado con exito") 

def realizar_deposito():
    usuario=input("ingrese nombre de usuario")
    if usuario in usuarios:
        index=usuarios.index(usuario)
        monto=float(input("ingrese el valor a depositar"))
        saldos[index] +=monto 
        print(f"deposito de {monto}realizado con exito, nuevo saldo:{saldos[index]}")
    else:
        print("el usuario no existe")

def retiro():
    usuario=input("ingrese nombre de usuario")
    if usuario in usuarios:
        index=usuarios.index(usuario)
        monto=float(input("ingrese monto a retirar"))
        if monto<= saldos[index]:
            print(f"Retiro de{monto} realizado con exito. nuevo saldo:{saldos[index]}")
        else:
            print("fondos insuficientes")
    else:
        print("usuario no existe")
                    
def consultar_saldo():
    usuario=input("ingrese nombre de usuario")
    if usuario in usuarios:
        index=usuarios.index(usuario)
        print(f"el saldo actual de {usuario}es {saldos[index]}")
    else:
        print("usuario no existe") 

def main(): 
    while True:
        mostrar_menu()
        opcion=input ("selecione una opcon")
        if opcion=="1":
            registrar_usuario()
        elif opcion=="2":
            realizar_deposito()
        elif opcion== "3":
            retiro()
        elif opcion== "4":
            consultar_saldo
        elif opcion== "5":
            print("gracias por usar el sistema")
            break
        else:
            print ("opcion no valida , intente de nuevo")                
 
main()        
        
                                 
        
            

