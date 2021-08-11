import random as r

pontos_computador = 0
pontos_jogador = 0

print("------ Colors Choices Game -----")
print("Escolha a mesma cor que o computador para vencer o jogo\nBoa sorte!")

while True:
    # Declare colors choices as variables and specify colors of the game inside the nested while loop.
    print("\n1 - Vermelho\n2 - Laranja\n3 - Amarelo\n4 - Verde\n5 - Azul")
 
    # Cor escolhida pelo jogador
    escolha_jogador = int(input("Escolha uma cor: "))

    while escolha_jogador > 5 or escolha_jogador < 1:
        escolha_jogador = int(input("Escolha uma cor válida: "))
    
    if escolha_jogador == 1:
        cor_jogador = 'Vermelho'
    elif escolha_jogador == 2:
        cor_jogador = 'Laranja'
    elif escolha_jogador == 3:
        cor_jogador = 'Amarelo'
    elif escolha_jogador == 4:
        cor_jogador = 'Verde'
    elif escolha_jogador == 5:
        cor_jogador = 'Azul'
    
    print("\nVocê escolheu {}".format(cor_jogador))

    # Cor escolhida pelo computador
    escolha_computador = r.randint(1, 7)

    if escolha_computador == 1:
        cor_computador = 'Vermelho'
    elif escolha_computador == 2:
        cor_computador = 'Laranja'
    elif escolha_computador == 3:
        cor_computador = 'Amarelo'
    elif escolha_computador == 4:
        cor_computador = 'Verde'
    elif escolha_computador == 5:
        cor_computador = 'Azul'
    
    print("O computador escolheu {}\n".format(cor_computador))
 
    # Verificar quem ganhou a rodada
    if(cor_jogador == cor_computador):
        pontos_jogador += 1
    else:
        pontos_computador += 1

    # Exibir pontuação     
    print("Pontuação do jogador: {}".format(pontos_jogador))
    print("Pontuação do computador: {}".format(pontos_computador))

    # Avaliar fim do jogo
    print("\nVocê deseja jogar novamente? Escolha n ou N para terminar o jogo")
    resposta = input()   
    if resposta == 'N' or resposta == 'n':
        break

if pontos_computador == pontos_jogador:
    print("\n------- Empate! -------")

elif pontos_computador < pontos_jogador:
    print("\n------- Você venceu! -------")

elif pontos_computador > pontos_jogador:
    print("\n------- Você perdeu! -------")

print("Obrigado por jogar!")