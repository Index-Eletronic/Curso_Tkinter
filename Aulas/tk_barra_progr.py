from tkinter import *
from tkinter.ttk import *
janela = Tk()

def funcao():
    barra['value'] = barra['value']+10
    et1['text'] = barra['value']


janela.geometry('500x400+50+200')
janela.resizable(width=0, height=0)

et1 = Label(janela, text='0%')
et1.pack()

barra = Progressbar(janela, length=400)
barra['value'] = 0 # Faz o avanço progreço da barra
barra.pack()

btn = Button(janela, text='Avanço', command=funcao)
btn.pack()

janela.mainloop()