from tkinter import *
janela = Tk()
janela.title("TUON MARCENARIA") # Titulo
janela.geometry('500x500+100+100')
janela['bg'] = ("silver") # Alterando o background

lb1 = Label(janela, text='Etiqueta 1', bg='green')
lb1.pack(fill=X)

lb2 = Label(janela, text='Etiqueta 2', bg='red')
lb2.pack(side=LEFT, fill=BOTH)

lb3 = Label(janela, text='Etiqueta 3', bg='blue')
lb3.pack(expand=1, fill=BOTH)

En1 = Entry(janela)
En2 = Entry(janela)


bt = Button(janela, text='Avançar')

janela.mainloop()