from contacto import Contacto

# lista que se usa para almacenar los contactos
listaContactos = []



# edad promedio en los contactos
def edad_prom():
    listaContactos.sort(key=lambda x: x.edad)
    print("la edad promedio es de {} a {} años"
          .format(listaContactos[0].edad, listaContactos[-1].edad))

# contacto mas grande
def contacto_mayor():
    listaContactos.sort(key=lambda x: x.edad, reverse=True)
    print("El contacto mas grande es: {} ".format(listaContactos[0].nombre))

#contacto mas joven
def contacto_menor():
    listaContactos.sort(key=lambda x: x.edad)
    print("El contacto mas joven es: {} ".format(listaContactos[0].nombre))


# busqueda por nombre
def busqueda_nombre():
    print("Busqueda nombre")
    nombre_busqueda = str(input("Ingresa el nombre a buscar: "))
    for objContacto in listaContactos:
        if nombre_busqueda == objContacto.nombre:
            objContacto.muestraDetalles()


# busqueda por numero de teléfono
def busqueda_numero():
    print("Busqueda numero")
    numero_busqueda = input("Ingrea el numero a buscar: ")
    for objContacto in listaContactos:
        if numero_busqueda == objContacto.telefono:
            objContacto.muestraDetalles()


# Agregar nuevo contacto
def nuevo_contacto():
    print("Registrar nuevo contacto")
    nombre = input("ingresar nombre: ")
    telefono = input("ingresar telefono: ")
    fecha = input("ingresa edad: ")
    objContacto = Contacto(nombre, telefono, fecha)
    listaContactos.append(objContacto)


# Elimina contacto
def eliminar_contacto():
    print("Eliminar Contacto")
    nombre_o_numero = input("Ingresa Nombre o teléfono del contacto a eliminar: ")
    for objContacto in listaContactos:
        if nombre_o_numero == objContacto.telefono or nombre_o_numero == objContacto.nombre:
            listaContactos.remove(objContacto)
            print("contacto {} eliminado correctamente!".format(nombre_o_numero))


# muestra todos los contactos
def mostrar_agenda():
    print("mostrando agenda")
    for objContacto in listaContactos:
        objContacto.muestraDetalles()


# Actualizar contacto
def actualizacion_contacto():
    nombre_o_numero = input("Ingresa Nombre o teléfono del contacto a editar: ")
    for objContacto in listaContactos:
        if nombre_o_numero == objContacto.telefono or nombre_o_numero == objContacto.nombre:
            nuevo_nombre = input("Ingresa el nuevo nombre: ")
            nuevo_telefono = input("Ingresa el nuevo teléfono: ")
            nueva_edad = input("Ingresa la nueva edad: ")
            objContacto.actualizacion_contacto(nuevo_nombre, nuevo_telefono, nueva_edad)
            print("{} se actualizo correctamente".format(objContacto.nombre))
            objContacto.muestraDetalles()


# Menu incial
def main():
    while True:
        print("\n")
        print("|**************************|")
        print("|**|       Agenda       |**|")
        print("|**************************|")
        print("")
        print("Seleccione una opción:")
        print("1.- Edad promedio")
        print("2.- Contacto mayor")
        print("3.- Contacto menor")
        print("4.- Buscar contacto por nombre")
        print("5.- Buscar contacto por teléfono")
        print("6.- Nuevo contacto")
        print("7.- Eliminar contacto")
        print("8.- Mostrar agenda")
        print("9.- Actualizar contacto")
        print("0.- Salir\n")

        opcion = int(input("Opcion: "))

        if opcion == 1:
            edad_prom()
        elif opcion == 2:
            contacto_mayor()
        elif opcion == 3:
            contacto_menor()
        elif opcion == 4:
            busqueda_nombre()
        elif opcion == 5:
            busqueda_numero()
        elif opcion == 6:
            nuevo_contacto()
        elif opcion == 7:
            eliminar_contacto()
        elif opcion == 8:
            mostrar_agenda()
        elif opcion == 9:
            actualizacion_contacto()
        elif opcion == 0:
            print('Cerrando agenda')
            exit()


if __name__ == '__main__':
    main()
