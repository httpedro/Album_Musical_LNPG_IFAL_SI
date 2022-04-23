import json

def gravar_dados(album, ano, artista, lancamento):
    newData = {
        'album': album,
        'ano': ano,
        'artista': artista,
        'lancamento': lancamento
        }
    with open('app-de-album/bd-json.json', 'r') as json_file:
        oldData = json.load(json_file)
    with open('app-de-album/bd-json.json', 'w') as json_file:
        oldData.append(newData)
        jsoned_data = json.dumps(oldData, indent=True)
        json_file.write(jsoned_data)


def preenche_bd():
    print()


def preenche_artista(artista):
    print()


def preencher_ano(op, ano):
    print()