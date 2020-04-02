import sys, time
import serial 
from gtts import gTTS
import os
#mensaje_bienvenida = 'Bienvenido'
#mensaje_temperatura = 'procederemos a tomarle la temperatura'
#mensaje_rociador = 'procederemos a rociarle algo'
#mensaje_final = 'muchas gracias!'
#lenguaje = 'es'
#obj = gTTS(text=mensaje_bienvenida, lang=lenguaje, slow=False)
#obj.save("bienvenida.mp3")
#obj = gTTS(text=mensaje_temperatura, lang=lenguaje, slow=False)
#obj.save("temperatura.mp3")
#obj = gTTS(text=mensaje_rociador, lang=lenguaje, slow=False)
#obj.save("rociador.mp3")
#obj = gTTS(text=mensaje_final, lang=lenguaje, slow=False)
#obj.save("final.mp3")
arduino = serial.Serial('/dev/ttyUSB2', 9600)
def inicio():
    inicio_msg = arduino.read()
    inicio_msg = (inicio_msg.decode('utf-8'))
    print(inicio_msg)
    if (inicio_msg == "A"):
        os.system("mpg321 bienvenida.mp3")
        msg = ('Y')
        arduino.write(str.encode(msg))
        os.system("mpg321 temperatura.mp3")
        while True:
            lecturaDatos()
    else:
        print('No recibido')
        main()

def lecturaDatos():
    temperatura = arduino.readline() 
    print(temperatura)

def main():
    inicio()

if __name__ == "__main__":
    main()
