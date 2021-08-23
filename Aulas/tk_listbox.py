from tkinter import *

janela = Tk()
def selecao():
    etq['text'] ='Local é: ' + lista.get(ANCHOR)

et2 = Label(janela, text='Qual estado você mora?')
et2.pack()

frame = Frame(janela)
scrollbar = Scrollbar(frame, orient=VERTICAL)

lista = Listbox(frame, width=50, height=5, yscrollcommand=scrollbar.set)
scrollbar.config(command=lista.yview)
scrollbar.pack(side=RIGHT, fill=Y)
frame.pack()
lista.pack()

minhalista=['São Paulo','Rio de Janeio', 'Minas Gerais']
for item in minhalista:
    lista.insert(END, item) # Irá pegar os itens da lista e adiionar ao final

bt1=Button(janela, text='Selecionado', command=selecao)
bt1.pack()

etq=Label(janela, text=" ")
etq.pack()


janela.geometry('500x400+50+200')
janela.resizable(width=0, height=0)
janela.mainloop()