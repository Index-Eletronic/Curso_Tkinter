from tkinter import *
janela = Tk()

def funcao():
    Selecionado = 'Você selecionou a opção' + str(var.get())
    etq1['text'] = Selecionado

var=IntVar()
radiobt1 = Radiobutton(janela, text='Opção 1', variable=var, value=1)
radiobt1.pack()

radiobt2 = Radiobutton(janela, text='Opção 2', variable=var, value=2)
radiobt2.pack()

radiobt3 = Radiobutton(janela, text='Opção 3', variable=var, value=3)
radiobt3.pack()



btn=Button(janela, text='Selecionar', command=funcao)
btn.pack()

etq1 = Label(janela, text='')
etq1.pack()

janela.geometry('500x400+50+200')
janela.resizable(width=0, height=0)
janela.mainloop()