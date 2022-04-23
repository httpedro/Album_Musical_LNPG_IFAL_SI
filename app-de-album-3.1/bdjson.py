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
    with open('app-de-album-3.1/bd-json.json', 'r') as json_file:
        arquivo = json.load(json_file)
        matriz = []

        for dados in arquivo:
            for x in range(len(artista)):
                if (str(artista[x]).lower() in dados['artista'].lower()):
                    matriz.append(dados)
                    break
    return matriz


def preencher_ano(op, ano):
    
    with open('app-de-album-3.1/bd-json.json', 'r') as json_file:
        data = json.load(json_file)    
        matriz = []
        for values in data:

            if op == "Anterior a":
                if int(ano) >= int(values['ano']):
                    matriz.append(values)

            elif op == "Posterior a":
                if int(ano) <= int(values['ano']):
                    matriz.append(values)

            elif op == "Igual a":
                if int(ano) == int(values['ano']):
                    matriz.append(values)

    return matriz
