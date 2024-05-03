import random
def jogar():

    print("********************************")
    print("Bem vindo ao jogo de advinhacao")
    print("********************************")

    numero_secreto = random.randrange(1,101)
    total = 0
    pontos = 1000

    print("escolha o nível de dificuldade entre 1, 2 ou 3")
    nivel = int(input("digite o nível: "))

    if (nivel==1):
        total=8
    elif(nivel==2):
        total=6
    elif(nivel==3):
        total=4
    else:
        print("você digitou um nível inválido")
        exit()

    for contador in range(1, total+1):
        print("Tentativa {} de {}".format(contador,total))

        chute_str = input("Digite seu número entre 1 e 100: ")
        chute = int(chute_str)


        if (chute < 1 or chute > 100):
            print("Esse é um número inválido")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if (acertou):
            print("você acertou")

            break
        else:
            if(maior):
                print("você errou, seu chute foi maior que o número secreto.")
                pontos_perdidos = abs((chute - numero_secreto)*7.3) #traz o absoluto
                pontos=pontos-pontos_perdidos
                print("você perdeu {} pontos".format(pontos_perdidos))
            elif(menor):
                print("você errou, seu chute foi menor que o número secreto.")
                pontos_perdidos = abs((chute - numero_secreto)*7.3) #traz o absoluto
                pontos = pontos - pontos_perdidos
                print("você perdeu ",pontos_perdidos," pontos")

        contador=contador+1

    print("Fim do jogo, o número secreto era: ", numero_secreto)
    print("Sua pontuação foi: ",pontos,"/1000")
if(__name__=="__main__"):
    jogar()