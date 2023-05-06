from validate_email import validate_email
import re

class Email: 
    __idCuenta: str
    __dominio: str
    __tipoDominio: str
    __contrasenia: str
    
    def __init__(self, idCuenta: str, dominio: str, tipoDominio: str, contrasenia: str):
        self.__idCuenta = idCuenta 
        self.__dominio = dominio 
        self.__tipoDominio = tipoDominio 
        self.__contrasenia = contrasenia 
    
    def set_idCuenta(self, idCuenta: str):
        self.__idCuenta = idCuenta
    
    def get_idCuenta(self) -> str:
        return self.__idCuenta
    
    def set_dominio(self, dominio: str):
        self.__dominio = dominio
    
    def get_dominio(self) -> str:
        return self.__dominio
    
    def set_tipoDominio(self, tipoDominio: str):
        self.__tipoDominio = tipoDominio
    
    def get_tipoDominio(self) -> str:
        return self.__tipoDominio
    
    def set_contrasenia(self, contrasenia: str):
        self.__contrasenia = contrasenia
    
    def get_contrasenia(self) -> str:
        return self.__contrasenia
    
    def retornaEmail(self) -> str:
        return f"{self.__idCuenta}@{self.__dominio}.{self.__tipoDominio}"
    
    
    def crearCuenta(self, direccion):
        separador1= direccion.split('@')
        separador2= separador1[1].split('.')

        idCuenta = separador1[0]
        dominio = separador2[0]
        tipoDominio = separador2[1]
        #contrasenia = str(input("Ingrese la contraseña: "))
        nuevoEmail= Email(idCuenta, dominio, tipoDominio, None)
        return nuevoEmail.retornaEmail()
    
    def modificarPassword(self):
        password_actual = input("Para cambiar la contraseña, ingrese primero la actual: ")
        if password_actual ==self.__contrasenia:
            nueva_password = input("Ingrese la nueva contraseña: ")
            self.__contrasenia = nueva_password
            print("Contraseña modificada exitosamente")
        else:
            print("Contraseña incorrecta")
        
    def validarEmail(self, direccion):
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        es_valido = re.match(patron, direccion)
        return es_valido is not None
        
        