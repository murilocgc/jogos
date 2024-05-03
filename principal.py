import forca
import adivinhacao

print("********************************")
print("******Escolha o seu jogo!*******")
print("********************************")

print("(1) Forca e (2) Adivinhação")

jogo = int(input("Digite o número do jogo: "))

if (jogo == 1):
    print("Iniciando Forca...")
    forca.jogar()
elif (jogo == 2):
    print("Iniciando adivinhacao...")
    adivinhacao.jogar()
