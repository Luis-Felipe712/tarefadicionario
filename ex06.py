dicionario = {'luis':'estudante','anderson':'professor', 'pc':'computador'}

def ordenar_chaves(dicionario):
    chaves_ordenadas = sorted(dicionario.keys())
    lista_ordenada = [(chave, dicionario[chave]) for chave in chaves_ordenadas]
    print(lista_ordenada)
        

ordenar_chaves(dicionario)