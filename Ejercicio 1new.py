from Emailnew import Email 
import csv

if __name__ == '__main__':
    # 1- Ingresar el nombre de una persona y su dirección de e-mail (instancia de la clase Email)
    nombre = input("Ingrese el nombre: ")
    direccion = input("ingrese la direccion sin dominio:  ")
    dominio = input("ingrese el dominio @:   ")
    tipodom = input("ingrese el tipo dominio:  ")
    clave = input("ingrese la clave:  ")
    email = Email(direccion,dominio,tipodom,clave)
    direccion = email.retornaEmail()
    print(f"Estimado {nombre} te enviaremos tus mensajes a la dirección {direccion}")

    # 2- Modificar la contraseña
    #print("Contraseña anterior:", email.get_contrasenia())
    email.modificarPassword()
    # print("Contraseña nueva:", email.get_contrasenia())
    # 3- Crear un objeto de clase Email a partir de una dirección de correo
    nuevoEmail = input("ingrese la direccion de correo:  ")
    nuevo_Email = Email("", "", "", "")
    print (nuevo_Email.crearCuenta(nuevoEmail))
    
    # 4- a) Leer de un archivo separado por comas 10 direcciones de email, crear las cuentas correspondientes,
    # solo para las direcciones válidas, para las no válidas, mostrar mensaje de error indicando 
	#la dirección de email incorrecta.


with open('direcciones.csv') as f:  # Abre el archivo 'direcciones.csv' en modo lectura
    reader = csv.reader(f)  # Crea un objeto lector para leer el archivo CSV

    for row in reader:  # Itera sobre cada fila en el archivo CSV
        direccion = row[0]  # Obtiene la dirección de email de la primera columna de la fila
        email = Email("", "", "", "")  # Crea un objeto Email con la dirección de email
        if email.validarEmail(direccion):  # Valida si la dirección de email es válida
            
            email.crearCuenta(direccion)  # Crea la cuenta de email si la dirección es válida
        
        else:
            print(f"La dirección de email {direccion} es incorrecta.")  # Imprime un mensaje de error si la dirección es inválida
f.close()

