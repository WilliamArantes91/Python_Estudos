produtos = ['tv','celular','mouse','teclado','tablet']
print(produtos)

vendas = [1000,1500,350,270,900]
print(vendas)

#lista[i] -> é o valor do indice i da lista
print(produtos[0]) #tv
print(vendas[0])#1000

vendas[3] = 300
print('Vendas do produto {} foram de {} unidades.'.format(produtos[3],vendas[3]))

texto = 'william@gmail.com' #Também é uma lista, porém a string em python é imutável
#texto[1] = 'x'
print(texto[0])

