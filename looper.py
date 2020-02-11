import socket
import os
import time
os.system('clear')
def valor():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("~: "))
            correcto=True
        except ValueError:
            print('Error, introduce un valor del menu')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
 
    print ("1. Iniciar Looper")
    print ("2. Seleccionar ruta de imagenes")
    print ("3. Descargar las librerias y archivos")
    print ("4. Salir")
    nombre_equipo = socket.gethostname()
    direccion_equipo = socket.gethostbyname(nombre_equipo)
    print ("La IP es: %s" %direccion_equipo)
    print ("Introduce un valor del menu: ")
 
    opcion = valor()
 
    if opcion == 1:
        delay = int(input("Ingresar el delay de las imagenes: "))
	os.system('clear')
	os.system('feh -Z -x -F -Y -N -z -D {}'.format(delay))
    elif opcion == 2:
        print ("Opcion 2")
    elif opcion == 3:
	os.system('clear')
  	os.system('sudo apt-get install feh')
	os.system('sudo apt-get install xscreensaver')
	os.system('clear')
	print("Las librerias fueron descargadas/actualizadas")
	time.sleep(2)
	os.system('clear')
    elif opcion == 4:
        salir = True
    else:
        print ("Introduce un valor del menu")
 
print ("Cerrando...")
time.sleep(2)
os.system('clear')
