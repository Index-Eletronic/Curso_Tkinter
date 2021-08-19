from tkinter import *

janela = Tk()


lista = Listbox(janela)
lista.pack()
lista.insert(END,'Teste 1')
lista.insert(END,'Teste 2')
lista.insert(END,'Teste 3')

janela.geometry('500x400+50+200')
janela.mainloop()