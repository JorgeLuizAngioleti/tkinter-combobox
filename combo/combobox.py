from tkinter import *
from tkinter import ttk
import sqlite3
root=Tk()

def nomes():
    if not a1.get() or not au.get():
        print('erro')
    else:
        try:
            conexao = sqlite3.connect("exemplo.sqlite") 
            cursor = conexao.cursor() 
            cursor.execute('''create table if not exists pessoas(nome text unique,turma text)''')
            b=a1.get().upper()
            c=au.get().upper()
            cursor.execute('''insert into pessoas ( nome,turma ) values(?,?)''', (b,c)) 
            conexao.commit()                
            cursor.close() 
            conexao.close()
            print('gravado com sucesso!')
        except:
            print('este nome já existe')
def list_pac():
        lista = []
        conexao = sqlite3.connect("exemplo.sqlite")
        cursor = conexao.cursor()
        cursor.execute("SELECT rowid,nome,turma FROM pessoas ORDER BY nome")
        for record in cursor:
            lista.append(record[1])#0 imprime id 1 imprime nome 2 turma
            print(record)
        return tuple(lista)
def listar():
    box['value']=list_pac()#posso colocar fora da função

lb1=Label(root,text="nome")
lb1.grid()
a1=Entry(root)
a1.grid()
lb2=Label(root,text="turma")
lb2.grid()
# aula
au = StringVar(root)
aa = ('1ºano mat','2ºano mat','3ºano mat','4ºano mat','5ºano mat','6ºano mat','7ºano mat','8ºano mat','9ºano mat','\n',
      '1ºano vesp','2ºano vesp','3ºano vesp','4ºano vesp','5ºano vesp','6ºano vesp','7ºano vesp','8ºano vesp','9ºano vesp')

option = OptionMenu(root, au, *aa)
option.grid()
bt1=Button(root,text="gravar",command=nomes)
bt1.grid()
bt2=Button(root,text="listar",command=listar)
bt2.grid()
nomes = StringVar()
box = ttk.Combobox(root,width=50, textvariable=nomes)
box['values'] ='Nomes'
box.current(0)#indica para imprimir o primeiro intem da lista(nomes)
box.grid()


root.mainloop()
