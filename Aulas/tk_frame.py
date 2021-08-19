from tkinter import *

janela = Tk()

frame1 = Frame(janela, padx=20, pady=20) # Frame comum.
frame1.grid(row=0, column=0)

Et1=Label(frame1, text="Etiqueta 1")
Et1.pack()
bt1=Button(frame1, text="Botão 1")
bt1.pack()

frame2 = LabelFrame(janela, padx=20, pady=20, text='Frame2') # Label Frame
frame2.grid(row=0, column=1)

Et2=Label(frame2, text="Etiqueta 2")
Et2.pack()
bt2=Button(frame2, text="Botão 2")
bt2.pack()

janela.geometry('500x400+50+200')
janela.mainloop()
