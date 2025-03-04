from tkinter import*
from tkinter import ttk
def saludar():
    pass

ventana = Tk()
ventana.title("Mi calculadora")
ventana.geometry("400x200")
marco = ttk.Frame(ventana, padding=10)
marco.grid()
etiqueta =  ttk.Label(ventana, text="hola").grid(row=0, column=0)
boton = Button(text="ok",command =saludar).grid(row=0, column=1)
ventana.mainloop()
