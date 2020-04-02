from tkinter import *
import time
def inicio():
    window = Tk()

    window.title("Welcome to LikeGeeks app")

    data = "Puto"
    lbl = Label(window, text=data, font=("Arial Bold", 50))

    lbl.grid(column=0, row=0)

def menu():
    windows = Tk()
    window.title("Welcome")
    data = "Hola"
    lbl = Label(window, text = data, font=("Arial Bold", 50))
    lbl.grid (column=0, row=0)
    window.mainloop()

def main():
    inicio()
    menu()

main()
