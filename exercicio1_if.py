vendas_funcionario1 = 1000
vendas_funcionario2 = 770
vendas_funcionario3 = 2700

#A meta de vendas é 1000, se o valor das vendas for maior ou igual a meta, o valor do bonus é de 10% do valor de vendas, caso contrário bonus = 0
meta_vendas = 1000

if vendas_funcionario1 >= meta_vendas:
    bonus = 0.1 * vendas_funcionario1
    print('Bonus do funcionário foi de {}'.format(bonus))
else:
    print('Funcionário 1 não ganhou bonus')

if vendas_funcionario2 >= meta_vendas:
    bonus = 0.1 * vendas_funcionario2
    print('Bonus do funcionário 2 foi de {}'.format(bonus))
else:
    print('Funcionário 2 não ganhou bonus')

if vendas_funcionario3 >= meta_vendas:
    bonus = 0.1 * vendas_funcionario3
    print('Bonus do funcionário 3 foi de {}'.format(bonus))
else:
    print('Funcionário 3 não ganhou bonus')