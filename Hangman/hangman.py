# Importação dos módulos
import random
from hangman_guessing import lista_palavras
from hangman_life import nome_jogo
from hangman_life import vidas

# Inicialização de variáveis
palavra_secreta = random.choice(lista_palavras).lower()
qtd_letras = len(palavra_secreta)
fim_de_jogo = False
tentativas = 6

# Mostra nome do jogo
print(nome_jogo)

# Lista vazia onde serão adicionadas as letras certas
chutes = []
for _ in range(qtd_letras):
    chutes += "_"

while not fim_de_jogo:
    palpite_jogador = input("Chute uma letra: ")

    # Jogador chuta uma letra que já foi adivinhada
    if palpite_jogador in chutes:
        print("A letra já foi adivinhada: {}.".format(palpite_jogador))

    # Checar se a letra chutada está certa ou errada
    for indice in range(qtd_letras):
        letra = palavra_secreta[indice]
        
        if palpite_jogador == letra:
            chutes[indice] = letra

    # Check if the players guess the wrong letter they will lose a try.
    if palpite_jogador not in palavra_secreta:
        #If the letter is not in the guessed_word, print out the letter and let them know it's not in the word.
        print("Você chutou \"{:s}\" errado e perdeu uma tentativa.".format(palpite_jogador))
        
        # Verifica se há tentativas restantes  
        tentativas -= 1
        if tentativas == 0:
            fim_de_jogo = True
            print("Game Over. Você Perdeu.")

    # Mostra a string de chutes
    print(' '.join(chutes))

    # Verifica se o jogador já acertou todas as letras
    if "_" not in chutes:
        fim_de_jogo = True
        print("Você venceu, parabéns!")

    # Imprime o desenho da forca
    print(vidas[tentativas])