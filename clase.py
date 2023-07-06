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
            datos = "Rut: {0}| Nombre Completo: {1}| Sexo: {2} | Cargo: {3}"
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
       # return carga1
    


    @staticmethod
    def agregarCarga(carga):
        carga = Familiar.pedirDatosCarga()
        Familiar.carga_familiar.append(carga)
        

    @staticmethod
    def actualizarCarga(self):
        self.listarCarga()

            

        for carga in Familiar.carga_familiar:
            if carga.rut_carga == rut_carga:
                print("=== Actualizar carga familiar ===")
                nombre_completo = input("Ingrese nuevo nombre completo: ")
                parentesco = input("Ingrese nuevo parentesco: ")
                rut = input("Ingrese nuevo rut del trabajador: ")
                
                carga.nombre_completo = nombre_completo
                carga.parentesco = parentesco
                carga.rut = rut

                print("Carga familiar actualizada.")
                return True

        print("No se encontró la carga familiar con el rut especificado.")
        
        return False    
        
    def addCarga(self,carga_familiar):
        self.carga_familiar.append(carga_familiar)
    
    
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
    


class Musica():
    trabajador= []
    def listarTrabajador(self):
        print("\nTrabajadores: \n")
        for con in self.trabajador:
            datos = "Rut: {0}| Nombre Completo: {1}| Sexo: {2} | Cargo: {3}"
            print(datos.format(con.rut, con.nombre_completo, con.sexo, con.cargo))
            print(" ")  

    def rutExiste(self,rut):
        existerut = False
        c=0
        for con in self.trabajador:
            if con.rut == rut:
                existerut = True
                break
            c += 1
        if existerut:
            indice = c
        else:
            indice = -1
        return indice #retorna -1 si no está, sino, retorna indice en donde está esa id en el arreglo

    def addCd(self,trabajador):
        self.trabajador.append(trabajador)
        
    @staticmethod
    def pedirDatosCD(rut):
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

    def agregarTrabajador(self):  #Agrega Cds
        rut=0
        for con in self.trabajador: #revisa arreglo creado más arriba
            if con.rut > rut:
                rut = con.rut
        trabajador=Musica.pedirDatosCD(rut+1) #esto asegura que el id es mayor al último registrado  #
        return trabajador
    
    def actualizarCds(self):
        self.listarTrabajador()        
        NumeroCorrecto = False
        while(not NumeroCorrecto):
            idEditar = input("Ingrese el ID del contacto a editar: ")
            if idEditar.isnumeric():
                if (int(idEditar) > 0):
                    NumeroCorrecto = True
                    idEditar = int(idEditar)
                else:
                    print("El Id debe ser mayor a 0.")
            else:
                print("debe ingresar un número.")
        
        existeId=self.idExiste(idEditar)

        if existeId > -1:
            print("ingrese datos a modificar")
            trabajador=Musica.pedirDatosCD(idEditar)
            self.cd[existeId]=trabajador #modifica el contacto en el objeto
        else:
            trabajador = None

        return trabajador
    
    def eliminarCds(self):
        self.listarTrabajador()

        NumeroCorrecto = False
        while(not NumeroCorrecto):
            idEliminar = input("Ingrese el id del contacto a eliminar: ")
            if idEliminar.isnumeric():
                if (int(idEliminar) > 0):
                    NumeroCorrecto = True
                    idEliminar = int(idEliminar)
                else:
                    print("El Id debe ser mayor a 0.")
            else:
                print("debe ingresar un número.")
        existerut=self.rutExiste(idEliminar)

        if existerut == -1:
            idEliminar = 0
        else:
            del self.trabajador[existerut] #elimina el contacto de la lista en el obj
        
        return idEliminar
    
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

