#Programa que faz a média aritmética de um aluno e mostra junto com seu nome
print("Seja bem-vindo(a) professor(a)!")

aluno = input('Informe o nome do aluno: ')
nota1 = float(input('Informe a primeira nota do aluno: '))
nota2 = float(input('Informe a segunda nota do aluno: '))
nota3 = float(input('Informe a terceira nota do aluno: '))

media = (nota1 + nota2 + nota3) / 3

print(f'A média das notas do(a) aluno(a) {aluno} é {media}')
