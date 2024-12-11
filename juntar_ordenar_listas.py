produtos = ['apple tv','mac','iphone x','iphone 11','ipad','apple watch','Macbook','airpods']
novos_produtos = ['iphone 12','ioculos']
vendas = [1000,1500,15000,20000,270,900,100,1200]
vendas_iphonex = [15000]
vendas_iphone11 = [20000]

#Juntar listas
produtos.extend(novos_produtos) #Ou seja, a lista produtos receberá os novos itens
print(produtos)

#Podemos juntar duas listas, porém, será criada uma terceira variável lista_nova = lista1+lista2
nova_lista = novos_produtos+produtos #Sim, a ordem importa
print(nova_lista)

total_iphone = vendas[2] + vendas[3]
print(total_iphone)
total_iphone_listas = vendas_iphone11+vendas_iphone11
print(total_iphone_listas)

#Ordenar listas

produtos.sort()
print(produtos) #Cuidado! O Python ordena os itens de acordo com a tabela ASCII, suponhamos que tenha algum item com a letra maiuscula,
#seria então o primeiro item da lista
vendas.sort(reverse=True) #Ao contrário por exemplo
print(vendas)