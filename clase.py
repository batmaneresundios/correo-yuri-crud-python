from BD.conexion import DAO

class Empresa():
    def __init__(self,rut,nombre_completo,sexo,cargo):
        self.rut = rut
        self.nombre_completo = nombre_completo
        self.sexo = sexo
        self.cargo = cargo
            
    def returnArray(self):
        return [self.rut,self.nombre_completo,self.sexo,self.cargo]

class Trabajador(Empresa):
    def __init__(self, rut, nombre_completo, sexo, cargo, direccion, telefono, fecha_ingreso,area,departamento):
        super().__init__(rut, nombre_completo, sexo, cargo)
        self.direccion = direccion
        self.telefono = telefono
        self.fecha_ingreso = fecha_ingreso
        self.area = area
        self.departamento = departamento

    def returnArray2(self):
        return super().returnArray() + [self.direccion, self.telefono, self.fecha_ingreso,self.area,self.departamento]

class Carga():
    def __init__(self,rut_carga,nombre_completo,parentesco,rut):
        self.rut_carga = rut_carga
        self.nombre_completo = nombre_completo
        self.parentesco = parentesco
        self.rut = rut

    def returnCarga(self):
        return [self.rut_carga,self.nombre_completo,self.parentesco,self.rut]

class Familiar():
    carga_familiar = []
    #carga = []

    def listarCarga(self):
        print("\Carga: \n")
        for con in self.carga_familiar:
            datos = "Rut carga: {0}| Nombre Completo: {1}| Sexo: {2} | Rut trabajador: {3}"
            print(datos.format(con.rut_carga, con.nombre_completo, con.parentesco, con.rut))
            print(" ")      

    @staticmethod
    def pedirDatosCarga():
        print("=== Datos carga familiar del trabajador ===")
        rut_carga= input("Ingrese el rut carga familiar: ")
        numeroCorrecto = False
        while(not numeroCorrecto):
            nombre_completo = input("Ingrese nombre completo : ")
            parentesco = input("Ingrese parentesco: ")
            rut = input("Ingrese rut del trabajador: ")            
            numeroCorrecto = True
        carga = Carga(rut_carga,nombre_completo,parentesco,rut) 
        Familiar.carga_familiar.append(carga)   
        return carga   
    

    @staticmethod
    def agregarCarga(carga):
        carga = Familiar.pedirDatosCarga()
        Familiar.carga_familiar.append(carga)
        
    def actualizarCarga(self):
        rut = input("Ingrese su rut: ")        
        datos = dao.listarCargas(rut)
        if len(datos) > 0:
            for trabajador in datos:
                print("Rut carga: {0}| Nombre Completo: {1}| Parentesco: {2}".format(
                    trabajador[0], trabajador[1], trabajador[2]))
        carga_actualizar = input("Ingrese RUT Carga familiar a actualizar: ")

        nombre = input("Ingrese nuevo nombre: ")
        parentesco = input("Ingrese nuevo parentesco: ")
        dao.actualizaCargas(nombre, parentesco,carga_actualizar)
 
        
    def addCarga(self,carga_familiar):
        self.carga_familiar.append(carga_familiar)



    def eliminarCarga(self):
        rut = input("Ingrese su rut: ")        
        datos = dao.listarCargas(rut)
        if len(datos) > 0:
            for trabajador in datos:
                print("Rut carga: {0}| Nombre Completo: {1}| Parentesco: {2}".format(
                    trabajador[0], trabajador[1], trabajador[2]))
        carga_eliminar = input("Ingrese RUT Carga familiar a eliminar: ")
        dao.eliminarCarga(carga_eliminar)        

    
    
class Contacto():
    def __init__(self,rut_contacto,nombre_completo,relacion,telefono,id_rut):
        self.rut_contacto = rut_contacto
        self.nombre_completo = nombre_completo
        self.relacion = relacion
        self.telefono = telefono
        self.id_rut = id_rut

    def arrayContacto(self):
        return [self.rut_contacto,self.nombre_completo,self.relacion,self.telefono,self.id_rut]

class Emergencia():
    contacto =[]

    def pedirDatosContacto(self):
        print("=== Datos contacto de Emergencia del trabajador ===")        
        rut_contacto = input("Ingrese el rut: ")
        NumeroCorrecto = False
        while(not NumeroCorrecto):
            nombre_completo = input("Ingrese nombre completo : ")
            relacion = input("Ingrese relacion: ")
            telefono = input("Ingrese telefono: ")
            id_rut = input("Ingrese el rut del trabajador: ")
            NumeroCorrecto = True
        contacto = Contacto(rut_contacto,nombre_completo,relacion,telefono,id_rut)
        return contacto
    
    def agregarContacto(self):  
        rut_contacto=0
        for con in self.contacto: 
            if con.rut_contacto > rut_contacto:
                rut_contacto = con.rut_contacto
        contacto = Emergencia.pedirDatosContacto(rut_contacto+1) 
        return contacto
    
    def actualizarContactoEmergencia(self):
        rut = input("Ingrese su rut: ")        
        datos = dao.listarContactoEmergencia(rut)
        if len(datos) > 0:
            for trabajador in datos:
                print("Rut contacto de emergencia: {0}| Nombre Completo: {1}| Relacion: {2}| Telefono: {3}".format(
                    trabajador[0], trabajador[1], trabajador[2], trabajador[3]))
        contacto_actualizar = input("Ingrese RUT Contacto Emergencia a actualizar: ")

        nombre = input("Ingrese nuevo nombre: ")
        relacion = input("Ingrese nueva relacion: ")
        telefono = input("Ingrese nuevo telefono: ")
        dao.actualizaContactoEmergencia(nombre, relacion,telefono,contacto_actualizar)

    def eliminarContacto(self):
        rut = input("Ingrese su rut: ")
        datos = dao.listarContactoEmergencia(rut)
        if len(datos) > 0:
            for trabajador in datos:
                print("Rut contacto de emergencia: {0}| Nombre Completo: {1}| Relacion: {2}| Telefono: {3}".format(
                    trabajador[0], trabajador[1], trabajador[2], trabajador[3]))
            
            contacto_eliminar = input("Ingrese RUT Contacto Emergencia a eliminar: ")
            contacto_encontrado = False
            
            for trabajador in datos:
                if trabajador[0] == contacto_eliminar:
                    contacto_encontrado = True
                    break
            
            if contacto_encontrado:
                dao.eliminarContacto(contacto_eliminar)
                print("Contacto de emergencia eliminado con éxito.")
            else:
                print("El RUT de contacto de emergencia ingresado no existe en la base de datos.")
        else:
            print("No se encontraron contactos de emergencia para el rut proporcionado.")
        


class Empleados():
    trabajador= []
    def listarTrabajador(self):
        print("\nTrabajadores: \n")
        for con in self.trabajador:
            datos = "Rut: {0}| Nombre Completo: {1}| Sexo: {2} | Cargo: {3}"
            print(datos.format(con.rut, con.nombre_completo, con.sexo, con.cargo))
            print(" ")  


    def actualizarDatosPersonales(self):
        rut = input("Ingrese su rut: ")        
        datos = dao.listarDatosPersonales(rut)
        if len(datos) > 0:
            for trabajador in datos:
                print("Rut: {0}| Nombre Completo: {1}| Sexo: {2} | Cargo: {3} | Direccion: {4} | Telefono: {5}".format(
                    trabajador[0], trabajador[1], trabajador[2], trabajador[3],trabajador[4],trabajador[5]))
                
        direccion = input("Ingrese nueva direccion: ")
        telefono = input("Ingrese nuevo telefono: ")
        dao.actualizarDatosPersonales(rut, direccion, telefono)


    def addTrabajador(self,trabajador):
        self.trabajador.append(trabajador)
        
    @staticmethod
    def pedirDatosTrabajador(rut):
        print("=== Datos personales del trabajador ===")
        rut= input("Ingrese rut del trabajador: ")
        NumeroCorrecto = False
        while(not NumeroCorrecto):
            nombre_completo = input("Ingrese nombre completo : ")
            sexo = input("Ingrese sexo: ")
            direccion = input("Ingrese dirección: ")
            telefono = input("Ingrese telefono: ")
            NumeroCorrecto = True
            print("=== Datos laborales del trabajador ===")
            cargo = input("Ingrese cargo del trabajador: ")
            fecha_ingreso = input("Ingrese fecha de ingreso del trabajador: ")
            print("Ingrese ID área del trabajador según las siguientes áreas: ")
            area = dao.listarArea()
            for i in range(len(area)):
                print(area[i])
                continue
            area = input("Ingrese ID del área: ")
            print("Ingrese ID departamento del trabajador según los siguientes departamentos: ")
            departamento = dao.listarDepartamento()
            for i in range(len(departamento)):
                print(departamento[i])
                continue
            departamento = input("Ingrese ID del departamento: ")                     
            NumeroCorrecto = True
        trabajador = Trabajador(rut,nombre_completo,sexo,cargo,direccion,telefono,fecha_ingreso,area,departamento)
        return trabajador

    def agregarTrabajador(self):  
        rut=0
        for con in self.trabajador:
            if con.rut > rut:
                rut = con.rut
        trabajador=Empleados.pedirDatosTrabajador(rut+1) 
        return trabajador
    
    
class Filtrado():
    def listar_por_sexo(self):
        sexo = input("Ingrese el sexo para filtrar (Masculino/Femenino): ")
        trabajadores = dao.listarsexo(sexo)
        if len(trabajadores) > 0:
            for trabajador in trabajadores:
                print("Rut: {0} | Nombre: {1} | Sexo: {2} | Cargo: {3}".format(
                    trabajador[0], trabajador[1], trabajador[2], trabajador[3]))
        else:
            print("No se encontraron trabajadores con el sexo especificado.")

    def listar_por_cargo(self):
        cargo = input("Ingrese el cargo para filtrar: ")
        trabajadores = dao.listarCargo(cargo)
        if len(trabajadores) > 0:
            for trabajador in trabajadores:
                print("Rut: {0} | Nombre: {1} | Sexo: {2} | Cargo: {3}".format(
                    trabajador[0], trabajador[1], trabajador[2], trabajador[3]))
        else:
            print("No se encontraron trabajadores con el cargo especificado.")

    def listar_por_area(self):  
        
        area = input("Ingrese el area para filtrar: ")
        trabajadores = dao.listararea(area)
        if len(trabajadores) > 0:
            for trabajador in trabajadores:
                print("Rut: {0} | Nombre: {1} | Sexo: {2} | Cargo: {3} | Nombre Area: {4}".format(
                    trabajador[0], trabajador[1], trabajador[2], trabajador[3],trabajador[4]))
        else:
            print("No se encontraron trabajadores con el cargo especificado.")

    def listar_por_departamento(self):
        departamento = input("Ingrese el departamento para filtrar según lo siguiente: ")
        trabajadores = dao.listardepartamento(departamento)
        if len(trabajadores) > 0:
            for trabajador in trabajadores:
                print("Rut: {0} | Nombre: {1} | Sexo: {2} | Cargo: {3} | Nombre departamento: {4}".format(
                    trabajador[0], trabajador[1], trabajador[2], trabajador[3],trabajador[4]))
        else:
            print("No se encontraron trabajadores con el cargo especificado.")



dao = DAO()

