#Tenemos la lista de contactos
contactos = []

def actualizar_contacto():
    print("==================================")
    print("|    Actualizar contacto         |")
    print("==================================")
    nombre = input("¿Cuál es el nombre del contacto? ")
    
    #se busca al contacto
    for i in contactos:
        if i["nombre"] == nombre:
            #se solicita el dato que queremos actualizar
            seleccion = input("¿Que quieres actualizar? (1.nombre\n2.telefono\n3.email) ")
            if seleccion == "1":
                i["nombre"] = input("¿Cuál es el nuevo nombre? ")
            elif seleccion == "2":
                i["telefono"] = input("¿Cuál es el nuevo teléfono? ")
            elif seleccion == "3":
                i["email"] = input("¿Cuál es el nuevo email? ")
            print("Contacto actualizado")
            break
    else:
        print("No se encontro el contacto")
    menu()

def eliminar_contacto():
    print("==================================")
    print("|    Eliminar contacto           |")
    print("==================================")
    
    #buscamos al contacto
    nombre = input("¿Cuál es tu nombre? ")
    for i in contactos:
        if i["nombre"] == nombre:
            
            #con remove eliminamos el contacto de la lista
            contactos.remove(i)
            print("Contacto eliminado")
            break
    else:
        print("No se encontro el contacto")
    menu()

def buscar_contacto():
    print("==================================")
    print("|    Buscar contacto             |")
    print("==================================")
    nombre = input("¿Cuál es tu nombre? ")
    for i in contactos:
        if i["nombre"] == nombre:
            print(i["nombre"] + " - " + i["telefono"] + " - " + i["email"])
            break
    else:
        print("No se encontro el contacto")
    menu()

def ver_contactos():
    print("==================================")
    print("|    Listado de contactos        |")
    print("==================================")
    #mostramos todos los contactos de la lista separados por un guion
    for i in contactos:
        print(i["nombre"] + " - " + i["telefono"] + " - " + i["email"])
    menu()
        
def agregar_contacto():
    # Pedimos los datos del usuario, Las validaciones no están incluidas
    nombre = input("¿Cuál es tu nombre? ")
    telefono = input("¿Cuál es tu número de teléfono? ")
    email = input("¿Cuál es tu correo electrónico? ")
    # guardamos los datos en un diccionario
    nuevo_contacto = {"nombre": nombre, "telefono": telefono, "email": email}
    contactos.append(nuevo_contacto)
    menu()
    
def menu():
    print("\n--------------------------------")
    print("Agenda de contactos")
    print("1. Agregar contacto")
    print("2. Ver contactos")
    print("3. Buscar Contacto")
    print("4. Eliminar Contacto")
    print("5. Actualizar Contacto")
    print("6. Salir")
    # pedimos la entrada del usuario
    seleccion = input("¿Cuál es tu elección? ")
    print("--------------------------------\n")
    
    if seleccion == "1":
        agregar_contacto()
        
    elif seleccion == "2":
        ver_contactos()
        
    elif seleccion == "3":
        buscar_contacto()
        
    elif seleccion == "4":
        eliminar_contacto()
        
    elif seleccion == "5":
        actualizar_contacto()
        
    elif seleccion == "6":
        print("Hasta pronto")
        return 0
            
    else:
        print("Opción inválida")   
        
#esta es la funcion principal
menu()