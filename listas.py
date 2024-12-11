produtos = ['tv','celular','mouse','teclado','tablet']
print(produtos)

vendas = [1000,1500,350,270,900]
print(vendas)

#lista[i] -> é o valor do indice i da lista
print(produtos[0]) #tv
print(vendas[0])#1000

#vendas[3] = 300
#print('Vendas do produto {} foram de {} unidades.'.format(produtos[3],vendas[3]))

texto = 'william@gmail.com' #Também é uma lista, porém a string em python é imutável
#texto[1] = 'x'
print(texto[0])

#Algumas funções Básicas de Lista

#Tamanho da lista
print('O tamanho da lista é: {}'.format(len(vendas)))

#Maior e menor valor da lista
print('O maior valor da lista é {} e o menor valor da lista é {}.'.format(max(vendas),min(vendas)))

ma = vendas.index(max(vendas))
me = vendas.index(min(vendas))

print('O produto mais vendido é o {} com {} unidades vendidas'.format(produtos[ma],max(vendas)))
print('O produto menos vendido é o {} com {} unidades vendidas'.format(produtos[me],min(vendas)))
