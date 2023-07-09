import mysql.connector
from mysql.connector import Error

#Data Access Object, realiza consultas.
class DAO():

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306, #puerto cambiado vs windows.
                user='root',
                password='',
                db='correo_yuri' #nombre bd con Mayus
            )
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))

    def listarTrabajador(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute('SELECT `rut`, `nombre_completo`, `sexo`, `cargo` FROM `trabajador`;')  #Nombre tabla con Mayus.
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
    
    def registrarTrabajador(self, trabajador):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO trabajador (rut, nombre_completo, sexo, cargo, direccion, telefono, fecha_ingreso, id_area, id_departamento) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}','{7}','{8}')"
                cursor.execute(sql.format(trabajador[0], trabajador[1], trabajador[2], trabajador[3], trabajador[4], trabajador[5], trabajador[6], trabajador[7], trabajador[8]))
                self.conexion.commit()
                print("¡Trabajador registrado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))


    def registrarCarga(self, carga):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO `carga_familiar`(`rut_carga`, `nombre_completo`, `parentesco`, `rut_trabajador`) VALUES ('{0}','{1}','{2}','{3}')"
                cursor.execute(sql.format(carga[0], carga[1], carga[2], carga[3]))
                self.conexion.commit()
                print("Carga registrada!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def registrarContacto(self, contacto):
                if self.conexion.is_connected():
                    try:
                        cursor = self.conexion.cursor()
                        sql = "INSERT INTO contacto_emergencia (rut_contacto, nombre_completo,relacion,telefono,rut) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')"
                        cursor.execute(sql.format(contacto[0],contacto[1],contacto[2],contacto[3],contacto[4]))
                        self.conexion.commit()
                        print("Contacto de emergencia registrado!\n")
                    except Error as ex:
                        print("Error al intentar la conexión: {0}".format(ex))

    
    def eliminarTrabajador(self, rut):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM trabajador WHERE rut = '{0}'"
                cursor.execute(sql.format(rut))
                self.conexion.commit()
                print("¡Contacto eliminado!\n")
            except Error as error: #ejemplo de uso de rollback
                print("Fallo al intentar eliminar dato rollback: {}".format(error))
                # revirtiendo los cambios
                self.conexion.rollback()
            finally:
                # closing database connection.
                if self.conexion.is_connected():
                    cursor.close()
                    #conn.close()
                    #print("connection is closed")
            """except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))"""
    
    def listarArea(self):
            if self.conexion.is_connected():
                try:
                    cursor = self.conexion.cursor()
                    cursor.execute('SELECT * FROM area;')  #Nombre tabla con Mayus.
                    resultados = cursor.fetchall()
                    return resultados
                except Error as ex:
                    print("Error al intentar la conexión: {0}".format(ex))

    def listarDepartamento(self):
            if self.conexion.is_connected():
                try:
                    cursor = self.conexion.cursor()
                    cursor.execute('SELECT * FROM departamento;')  #Nombre tabla con Mayus.
                    resultados = cursor.fetchall()
                    return resultados
                except Error as ex:
                    print("Error al intentar la conexión: {0}".format(ex))

    def filtrarTrabajador(self, sexo):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                query = "SELECT t.rut, t.nombre_completo, t.sexo, t.cargo, t.direccion, t.telefono, t.fecha_ingreso, a.nombre AS area, d.nombre AS departamento, t.id_usuario FROM trabajador t JOIN area a ON t.id_area = a.id_area JOIN departamento d ON t.id_departamento = d.id_departamento WHERE t.sexo = %s;"
                cursor.execute(query, (sexo,))
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def listarsexo(self, sexo):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = 'SELECT * FROM trabajador WHERE sexo = %s'
                cursor.execute(sql, (sexo,))
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
    def listarCargo(self,cargo):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = 'SELECT * FROM trabajador WHERE cargo = %s'
                cursor.execute(sql, (cargo,))
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
    def listararea(self,area):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = 'SELECT trabajador.rut, trabajador.nombre_completo, trabajador.sexo, trabajador.cargo, area.nombre FROM trabajador INNER JOIN area ON trabajador.id_area = area.id_area WHERE nombre= %s'
                cursor.execute(sql, (area,))
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
    def listardepartamento(self,departamento):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = 'SELECT trabajador.rut, trabajador.nombre_completo, trabajador.sexo, trabajador.cargo, departamento.nombre FROM trabajador INNER JOIN departamento ON trabajador.id_departamento = departamento.id_departamento WHERE nombre= %s'
                cursor.execute(sql, (departamento,))
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))                
               
        
    def actualizarCarga(self, carga):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE `carga_familiar` SET `nombre_completo` = '{0}', `parentesco` = '{1}', `rut` = '{2}' WHERE `rut_carga` = '{3}'"
                cursor.execute(sql.format(carga.nombre_completo, carga.parentesco, carga.rut, carga.rut_carga))
                self.conexion.commit()
                print("Carga actualizada!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def listarCarga(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "SELECT * FROM carga_familiar;"
                cursor.execute(sql)
                results = cursor.fetchall()
                return results
            except Error as ex:
                    print("Error al intentar la conexión: {0}".format(ex))



    def listarDatosPersonales(self,rut):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = 'SELECT `rut`, `nombre_completo`, `sexo`, `cargo`, `direccion`, `telefono` FROM `trabajador` WHERE `rut` = %s;'
                cursor.execute(sql,(rut,))
                results = cursor.fetchall()
                return results
            except Error as ex:
                    print("Error al intentar la conexión: {0}".format(ex))

    def actualizarDatosPersonales(self, rut, nueva_direccion, nuevo_telefono):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                query = "UPDATE `trabajador` SET `direccion` = %s, `telefono` = %s WHERE `rut` = %s;"
                cursor.execute(query, (nueva_direccion, nuevo_telefono, rut))
                self.conexion.commit()
                cursor.close()
                print("Datos actualizados en la base de datos.")
            except mysql.connector.Error as error:
                print("Error al actualizar los datos en la base de datos: ", error)
        else:
         print("No se pudo establecer una conexión a la base de datos.")            

    def listarCargas(self,rut):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = 'SELECT `rut_carga`, `nombre_completo`, `parentesco` FROM `carga_familiar` WHERE `rut_trabajador` = %s;'
                cursor.execute(sql,(rut,))
                results = cursor.fetchall()
                return results
            except Error as ex:
                    print("Error al intentar la conexión: {0}".format(ex))
                    
    def actualizaCargas(self, nombre, parentesco, carga_actualizar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                query = "UPDATE carga_familiar SET `nombre_completo` = %s, `parentesco` = %s WHERE `rut_carga` = %s;"
                cursor.execute(query, (nombre, parentesco, carga_actualizar))
                self.conexion.commit()
                cursor.close()
                print("Datos actualizados")
            except mysql.connector.Error as error:
                print("Error al actualizar los datos en la base de datos: ", error)
        else:
         print("No se pudo establecer una conexión a la base de datos.")            

    def listarContactoEmergencia(self,rut):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = 'SELECT `rut_contacto`, `nombre_completo`, `relacion`, `telefono` FROM `contacto_emergencia` WHERE `rut` = %s;'
                cursor.execute(sql,(rut,))
                results = cursor.fetchall()
                return results
            except Error as ex:
                    print("Error al intentar la conexión: {0}".format(ex))
                    
    def actualizaContactoEmergencia(self, nombre, relacion,telefono,contacto_actualizar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                query = "UPDATE contacto_emergencia SET `nombre_completo` = %s, `relacion` = %s,`telefono` = %s WHERE `rut_contacto` = %s;"
                cursor.execute(query, (nombre, relacion,telefono, contacto_actualizar))
                self.conexion.commit()
                cursor.close()
                print("Datos actualizados")
            except mysql.connector.Error as error:
                print("Error al actualizar los datos en la base de datos: ", error)
        else:
         print("No se pudo establecer una conexión a la base de datos.")            


    def eliminarCarga(self,rut_carga):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                query = 'DELETE FROM `carga_familiar` WHERE rut_carga = %s;'
                cursor.execute(query, (rut_carga,))
                self.conexion.commit()
                cursor.close()
                print("Carga eliminada con exito")
            except mysql.connector.Error as error:
                print("Error al actualizar los datos en la base de datos: ", error)
        else:
         print("No se pudo establecer una conexión a la base de datos.")           

    def eliminarContacto(self,rut_contacto):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                query = 'DELETE FROM `contacto_emergencia` WHERE rut_contacto = %s;'
                cursor.execute(query, (rut_contacto,))
                self.conexion.commit()
                cursor.close()
                print("Carga eliminada con exito")
            except mysql.connector.Error as error:
                print("Error al actualizar los datos en la base de datos: ", error)
        else:
         print("No se pudo establecer una conexión a la base de datos.")      
    
    def Login(self, id_usuario, password):
            if self.conexion.is_connected():
                try:
                    cursor = self.conexion.cursor()
                    sql = "SELECT id_usuario, tipo_usuario FROM usuario WHERE id_usuario= %s AND password = %s"
                    cursor.execute(sql, (id_usuario, password))
                    resultados = cursor.fetchall()
                    return resultados
                except Error as ex:
                    print("Error al intentar la conexión: {0}".format(ex))