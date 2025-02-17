# Calculo de a média do aluno

# Solicitando as notas ao usuário

nota1 = float(input("Informe a nota 1: "))
nota2 = float(input("Informe a nota 2: "))
nota3 = float(input("Informe a nota 3: "))

# Calculo da média

media = (nota1 + nota2 + nota3) / 3

# Verificar a média e imprimir o resultado para o(a) usuário(a)

if media >= 7:
    print("Você foi aprovado(a) com a média: ", media)
elif media < 5:
    print("Você foi reprovado(a) com a média ", media)
else:
    print("Sua média foi ", media, "e você está de recuperação!")

