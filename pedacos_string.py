precos = 'Jan: 25, Fev: 27, Mar:29'
preco_jan = precos[5:7] #Primeiro caractere - Inclusivo / Ultimo caractere - Exclusivo
preco_mar = precos[-2:]
preco_fev = precos[-10:-8]

print(preco_jan)
print(preco_mar)
print(preco_fev)

#Posição Inicial e Final com Step
codigo = '1.2.3.4,5,1,2.3.4,7.9'
pedaco_cod = codigo[2:10:2] #[inicio:fim: de quanto em quanto]
print(pedaco_cod)
