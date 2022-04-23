from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import messagebox
# Importa as funções do domain.py
from domain import *

# Função cria uma treeview 
def treeview_bd(screem):

    treeview = ttk.Treeview(screem,columns=('Álbum', 'Ano de Lançamento', 'Banda/Artista', 'Lançamento do Artista'), show='headings')
    treeview.column('Álbum', minwidth=0,width=150)
    treeview.column('Ano de Lançamento', minwidth=0,width=125)
    treeview.column('Banda/Artista', minwidth=0,width=125)
    treeview.column('Lançamento do Artista', minwidth=0,width=125)
    treeview.heading('Álbum', text='Álbum')
    treeview.heading('Ano de Lançamento', text='Ano de Lançamento')
    treeview.heading('Banda/Artista', text='Banda/Artista')
    treeview.heading('Lançamento do Artista', text='Lançamento')
    treeview.pack(padx=10,pady=10,fill='both', expand=True)

    return treeview


# Função criada para fazer a view da tabela que mostra o que tem no bd
def banco_dados_screem():
    
    banco_dados_screem = Tk()
    banco_dados_screem.title("Banco de dados")
    banco_dados_screem.geometry("600x600")
    banco_dados_screem.configure(background="#FFDBE9")

    banco_de_dados_texto = Label(banco_dados_screem, text="Deseja fazer buscas no banco de dados?",background="#FFDBE9")
    banco_de_dados_texto.pack()

    btn_artista = Button(banco_dados_screem, text='Realizar busca por artista', width=40,command=busca_por_artista)
    btn_artista.pack()  
    btn_ano = Button(banco_dados_screem, text="Realizar busca por ano", width=40, command=busca_por_ano)  
    btn_ano.pack()
    # Chama a função para criar a TreeView
    treeview = treeview_bd(banco_dados_screem)
    # Chama a função do domain.py para preencher a TreeView que por sua vez fará o pedido para o bd.py
    lista = preencher_bd()
    # Preenche a TreeView
    for dados in lista:
        treeview.insert('','end',values=(dados))   
    
    banco_dados_screem.mainloop()         

# Função que cria a tela de busca por artista
def busca_por_artista():
    # Essa Função apaga os dados da TreeView caso tenha algum, chama a função para preenche-la pelo domain.py
    # enviando o artista digitado como parâmetro. Depois de receber a matriz com os devidos valores insere-os na TreeView
    def busca(artista:str):
        artista = artista.split(', ')
        # Apaga
        treeview.delete(*treeview.get_children())
        # Chama
        lista = preencher_artista(artista)
        # Preenche
        for dados in lista:
            treeview.insert('','end', values=(dados))


    busca_artista_screem = Tk()
    busca_artista_screem.title("Busca por Artista")
    busca_artista_screem.geometry("600x600")
    busca_artista_screem.configure(background="#FFDBE9")
    
    busca_artista_label = Label(busca_artista_screem, text="Digite o Artista/Banda que deseja procurar", background="#FFDBE9")
    busca_artista_label.pack(ipady=10)
    busca_artista_label2 = Label(busca_artista_screem, background="#FFDBE9")
    busca_artista_label2.pack(side=TOP)

    busca_artista = Entry(busca_artista_screem, bd=2)
    busca_artista.place(x=10, y=40, width=500)

    # Lambda permite enviar parametros dentro do command
    btn = Button(busca_artista_screem, text="Buscar",width=8, command=lambda:busca(busca_artista.get()))
    btn.place(x=520, y=37)

    treeview = treeview_bd(busca_artista_screem)

    busca_artista_screem.mainloop()


# Função que cria a tela de busca por ano
def busca_por_ano():
    # Essa Função apaga os dados da TreeView caso tenha algum, chama a função para preenche-la pelo domain.py
    # enviando a opção e o ano digitado como parâmetro. Depois de receber a matriz com os devidos valores insere-os na TreeView
    def busca(op, ano):
        # Apaga
        treeview.delete(*treeview.get_children())
        # Chama
        lista = preencher_ano(op, ano)
        # Preenche
        for dados in lista:
            treeview.insert('','end', values=(dados['album'], dados['ano'], dados['artista'], dados['lancamento']))


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
    # Lambda permite enviar parametros dentro do command
    bd_busca_ano = Entry(busca_ano_screem, bd=2)
    bd_busca_ano.place(x=260, y=40)
    btn = Button(busca_ano_screem, text="Buscar",width=15, command=lambda:busca(op_ano.get(), bd_busca_ano.get()))
    btn.place(x=400, y=37)

    treeview = treeview_bd(busca_ano_screem)
    busca_ano_screem.mainloop()


# Função da view principal que cadastra banda
def main():
    # Função que grava dados no arquivo a partir dos parâmetros pegos nas Entrys e radioValue
    # a função também limpa os dados da label após salvar os dados 
    def grava_e_limpa_dados(album, ano, banda, lancamento):
        # Tratamento de erros
        if(album=="" or ano=="" or banda==""):
            messagebox.showinfo(title="ERRO", message="Preencha Todos os Dados")
        while True:
            if(ano!=''):
                try:
                    ano = int(ano)  
                    break            
                except ValueError:
                    entry_ano_lancamento.delete(0,END)
                    messagebox.showerror(title='ERRO', message='Valor para ANO inválido!')
            break
        if ano <= 0:
            entry_ano_lancamento.delete(0,END)
            messagebox.showerror(title='ERRO', message='Valor para ANO DEVE ser maior que ZERO')
        else:
            # Chama a função para gravar
            gravar_dados(album, ano, banda, lancamento)
            # Limpa os dados nas entry e reseta o valor do radio
            entry_album.delete(0,END)
            entry_ano_lancamento.delete(0,END)
            entry_banda.delete(0,END)
            radioValue.set('Sim')
    
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

    radioValue=StringVar()
    radioValue.set('Sim')
    Label(programa, text="Primeiro Lançamento?",background="#FFDBE9",foreground="#000").pack()
    radio1 = Radiobutton(programa, text='Sim',variable=radioValue, value='Sim', background="#FFDBE9",foreground="#000") 
    radio2 = Radiobutton(programa, text='Não',variable=radioValue, value='Não', background="#FFDBE9",foreground="#000")
    radio1.pack()
    radio2.pack()

    # Lambda permite enviar parâmetros dentro do command
    Button(text="Salvar",width=25, command=lambda:grava_e_limpa_dados(entry_album.get(), entry_ano_lancamento.get(), entry_banda.get(), radioValue.get())).pack(pady="5")
    Button(text="Banco de dados",width=25, command=banco_dados_screem).pack()
    
    programa.mainloop()


# Executa o programa
main()
