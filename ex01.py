lista = {}

def numero():
    return str(input('Informe um item: '))

while True:
    item = numero()
    if item == '':
        break
    valor = int(input('Informe o valor do item: '))
    lista[item] = valor

mai = max(lista.items())
print('O maior valor da lista: ', mai)