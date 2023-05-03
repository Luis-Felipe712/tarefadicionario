lista = {}

def insertNome():
    return str(input('Informe o nome: '))
def insertIdade():
    return int(input('Informe a idade: '))

while True:
    nome = insertNome()
    if nome == '':
        break

    idade = insertIdade()
    lista[nome] = {
        'idade': idade
    }

for i, d in lista.items():
    if d['idade'] > 18:
        print('nome:', i ,'idade:', d['idade'])