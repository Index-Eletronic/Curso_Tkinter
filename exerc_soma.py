from tkinter import *

def click1():
    x = entrada1.get()
    y = entrada2.get()

    if x.isnumeric() and y.isnumeric():
        z = int(x) + int(y)
        Etiqueta['text'] = z
    else:
        Etiqueta['text']="Entre com dados validos"

janela=Tk()
janela['bg'] = ('lightgray')
Etiqueta = Label(janela, text='Primeiro numero: ', bg="lightgray")
Etiqueta.pack()

entrada1=Entry(janela, width=5)
entrada1.pack()

Etiqueta=Label(janela, text='Segundo numero: ', bg="lightgray")
Etiqueta.pack()

entrada2=Entry(janela, width=5)
entrada2.pack()

btn1=Button(janela, text="SOMAR", command=click1)
btn1.pack()

Etiqueta=Label(janela, text='', bg="lightgray")
Etiqueta.pack()

janela.geometry('500x400+50+200')
janela.mainloop()