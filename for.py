"""O for é uma estrutura que pode percorrer por exemplo uma lista
for i in lista de informações:

for i in range(5): #i é o indice
    print(i)"""

produtos = ['coca','pepsi','guarana','sprite','fanta']
producao = [15000, 12000, 13000, 5000, 250]

tamanho = len(produtos)
for i in range(tamanho):
    print('{} unidades produzidas de {}'.format(producao[i],produtos[i]))
