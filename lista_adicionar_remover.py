#Adicionar -> lista.append(item) OBS: sempre adiciona no final da lista
#Remover -> lista.pop(indice) / lista.remove(item)

produtos = ['apple tv','mac','iphone x','ipad','apple watch','macbook','airpods']

print(produtos)
#adicionar o iphone 11
produtos.append('iphone 11')
print(produtos)

#remover o iphone x
#produtos.remove('iphonex')
#produtos.pop(2)
print(produtos)

#Suponhamos que escrevi 'iphonex' irá acontecer um erro ValueError? list.remove(iphonex): iphonex no in list, como tratamos este erro?
try:
    produtos.remove('iphonex')
except:
    print('{} não existe na lista de produtos'.format('iphonex')) #Caso eu não queira que aconteça nada, inclua a palavra pass

#metodo join -> texto.join(lista) :  pega todos os itens da lista e separa conforme delimitador
print('\n'.join(produtos))

#Método split: transforma uma string em uma lista pelo delimitador
lista = 'apple tv,mac,iphone x,ipad,apple watch,macbook,airpods'
print(lista.split(','))



