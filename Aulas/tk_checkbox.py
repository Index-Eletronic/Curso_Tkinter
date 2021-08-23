from tkinter import *
janela = Tk()

def funcao():
    if var1.get() == 1:
        etq1['text'] = 'Opção 1 selecionada'
    else:
        etq1['text'] = ''
    if var2.get() == 1:
        etq2['text'] = 'Opção 2 selecionada'
    else:
        etq2['text'] = ''

var1=IntVar()
checbox1=Checkbutton(janela, text='Opção 1', variable=var1)
checbox1.pack()

var2=IntVar()
checkbox2=Checkbutton(janela, text='Opção 2', variable = var2)
checkbox2.pack()

btn=Button(janela, text='Selecionar', command=funcao)
btn.pack()

etq1 = Label(janela, text='')
etq1.pack()

etq2 = Label(janela, text='')
etq2.pack()


janela.geometry('500x400+50+200')
janela.resizable(width=0, height=0)
janela.mainloop()
