import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("*********************************")


    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    rodada = 1
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1)Fácil  (2)Médio  (3)Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    while(rodada <= total_de_tentativas):
        print("Tentativa {} de {}" .format(rodada, total_de_tentativas))
        chute_str = input("Digite o seu número entre 1 e 100: ")
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            rodada = rodada + 1
            continue

        acertou = chute == numero_secreto;
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("Você errou, digitou um número maior!")
            elif(menor):
                print("Você errou, digitou um número menor!")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos
        rodada = rodada + 1

    print("FIM DO JOGO!")

if(__name__ == "__main__"):
    jogar()
