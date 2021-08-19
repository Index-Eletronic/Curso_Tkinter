from tkinter import *
janela = Tk()
janela.title("TUON MARCENARIA") # Titulo
janela.geometry('800x500+100+100')
janela['bg'] = ("silver") # Alterando o background

lb1 = Label(janela, text='Login')
lb1.grid(column=0, row=0)
lb2 = Label(janela, text='Senha')
lb2.grid(column=0, row=1)

En1 = Entry(janela)
En1.grid(column=1, row=0, padx=(50,50))
En2 = Entry(janela)
En2.grid(column=1, row=1)

bt = Button(janela, text='Avançar')
bt.grid(column=0, row=2, columnspan= 2) # columnspan mescla a quatidade de celulas definidas ( 2 ).
janela.mainloop()