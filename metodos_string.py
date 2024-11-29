faturamento = 1000
print('Faturamento da loja foi de {}'.format(faturamento)) #Usamos o método format

#capitalize() : Coloca a primeira letra em maiuscula
texto = 'william'
print(texto.capitalize())

#casefold() : Transforma todas as letras em minúsculas (existe lower() mas o casefold é melhor normalmente)
texto = 'SOUZA'
print(texto.casefold())

#count() : Quantidade de vezes que um valor aparece na string
texto = 'williamarantes@gmail.com'
print(texto.count('l'))

#endswitch() :  Verifica se o texto termina com um valor especifico e dá como resposta True ou False
print(texto.endswith('m'))

#find() : Procura um texto dentro de outro texto e dá como resposta a posição do texto encontrado
print(texto.find('@'))

#isalnum() : Verifica se um texto é todo feito com caracteres alfanuméricos (letras e números) -> letras com acento ou ç são considerados letras para essa função
texto = 'João123'
print(texto.isalnum())

#isalpha() : Verifica se um texto é todo feito de letras
print(texto.isalpha())

#isnumeric(): Verifica se um texto é todo feito por números
texto = '123'
print(texto.isnumeric())

#replace() : Substitui um texto por um outro texto em uma string
texto = '1000.00'
print(texto.replace('.','/'))

#split() : Separa uma string de acordo com um delimitador em vários textos diferentes
texto = 'william@gmail.com'
print(texto.split('@'))

#splitlines() : Separa um texto em vários textos de acordo com os "enters" do texto
texto = '''Olá, bom dia
venho por meio deste e-mail lhe informar o faturamento da loja no dia de hoje.
Faturamento = R$2.500,00
'''
print(texto.splitlines())

#startswith() : Verifica se a string começa com determinado texto
texto = ' BEB12343'
print(texto.startswith('BEB'))

#strip() : Retira caracteres indesejados dos textos. Por padrão, retira espaços extras no início e no final
print(texto.strip())

#title() : Coloca a primeira letra de cada palavra em maiuscula
texto = 'william souza arantes'
print(texto.title())

#upper() : Coloca o texto todo em letra maiuscula
print(texto.upper())