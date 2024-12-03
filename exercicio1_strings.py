"""Cadastro de CPF - Caso o usuário digite algo diferente de números ou digite menos de 11 caracteres, o programa deve exibir
uma mensagem de "Digite seu CPF corretamente e digite apenas números.

- Permita que o usúario insira pontos, traços e espaços vazios, pórem nós que devemos tratar os que o usuário inserir para padronizar o CPF
- A verificação de tamanho do CPF com 11 caracteres continua válida, mas ela só deve ser feita depois de retirar todos os pontos, traços e espaços vazios
ou seja, deve sobrar apenas números no cpf.
- Exibir uma menasgem para o usuário, caso ele tenha inserido CPF inválido ou então apenas deve pritar o CPF correto já só com números"""

#tratar o cpf
#tirar espaços no inicio e no final, tirar os pontos, tirar os traços

cpf = input('Insira seu CPF:')
cpf = cpf.strip()
cpf = cpf.replace('.','')
cpf = cpf.replace('-','')

if len(cpf) == 11 and cpf.isnumeric():
    print(cpf)
else: 
    print('Digite seu CPF corretamente, e digite apenas números')