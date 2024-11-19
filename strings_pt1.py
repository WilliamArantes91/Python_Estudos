email = 'william@gmail.com'
nome = 'William Arantes'

#Tamanho da string
print(len(nome))

#Pegar um item de uma string
print(nome[0]) #W
print(nome[6]) #m

#Para pegar um texto de trás para frente: texto[indice] -> onde indice é negativo
# w   i   l   l   i   a   m   @   g  m  a  i  l  .  c  o  m
#-17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1    

print(email[-2])                         

#Para pegar o pedaço de um texto use: (dois pontos). ou texto[indice:] ou ainda texto[indice:indice]
print(email[:-1])

