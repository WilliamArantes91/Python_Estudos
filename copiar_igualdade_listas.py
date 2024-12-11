#Quando fazemos lista2 = lista não estamos criando uma lista nova, mas estamos atribuindo outra variável a mesma lista.
#Se quisermos copiar a lista devemos fazer lista2 = lista.copy() ou então lista2 = lista1[:]

lista = ['ipad','iphone x','apple tv']
lista2 = lista

lista2.append('macbook')

print(lista)

lista3 = lista.copy()

lista.append('qualquer_coisa')

print(lista)
print(lista2)
print(lista3)