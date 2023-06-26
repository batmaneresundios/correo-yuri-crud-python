from BD.conexion import DAO
from clase import CD, Musica


def actualizarTrabajador():
    arrayCd = dao.listarTrabajador()
    musica.trabajador = []
    for con in musica.trabajador:
        musica.addCd(CD(con[0], con[1], con[2], con[3], con[4], con[5], con[6]))

def menuPrincipal():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("==================== MENÚ PRINCIPAL ====================")
            print("1.- Listar Trabajadores")
            print("2.- Registrar contacto")
            print("3.- Actualizar contacto")
            print("4.- Eliminar contacto")
            print("5.- Salir")
            print("========================================================")
            opcion = int(input("Seleccione una opción: "))

            if opcion < 1 or opcion > 5:
                print("Opción incorrecta, ingrese nuevamente...")
            elif opcion == 5:
                continuar = False
                print("¡Gracias por usar la aplicación de agenda!!!")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)


def ejecutarOpcion(opcion):
    
    if opcion == 1:
        try:
            #actualizarAgenda()
            if len(musica.trabajador) > 0:
                musica.listarTrabajador()
            else:
                print("No se encontraron contactos...")
        except:
            print("Ocurrió un error...")
    elif opcion == 2:
        contacto = musica.agregarContacto()
        try:
            dao.registrarContacto(musica.returnArray())
        except:
            print("Ocurrió un error...")
    elif opcion == 3:
        try:
            #actualizarAgenda()
            if len(musica.contactos) > 0:
                contacto = musica.actualizarContacto()
                if contacto:
                    dao.actualizarContacto(contacto.returnArray())
                else:
                    print("Id de contacto a actualizar no encontrado...\n")
            else:
                print("No se encontraron contactos...")
        except:
            print("Ocurrió un error...")
    elif opcion == 4:
        try:
            #actualizarAgenda()
            if len(musica.contactos) > 0:
                idEliminar = musica.eliminarContacto()
                if not(idEliminar == 0):
                    dao.eliminarContacto(idEliminar)
                else:
                    print("Id de contacto no encontrada...\n")
            else:
                print("No se encontraron contactos...")
        except:
            print("Ocurrió un error...")
    else:
        print("Opción no válida...")

musica = Musica()
dao = DAO()
actualizarTrabajador() #ponemos los datos de la BD en el objeto agenda

menuPrincipal()