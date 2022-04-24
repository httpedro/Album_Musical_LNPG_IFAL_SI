import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Combobox


def limpa_dados():

    entry_album.delete(0,END)
    entry_ano_lancamento.delete(0,END)
    entry_banda.delete(0,END)
    radioValue.set(1)


def gravar_dados():
    # c=os.path.dirname(__file__)
    # album_arquivo=c+"\\arquivo_cadastro.txt"
    arquivo=open('arquivo_cadastro.txt',"a")

    album = entry_album.get()
    ano_lancamento = entry_ano_lancamento.get()
    banda = entry_banda.get()
    primeiro_lancamento = radioValue.get()  

    if(album=="" or ano_lancamento=="" or banda=="" or primeiro_lancamento==""):
        messagebox.showinfo(title="ERRO", message="Preencha Todos os Dados")
    else:    
        if primeiro_lancamento == 1:
            primeiro_lancamento = 'Sim'
        else:
            primeiro_lancamento = 'Não'     

        arquivo.write(f'{album}|{ano_lancamento}|{banda}|{primeiro_lancamento}\n')

        limpa_dados()
        arquivo.close()


def banco_dados():

    arquivo = open('arquivo_cadastro.txt',"r")
    bd_screem = Tk()
    bd_screem.title("Banco de dados")
    bd_screem.geometry("600x600")
    bd_screem.configure(background="#FFDBE9")

    # bd_label = Label(bd_screem, background="#FFDBE9")
    # bd_label.pack(side=TOP, pady=40)
    bd_texto = Label(bd_screem, text="Deseja fazer buscas no banco de dados?",background="#FFDBE9")
    bd_texto.pack()

    btn_artista = Button(bd_screem, text='Realizar busca por artista', width=40,command=busca_por_artista)
    btn_artista.pack()  
    btn_ano = Button(bd_screem, text="Realizar busca por ano", width=40, command=busca_por_ano)  
    btn_ano.pack()

    tv = treeview_bd(bd_screem)

    for dados in arquivo:
        lista = dados.split('|')
        tv.insert('','end',values=(lista))
    arquivo.close()
    bd_screem.mainloop()         


def treeview_bd(screem):

    tv = ttk.Treeview(screem,columns=('Álbum', 'Ano de Lançamento', 'Banda/Artista', 'Lançamento do Artista'), show='headings')
    tv.column('Álbum', minwidth=0,width=150)
    tv.column('Ano de Lançamento', minwidth=0,width=125)
    tv.column('Banda/Artista', minwidth=0,width=125)
    tv.column('Lançamento do Artista', minwidth=0,width=125)
    tv.heading('Álbum', text='Álbum')
    tv.heading('Ano de Lançamento', text='Ano de Lançamento')
    tv.heading('Banda/Artista', text='Banda/Artista')
    tv.heading('Lançamento do Artista', text='Lançamento')
    tv.pack(padx=10,pady=10,fill='both', expand=True)

    return tv


def busca_por_artista():

    def busca():
        arquivo = open('arquivo_cadastro.txt',"r")
        tv.delete(*tv.get_children())
        valor = str(bd_busca_artista.get())

        for linha in arquivo:
            dados = linha.split('|')

            if valor.lower() in dados[2].lower():
                tv.insert('', 'end', values=(dados))

        arquivo.close()

    busca_artista_screem = Tk()
    busca_artista_screem.title("Busca por Artista")
    busca_artista_screem.geometry("600x600")
    busca_artista_screem.configure(background="#FFDBE9")

    busca_artista_label = Label(busca_artista_screem, text="Digite o Artista/Banda que deseja procurar", background="#FFDBE9")
    busca_artista_label.pack(ipady=10)
    busca_artista_label2 = Label(busca_artista_screem, background="#FFDBE9")
    busca_artista_label2.pack(side=TOP)

    bd_busca_artista = Entry(busca_artista_screem, bd=2)
    bd_busca_artista.place(x=10, y=40, width=500)

    btn = Button(busca_artista_screem, text="Buscar",width=8, command=busca)
    btn.place(x=520, y=37)

    tv = treeview_bd(busca_artista_screem)


def busca_por_ano():

    def busca():
        arquivo = open('arquivo_cadastro.txt',"r")
        tv.delete(*tv.get_children())
        valor_opcao = str(op_ano.get())
        valor_ano = int(bd_busca_ano.get())

        for linha in arquivo:
            dados = linha.split('|')

            if valor_opcao == "Anterior a":
                if int(valor_ano) >= int(dados[1]):
                    tv.insert('', 'end', values=(dados))

            elif valor_opcao == "Posterior a":
                if int(valor_ano) <= int(dados[1]):
                    tv.insert('', 'end', values=(dados))

            elif valor_opcao == "Igual a":
                if int(valor_ano) == int(dados[1]):
                    tv.insert('', 'end', values=(dados))

        arquivo.close()

    busca_ano_screem = Tk()
    busca_ano_screem.title("Busca por Ano")
    busca_ano_screem.geometry("600x600")
    busca_ano_screem.configure(background="#FFDBE9")

    busca_ano_label = Label(busca_ano_screem, text="Preencha os campos para realizar a busca", background="#FFDBE9")
    busca_ano_label.pack(ipady=10)
    busca_ano_label2 = Label(busca_ano_screem, background="#FFDBE9")
    busca_ano_label2.pack(side=TOP)

    opcoes = ("Posterior a", "Anterior a", "Igual a")
    op_ano = Combobox(busca_ano_screem, values=opcoes)
    op_ano.place(x=100, y=40)

    bd_busca_ano = Entry(busca_ano_screem, bd=2)
    bd_busca_ano.place(x=260, y=40)
    btn = Button(busca_ano_screem, text="Buscar",width=15, command=busca)
    btn.place(x=400, y=37)

    tv = treeview_bd(busca_ano_screem)

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

Button(text="Salvar",width=25, command=gravar_dados).pack(pady="5")
Button(text="Banco de dados",width=25, command=banco_dados).pack()

programa.mainloop()
