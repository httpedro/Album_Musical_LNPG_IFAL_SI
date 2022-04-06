import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
 
#c=os.path.dirname(file)
#album_arquivo=c+"\\arquivo_cadastro.txt"
arquivo=open('arquivo_cadastro.txt',"a")
 
def gravar_dados():
    album = entry_album.get()
    ano_lancamento = entry_ano_lancamento.get()
    banda =entry_banda.get()
    primeiro_lancamento =radioValue.get()  
 
    if(album=="" or ano_lancamento=="" or banda=="" or primeiro_lancamento==""):
        messagebox.showinfo(title="ERRO", message="Preencha Todos os Dados")
    else:    
        if primeiro_lancamento == 1:
            primeiro_lancamento = 'Sim'
        else:
            primeiro_lancamento = 'Não'     

        arquivo.write(f'{album}|{ano_lancamento}|{banda}|{primeiro_lancamento}')
       
        entry_album.delete(0,END)
        entry_ano_lancamento.delete(0,END)
        entry_banda.delete(0,END)
        radioValue.set(1)

        arquivo.close()
 
def listar_dados():
    arquivo = open('arquivo_cadastro.txt',"r")
    bd = Tk()
    bd.title("Banco de dados")
    bd.geometry("600x400")
    
    tv = ttk.Treeview(bd,columns=('Álbum', 'Ano de Lançamento', 'Banda/Artista', 'Lançamento do Artista'), show='headings')
    tv.column('Álbum', minwidth=0,width=150)
    tv.column('Ano de Lançamento', minwidth=0,width=125)
    tv.column('Banda/Artista', minwidth=0,width=125)
    tv.column('Lançamento do Artista', minwidth=0,width=125)
    tv.heading('Álbum', text='Álbum')
    tv.heading('Ano de Lançamento', text='Ano de Lançamento')
    tv.heading('Banda/Artista', text='Banda/Artista')
    tv.heading('Lançamento do Artista', text='Lançamento')
    tv.pack(ipadx=10, ipady=10, padx=10, pady=10, fill='both', expand=True)

    for dados in arquivo:
        lista = dados.split('|')
        tv.insert('','end',values=(lista[0], lista[1], lista[2],lista[3]))
                
 
programa = Tk()
programa.title("CADASTRO")
programa.geometry("500x500")
programa.configure(background="#FFDBE9")
 
Label(programa, text="Escreva o nome do álbum",background="#FFDBE9",foreground="#000").pack()
entry_album=Entry(programa)
entry_album.pack()
 
Label(programa, text="Escreva o ano de lancamento",background="#FFDBE9",foreground="#000").pack()
entry_ano_lancamento=Entry(programa)
entry_ano_lancamento.pack()
 
Label(programa, text="Escreva o nome da banda/Artista",background="#FFDBE9",foreground="#000").pack()
entry_banda=Entry(programa)
entry_banda.pack()

radioValue=IntVar()
radioValue.set(1)
Label(programa, text="Primeiro Lançamento?",background="#FFDBE9",foreground="#000").pack()
radio1 = Radiobutton(programa, text='Sim',variable=radioValue, value=1, background="#FFDBE9",foreground="#000") 
radio2 = Radiobutton(programa, text='Não',variable=radioValue, value=2, background="#FFDBE9",foreground="#000")
radio1.pack()
radio2.pack()

Button(text="salvar",command=gravar_dados).pack(pady="5")
Button(text="Listar",command=listar_dados).pack()
 
   
programa.mainloop()