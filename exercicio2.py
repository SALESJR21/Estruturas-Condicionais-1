# Cálculo de velocidade e pontuação na carteira

# Definindo as velocidades de referência para infrações

velocidade_leve = 50 * 1.1
velocidade_media = 70
velocidade_grave = 90
velocidade_gravissima = 110

# Solicitando ao usuário que informe a velocidade registrada do veículo

velocidade_veiculo = float(input("Informe a velocidade que o veículo passou: "))

# Verificando a classificação da infração e exibindo a penalidade correspondente

if velocidade_veiculo <= velocidade_leve:
    print("Isento")
elif velocidade_veiculo <= velocidade_media:
    print("3 pontos na carteira")
elif velocidade_veiculo <= velocidade_grave:
    print("4 pontos na carteira")
elif velocidade_veiculo <= velocidade_gravissima:
    print("5 pontos na carteira")
else:
    print("7 pontos na carteira")