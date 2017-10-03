import sys

def quadrado(d):
    tuples = { i:d[i]**2 for i in d }
    return tuples

def join_tuples(a, b, c):
    lista = []
    lista.append(a)
    lista.append(b)
    lista.append(c)
    return lista
    
d = { 'boleto1': 9, 'boleto2': 3, 'boleto3': 0, 'boleto4': 5, 'boleto5': 1 }
print quadrado(d)
segundo_dicionario = { 'nome': 'atilla', 'idade' : 23, 'telefone': '991237973', 'endereco': 'itajuba' }
terceiro_dicionario = { 'nome': 'adolfo', 'idade' : 28, 'telefone': '99', 'endereco': 'sjc' }
quarto_dicionario = { 'nome': 'jose', 'idade' : 24, 'telefone': '129', 'endereco': 'itabira' }

lista_tuples = join_tuples(segundo_dicionario, terceiro_dicionario, quarto_dicionario)

for aux in lista_tuples:
    for key in aux:
        if key == 'nome' and aux[key] == 'atilla':
            print 'Minha idade e: ' + str(aux['idade'])

    
