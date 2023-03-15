#Programa que inverte de trás para frente um valor informado
print("Seja bem-vindo(a)!")

# Invertendo um número com a função [::-1]

numero = int(input('Informe um número inteiro com 3 dígitos: '))

numeroInvertido = int(str(numero)[::-1]) 

#Detalhe importante: a função str converte para String!

print(f'O valor do {numero} invertido é {numeroInvertido}')