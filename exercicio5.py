# O código tem como função determinar se um número inteiro informado pelo usuário é par ou ímpar.

# Solicitando entrada do usuário
x = int(input("Digite um número: "))

# Verificando se o número é par ou ímpar
if x % 2 == 0:  # Usando o operador de módulo (%)
    print("Número Par!")
else:
    print("Número Ímpar!")