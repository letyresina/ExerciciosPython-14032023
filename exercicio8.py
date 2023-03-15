#Programa que calcula a comissão
print("Seja bem-vindo(a)!")

nome = input('Informe o nome do vendedor: ')

salario = 2500.00

carrosVendidos = int(input('Informe a quantidade de carros vendidos: '))

comissao = 200.00 * carrosVendidos

valorVendas = float(input('Informe o valor total das vendas: '))

porcentagem = valorVendas * 0.02

salarioFinal = salario + comissao + porcentagem 

print(f'O valor que {nome} receberá de salário é de {salarioFinal}')