"""O for no Python consegue percorrer uma lista e a cada loop retornar ao valor do item
for i in range(5):
    print(i)
    range(5) é na verdade uma lista do tipo: [0,1,2,3,4]
    
    Usando para listas:
    for item in lista:
        print(item)
        
        ou então para string:
        for ch in texto:
            print(ch)

produtos = ['coca','pepsi','guarana','sprite','fanta']
texto = 'william@gmail.com'

for produto in produtos:
    print(produto)

for ch in texto:
    print(ch)"""

vendas = [1200,300,800,1500,1900,2750,400,20,23,70,90,80,1100,999,900,880,870,50,1111,120,300,450,800]

#Digamos que a gente esteja analisando a meta de vendas de vários funcionários de uma empresa. A meta de vendas é de 1000 em 1 dia.
#Temos uma lista com as vendas de todos os funcionários e quero calcular qual o % de pessoas que bateram a meta
vendas_meta = 0

meta = 1000
for venda in vendas:
    if venda >= meta:
        vendas_meta+=1

meta_batida = (vendas_meta/len(vendas))*100

print('{:.1f}% dos funcionários bateram a meta do dia!'.format(meta_batida))

