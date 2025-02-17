# Este código determina o tipo de triângulo com base no comprimento dos três lados fornecidos pelo usuário. 

# Solicitando ao usuário os comprimentos dos três lados do triângulo

lado1 = float(input("Lado 1: "))
lado2 = float(input("Lado 2: "))
lado3 = float(input("Lado 3: "))

# Verificando se é um triângulo

if (lado1 > lado2 + lado3) or (lado2 > lado1 + lado3) or (lado3 > lado1 + lado2):
    print("Não é um triângulo!")
else:
    if lado1 == lado2 == lado3:
        print("Equilátero!")
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print("Isósceles!")
    else:
        print("Escaleno!")
