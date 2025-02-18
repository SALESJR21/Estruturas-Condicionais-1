# Reserva de Assento-Poltrona no Cinema

# Inicialização da matriz de assentos do cinema (10x10)
cinema = [["O" for _ in range(10)] for _ in range(10)]  # Todas as poltronas são inicialmente marcadas como "O" (livres)

while True:
    print("1 - Reservar Poltrona")
    print("2 - Layout do Cinema")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        # Reservar uma poltrona
        try:
            fila = int(input("Fila (1-10): "))
            poltrona = int(input("Poltrona (1-10): "))

            if 1 <= fila <= 10 and 1 <= poltrona <= 10:
                if cinema[fila - 1][poltrona - 1] == "O":  # Verifica se a poltrona está livre
                    cinema[fila - 1][poltrona - 1] = "X"  # Marca a poltrona como reservada ("X")
                    print("Poltrona reservada com sucesso!")
                else:
                    print("Poltrona já ocupada!")
            else:
                print("Fila ou poltrona fora do intervalo! Escolha entre 1 e 10.")
        except ValueError:
            print("Entrada inválida! Digite números inteiros para fila e poltrona.")

    elif opcao == "2":
        # Mostrar o layout do cinema
        print("Layout do Cinema:")
        for linha in cinema:
            print(" ".join(linha))  # Exibe o estado atual das poltronas

    elif opcao == "3":
        # Sair do programa
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida! Tente novamente.")