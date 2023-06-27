class Empresa():
    def __init__(self,rut,nombre_completo,sexo,cargo):
        self.rut = rut
        self.nombre_completo = nombre_completo
        self.sexo = sexo
        self.cargo = cargo
    
    def returnArray(self):
        return [self.rut,self.nombre_completo,self.sexo,self.cargo]

class Musica():
    trabajador= []
    def listarTrabajador(self):
        print("\nTrabajador: \n")
        for con in self.trabajador:
            datos = "Rut {0}| Nombre Completo: {1}| Sexo {2} | Cargo {3}"
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
        rut= input("Ingrese el rut: ")
        NumeroCorrecto = False
        while(not NumeroCorrecto):
            nombre_completo = input("Ingrese nombre completo : ")
            sexo = input("Ingrese sexo: ")
            cargo = input("Ingrese cargo: ")
            NumeroCorrecto = True
        trabajador = Empresa(rut,nombre_completo,sexo,cargo)
        return trabajador

    def agregarTrabajador(self):  #Agrega Cds
        rut=0
        for con in self.trabajador: #revisa arreglo creado más arriba
            if con.rut > rut:
                rut = con.rut
        trabajador=Musica.pedirDatosCD(rut+1) #esto asegura que el id es mayor al último registrado  #
        self.addCd(trabajador) #agrega al cd a la lista en el obj
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
