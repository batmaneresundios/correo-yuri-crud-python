from BD.conexion import DAO
from clase import Empresa, Musica,Familiar,Emergencia, Filtrado, Carga


def actualizarcarga():
    arrayCd = dao.listarCarga()
    for con in arrayCd:
        familiar.addCarga(Carga(con[0], con[1], con[2], con[3]))

        

    

def actualizarTrabajador():
    arrayCd = dao.listarTrabajador()
    for con in arrayCd:
        musica.addCd(Empresa(con[0], con[1], con[2], con[3]))

def imprimirCargaFamiliar():
    print("=== Carga familiar ===")
    if len(Familiar.carga_familiar) > 0:
        for carga in Familiar.carga_familiar:
            print(carga.returnCarga())
    else:
        print("No hay cargas familiares registradas.")
def verificarCargaFamiliar():
    if len(Familiar.carga_familiar) > 0:
        print("Hay cargas familiares registradas.")
    else:
        print("No hay cargas familiares registradas.")

def menuPrincipal():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("==================== MENÚ JEFE ====================")
            print("1.- Listar Trabajadores")
            print("2.- Registrar Trabajador")
            print("3.- Listar según sexo")
            print("4.- Listar según cargo")
            print("5.- Listar área")
            print("6.- Listar departamento")
            print("7.- actualizar carga")                       
                                   
            print("8.- Salir")
            print("========================================================")
            opcion = int(input("Seleccione una opción: "))

            if opcion < 1 or opcion > 9:
                print("Opción incorrecta, ingrese nuevamente...")
            elif opcion == 9:
                continuar = False
                print("¡¡¡Gracias por usar la aplicación Correo de Yuri!!!")
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
                print("No se encontraron trabajadores...")
        except:
            print("Ocurrió un error...")
    elif opcion == 2:
        #contacto = musica.agregarTrabajador()
        #contacto_a = emergencia.agregarContacto()        
        #carga = Familiar.pedirDatosCarga()
        #carga1= Familiar.agregarCarga(carga)
        #try:
            #dao.registrarTrabajador(contacto.returnArray2())
            #dao.registrarContacto(contacto_a.arrayContacto())
            #dao.registrarCarga(carga1.returnCarga())
        #except:
            print("Ocurrió un error...")
    elif opcion == 3:
        try:
            filtro.listar_por_sexo()
        except:
            print("Ocurrió un error...")

    #elif opcion == 4:
        #try:
            filtro.listar_por_cargo()
        #except:
            print("Ocurrió un error...")
    elif opcion == 5:
        try:
            filtro.listar_por_area()
        except:
            print("Ocurrió un error...")
    elif opcion == 6:
        try:
            filtro.listar_por_departamento()
        except:
            print("Ocurrió un error...")
    elif opcion == 4:
            try:
                #actualizarCDs()
                if len(familiar.carga_familiar) > 0:
                    cd = familiar.actualizarCarga()
                    if cd:
                        dao.actualizarCarga(cd.returnCarga())
                    else:
                        print("Id del CDS no se encontro :(")
                else:
                    print("No se encontro CDs :(")
            except:
                print("Ocurrió un error :(")
    elif opcion == 8:
        #carga = familiar.pedirDatosCarga()
        #dao.registrarCarga(carga.returnCarga())
        try:
            if len(familiar.carga_familiar) > 0:
                familiar.listarCarga()
        except:
                print("hola")




    else:
        print("Opción no válida...")







emergencia = Emergencia()
familiar = Familiar()
musica = Musica()
filtro = Filtrado()
dao = DAO()
actualizarTrabajador() #ponemos los datos de la BD en el objeto agenda
actualizarcarga()

menuPrincipal()


