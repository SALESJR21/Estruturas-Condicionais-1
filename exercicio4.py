# Verificando se a entrada de dados é de uma pessoa maior ou menor de idade

# Solicitar e validar o nome do usuário
while True:
    nome = input("Qual o seu nome? ")
    if nome.isalpha():  # Verificar se contém apenas letras
       break  # Sai do loop se a entrada for válida
    else:
        print("O nome deve conter apenas letras. Por favor, digite novamente.")

# Solicitar a idade do usuário

idade = float(input(f"{nome}, digite sua idade: "))

# Verificando a idade

if idade >= 18:
    print(f"Você é maior de idade, {nome}!")
else:
    print(f"Você é menor de idade, {nome}!")
