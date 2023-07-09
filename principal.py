from BD.conexion import DAO
from clase import Empresa, Empleados,Familiar,Emergencia, Filtrado, Carga

def actualizarcarga():
    arrayCarga = dao.listarCarga()
    for con in arrayCarga:
        familiar.addCarga(Carga(con[0], con[1], con[2], con[3]))
   
def actualizarTrabajador():
    arrayTrabajador = dao.listarTrabajador()
    for con in arrayTrabajador:
        empleados.addTrabajador(Empresa(con[0], con[1], con[2], con[3]))

def login():
    continuar = True
    while continuar:
        print("=== Inicio de Sesión ===")
        id_usuario = input("Ingrese su ID de usuario (RUT): ")
        contraseña = input("Ingrese su contraseña: ")

        resultados = dao.Login(id_usuario, contraseña)
        if resultados:
            tipo_usuario = resultados[0][1]
            if tipo_usuario == "jefe":
                menuPrincipal()
            elif tipo_usuario == "trabajador":
                menuTrabajador()
            elif tipo_usuario == "trabajadorecursos":
                menuTrabajadorRRHH()                
            continuar = False
        else:
            print("ID de usuario o contraseña incorrectos. Intente nuevamente.")        

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
            print("7.- Salir")                       
            print("========================================================")
            opcion = int(input("Seleccione una opción: "))

            if opcion < 1 or opcion > 8:
                print("Opción incorrecta, ingrese nuevamente...")
            elif opcion == 7:
                continuar = False
                print("¡¡¡Gracias por usar la aplicación Correo de Yuri!!!")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)

def ejecutarOpcion(opcion):    
    if opcion == 1:
        try:
            if len(empleados.trabajador) > 0:
                empleados.listarTrabajador()
            else:
                print("No se encontraron trabajadores...")
        except:
            print("Ocurrió un error...")
    elif opcion == 2:
        contacto = empleados.agregarTrabajador()
        contacto_a = emergencia.agregarContacto()        
        carga = familiar.pedirDatosCarga()
        try:
            dao.registrarTrabajador(contacto.returnArray2())
            dao.registrarContacto(contacto_a.arrayContacto())
            dao.registrarCarga(carga.returnCarga())
        except:
            print("Ocurrió un error...")
    elif opcion == 3:
        try:
            filtro.listar_por_sexo()
        except:
            print("Ocurrió un error...")

    elif opcion == 4:
        try:
            filtro.listar_por_cargo()
        except:
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

def menuTrabajadorRRHH():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("==================== MENÚ TRABAJADOR RR.HH ====================")
            print("1.- Listar Trabajadores")
            print("2.- Registrar Trabajador")
            print("3.- Salir")                       
            print("========================================================")
            opcion = int(input("Seleccione una opción: "))

            if opcion < 1 or opcion > 4:
                print("Opción incorrecta, ingrese nuevamente...")
            elif opcion == 3:
                continuar = False
                print("¡¡¡Gracias por usar la aplicación Correo de Yuri!!!")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcionTrabajadorRRHH(opcion)

def ejecutarOpcionTrabajadorRRHH(opcion):    
    if opcion == 1:
        try:
            if len(empleados.trabajador) > 0:
                empleados.listarTrabajador()
            else:
                print("No se encontraron trabajadores...")
        except:
            print("Ocurrió un error...")
    elif opcion == 2:
        contacto = empleados.agregarTrabajador()
        contacto_a = emergencia.agregarContacto()        
        carga = familiar.pedirDatosCarga()
        try:
            dao.registrarTrabajador(contacto.returnArray2())
            dao.registrarContacto(contacto_a.arrayContacto())
            dao.registrarCarga(carga.returnCarga())
        except:
            print("Ocurrió un error...")

def menuTrabajador():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("==================== MENÚ TRABAJADOR ====================")
            print("1.- Modificar datos personales")
            print("2.- Modificar cargas familiares")
            print("3.- Modificar contacto de emergencia")
            print("4.- Agregar carga familiar")
            print("5.- Agregar contacto de emergencia")
            print("6.- Eliminar carga familiar")
            print("7.- Eliminar contacto de emergencia")
            print("8.- Salir de la aplicación")
            
            opcion = int(input("Seleccione una opción: "))

            if opcion < 1 or opcion > 9:
                print("Opción incorrecta, ingrese nuevamente...")
            elif opcion == 8:
                continuar = False
                print("¡¡¡Gracias por usar la aplicación Correo de Yuri!!!")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcionTrabajador(opcion)

def ejecutarOpcionTrabajador(opcion):    
    if opcion == 1:
        try:          
            empleados.actualizarDatosPersonales() 
            
        except:
            print("Ocurrió un error...")
    elif opcion == 2:
        try:
            familiar.actualizarCarga()

        except:
            print("Ocurrió un error...")
    elif opcion == 3:
        try:
            emergencia.actualizarContactoEmergencia()
        except:
            print("Ocurrió un error...")            
    elif opcion == 4:
        try:
            carga = familiar.pedirDatosCarga()
            dao.registrarCarga(carga.returnCarga())
        except:
            print("Ocurrió un error...")            
    elif opcion == 5:
        try:
            contacto_a = emergencia.agregarContacto()        
            dao.registrarContacto(contacto_a.arrayContacto())
        except:
            print("Ocurrió un error...")
    elif opcion == 6:
        try: 
            familiar.eliminarCarga()
        except:
            print("Ocurrió un error...")    
    elif opcion == 7:
        try: 
            emergencia.eliminarContacto()

        except:
            print("Ocurrió un error...")            



emergencia = Emergencia()
familiar = Familiar()
empleados = Empleados()
filtro = Filtrado()
dao = DAO()
actualizarTrabajador() #ponemos los datos de la BD en el objeto agenda
actualizarcarga()
#menuPrincipal()
#menuTrabajador()
login()