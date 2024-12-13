#O Enumerate permite que você percorra uma lista e ao mesmo tempo tenha em uma variável o índice daquele item.

"""funcionarios = ['Maria','José','Antônio','João','Francisco','Ana','Luiz','Paulo','Carlos','Manoel','Pedro','Francisca','Marcos','Raimundo','Sebastião',
                'Antonia','Marcelo','Jorge','Márcia','Geraldo','Adriana','Sandra','Luis']

for funcionario in funcionarios:
    print(funcionario)

for i, funcionario in enumerate(funcionarios):
    print('{} é o funcionário {}'.format(i,funcionario))"""

#OBS: Usamos enumarate somente se precisar utilizar o indice 
#Em uma fábrica você tem vários produtos e não pode deixar que os produtos fiquem em falta. Para isso, foi definido uma quantidade
#mínima de estoque que os produtos precisam ter.
#Identifique quais produtos estão abaixo do nível mínimo do estoque

estoque = [1200,300,800,49,1900,2750,400,20,23,70]
produtos = ['coca','pepsi','guarana','skol','brahma','agua','del valle','red bull','cachaça','vinho']
nivel_minimo = 50



for i, qtde in enumerate(estoque):
    if qtde < nivel_minimo:
        print('O estoque do produto {} está em {}, por favor, fazer a reposição da mercadoria!'.format(produtos[i],qtde))