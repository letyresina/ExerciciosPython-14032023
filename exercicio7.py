#Programa que calcula o desconto
print("Seja bem-vindo(a)!")

valorProduto = float(input('Informe o valor do produto que deseja aplicar o desconto: '))
desconto = valorProduto * 0.1
valorFinal = valorProduto - desconto

print(f'O valor R${valorProduto} tem desconto de {desconto} dando no total {valorFinal}')