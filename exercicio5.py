#Programa que faz seu IMC
print("Seja bem-vindo(a)!")

peso = float(input('Informe seu peso atual: '))
altura = float(input('Informe sua altura: '))

IMC = peso / altura ** 2

print(f'Seu IMC é {IMC}')