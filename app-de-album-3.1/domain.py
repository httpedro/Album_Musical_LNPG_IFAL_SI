# Importa as funções do banco de dados
import bdjson
# Essa função recebe os valores das entrys e do radioValue no gui.py e as envia para a função do bd.py
def gravar_dados(album, ano, artista, lancamento):
    
    bdjson.gravar_dados(album, ano, artista, lancamento)


# Aqui é chamada a função para preencher a TreeView do banco de dados no gui.py armazenando os valores recebidos pelo
# bd.py em uma matriz e a retorna para o gui.py.
def preencher_bd():

    matriz = bdjson.preenche_bd()
    return matriz


# Aqui é chamada a função para preencher a TreeView da tela de Busca por artista no gui.py, enviando como parâmetro o 
# artista digitado. E retorna uma matriz com os valores recebidos pelo bd.py.
def preencher_artista(artista):

    matriz = bdjson.preenche_artista(artista)
    return matriz


# Aqui é chamada a função para preencher a TreeView da tela de Busca por ano no gui.py, enviando como parâmetro a opção da 
# ComboBox e o ano digitado. Além disso, retorna uma matriz com os valores recebidos pelo bd.py.
def preencher_ano(op, ano):
    
    matriz = bdjson.preenche_ano(op, ano)
    return matriz
