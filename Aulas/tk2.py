from tkinter import *

janela = Tk()
janela.title("TUON MARCENARIA") # Titulo
janela.geometry('800x500+100+100')
janela['bg'] = ("silver") # Alterando o background

bt1 = Button(janela, text='Botão 1')
#Valores para x e para y
bt1.place(x=400, y=250) # Gereniador de layout.
bt2 = Button(janela, text='Botão 2')
bt2.place(x=400, y=300)# Gereniador de layout.

En = Entry(janela)
En.place(x=450, y=250, anchor=NW) # anchor permite mudar a orientação do alinhamento ( conforme a bulsola ) north soult lest oest north west...
janela.mainloop()