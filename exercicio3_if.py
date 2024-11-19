alimentos_min = 50
bebidas_min = 75
limpeza_min = 30

nome = input('Informe o nome do produto: ')
categoria = input('Informe a categoria do produto: ')
estoque = int(input('Informe a quantidade atual em estoque: '))

if nome == '' or categoria == '' or estoque == '':
    print('Preencha corretamente os dados')
elif categoria == 'bebidas' and estoque <= bebidas_min:
    print('Solicitar {} a equipe de compras, temos apenas {} unidades em estoque.'.format(nome,estoque))
elif categoria == 'alimentos' and estoque <= alimentos_min:
    print('Solicitar {} a equipe de compras, temos apenas {} unidades em estoque.'.format(nome,estoque))
elif categoria == 'limpeza' and estoque <= limpeza_min:
    print('Solicitar {} a equipe de compras, temos apenas {} unidades em estoque.'.format(nome,estoque))
