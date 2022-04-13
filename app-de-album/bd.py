# import os 

#Função Recebe Parametros da lista e adiciona os dados no arquivo_cadastro.txt
def gravar_dados(album, ano, artista, lancamento):
    # c=os.path.dirname(_file_)
    # album_arquivo=c+"\\arquivo_cadastro.txt"
    arquivo=open('app-de-album/arquivo_cadastro.txt',"a")

    arquivo.write(f'{album}|{ano}|{artista}|{lancamento}\n')
     
    arquivo.close()

# Função que cria uma matriz com todos os valores do banco de dados e a retorna para o domain.py
def preenche_bd():
    arquivo = open('app-de-album/arquivo_cadastro.txt',"r")
    matriz = []

    for dados in arquivo:
        lista = dados.split('|')
        matriz.append(lista)

    arquivo.close()
    return matriz

# Função percorre a lista do banco de dados e verifica se o artista existe, listando assim elementos especificos na treeview 
def preenche_artista(artista):
    arquivo = open('app-de-album/arquivo_cadastro.txt',"r")
    matriz = []

    for dados in arquivo:
        lista = dados.split('|')
        for x in range(len(artista)):
            if (str(artista[x]).lower() in lista[2].lower()):
                matriz.append(lista)
                break

    arquivo.close()
    return matriz

# Função recebe 2 parâmetros, percorre a lista e verifica o(s) ano(s) de acordo com a opção escolhida na ComboBox.
# Retornando elementos especificos para a Treeview da tela
def preenche_ano(op, ano):
    arquivo = open('app-de-album/arquivo_cadastro.txt',"r")
    matriz = []

    for dados in arquivo:
        lista = dados.split('|')

        if op == "Anterior a":
            if int(ano) >= int(lista[1]):
                matriz.append(lista)

        elif op == "Posterior a":
            if int(ano) <= int(lista[1]):
                matriz.append(lista)

        elif op == "Igual a":
            if int(ano) == int(lista[1]):
                matriz.append(lista)

    arquivo.close()
    return matriz