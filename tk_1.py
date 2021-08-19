from tkinter import *

janela = Tk()
janela.title("TUON MARCENARIA") # Titulo
janela.iconbitmap("logo.ico") # inserir logomarca
janela['bg'] = ("silver") # Alterando o background

def click1():
    #Etiqueta['text']='Botão 1'
    Etiqueta['text'] = 'Ola ' + entrada.get() # Etiqueta passa a receber os dados de entrada.


entrada = Entry(janela, width=80)
entrada.pack()
#ent = entrada.get() # Os dados que forem digitados entram na variavel ent.
entrada.insert(0, "Qual seu nome") # Preenche o campo de texto com a informação.


Etiqueta = Label(janela, text='Olá Mundo', bg="white", font=35)
Etiqueta.pack()

botao1=Button(janela, text="Teste", bg="blue", fg="yellow", padx="50", pady="30", command=click1)
botao1.pack()

btn = Button(janela, text='Sair', command=janela.quit)
btn.pack()

#Largura / Altura / E=dist da margem esquerda / T = dist do topo
janela.geometry('1000x400+500+300')
janela.mainloop()# Inicializador