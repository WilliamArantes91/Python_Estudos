faturamento = 1000
custo = 500
lucro = faturamento - custo

#str -> transforma um numero em uma string
#in -> verifica se um texto está contido dentro de outro
#Uso do str() e do concatenar com +
#format e {} -> substitui valores
#%s -> substitui textos
#%d -> substitui números decimais 

print('O faturamento da loja foi de: '+ str(faturamento))

print('O faturamento foi de: {}. O custo foi de {} e o lucro foi de {}'.format(faturamento,custo,lucro))

print('O faturamento da loja foi de: %d' % faturamento)

print('@' in 'william@gmail.com')
print('@' in 'William')




