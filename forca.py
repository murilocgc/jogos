import random

def jogar():
    quebra_linha()

    header()

    forca()

    palavra_secreta=recebe_palavra_s()

    enforcou = False
    acertou = False
    erros = 0
    lista = []

    for letra in palavra_secreta:
        lista.append("_")
    #ou poderia ser
    #lista = ["_" for palavra in palavra_secreta]

    print("Voce tem 7 chances!", "\n")
    print(' '.join(lista))

    while (not enforcou and not acertou):

        chute = recebe_chute()

        if (chute in palavra_secreta):

            acha_letra(palavra_secreta, chute, lista)

        else:
            print("\nVocê Errou a Letra!")
            erros += 1
            desenha_forca(erros)

        print("\nVocê ainda tem {} chances".format(7 - erros), "\n")
        print(' '.join(lista))

        enforcou = (erros == 7)


        acertou = (''.join(lista) == palavra_secreta)


    if (enforcou):
        enforca(palavra_secreta)

    elif(acertou):
        acerta()

def header():
    print("********************************")
    print("******Jogo da Forca!*******")
    print("********************************" + "\n")

def recebe_palavra_s():
    caminho = r"C:\Users\Useer\Desktop\Estudo\Python\jogos\palavras.txt"
    arquivo = open(caminho, "r")

    lista_palavras = []

    for linha in arquivo:
        linha = linha.strip().lower()
        lista_palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(lista_palavras))
    palavra_secreta = lista_palavras[numero]
    return palavra_secreta

def recebe_chute():
    chute = input("Digite uma letra: " + "\n")
    chute = chute.strip('.').lower()
    return chute

def acha_letra(palavra_secreta, chute, lista):
    index = 0
    for letter in palavra_secreta:
        if (chute == letter):
            lista[index] = letter
        index = index + 1

def enforca(palavra_secreta):
    print("\nPuxa, voce foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    print("A palavra secreta era: {}".format(palavra_secreta))


def acerta():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def forca():
    print("  _______     ")
    print(" |/      |    ")
    print(" |            ")
    print(" |            ")
    print(" |            ")
    print(" |            ")
    print(" |            ")
    print("_|___         ")
    print()

def quebra_linha():
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")

if (__name__ == "__main__"):
    jogar()
