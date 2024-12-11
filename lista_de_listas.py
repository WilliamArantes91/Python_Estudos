vendedores = ['Maria','João','Douglas','Antonio']
produtos = ['ipad','iphone']
vendas = [[100,200],
          [300,500],
          [50,1000],
          [900,10],
         ]

#Quanto João vendeu de Ipad?
vendas_ipad_joao = vendas[1][0] #300
print(vendas_ipad_joao)

#Quanto Douglas vendeu de Iphone
vendas_iphone_douglas = vendas[2][1] #1000
print(vendas_iphone_douglas)

#Qual o total de vendas de Iphone
vendas_total_iphone = vendas[0][1] + vendas[1][1] + vendas[2][1] + vendas[3][1]
print('O total de vendas de iphone foi de: {} '.format(vendas_total_iphone))

#E se Maria na verdade fez apenas 50 vendas de Iphone, como eu modifico na minha lista o valor de vendas dela?
vendas[0][1] = 50
print(vendas)

#E se agora eu tenho um novo produto 'mac', como eu adiciono as vendas em cada um dos vendedores?
vendas_mac = [10,15,6,70]
vendas[0].append(vendas_mac[0])
vendas[1].append(vendas_mac[1])
vendas[2].append(vendas_mac[2])
vendas[3].append(vendas_mac[3])

print(vendas)