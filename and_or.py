"""if condicao_1 and condicao_2:
        vai ser executado se as duas condições forem verdadeiras ao mesmo tempo
    
    if condicao_1 or condicao_2:
        vai ser executado se pelo menos uma das condições forem verdadeiras """

meta_funcionario = 10000
meta_loja = 25000
vendas_funcionario = 5000
vendas_loja = 200000

"""if vendas_funcionario > meta_funcionario and vendas_loja > meta_loja:
    bonus = 0.03 * vendas_funcionario
    print('Bonus do funcionario foi de: {}'.format(bonus))
else:
    print('Funcionario não ganhou bonus')"""

nota_funcionario = 9
meta_nota = 9

if nota_funcionario >= meta_nota or (vendas_funcionario > meta_funcionario and vendas_loja > meta_loja):
    bonus = 0.03 * vendas_funcionario
    print('Bonus do funcionário foi de {}'.format(bonus))
else:
    print('Funcionário não ganhou bonus')