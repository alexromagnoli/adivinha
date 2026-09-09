import random

print ("Jogo de Adivinhação")
print ("Tente adivinhar o número que estou pensando entre 1 e 100")
print ("Você tem 7 tentativas para acertar o número secreto.")

numero_secreto = random.randint(1, 100)
tentativa = 0
max_tentativas = 7



while tentativa < max_tentativas:
    palpite = int(input("Digite o seu palpite: "))
    if palpite < 1 or palpite > 100:
        print("Por favor, digite um número entre 1 e 100.")
        continue

    tentativa += 1
    print("Tentativa", tentativa, "de", max_tentativas)

    if palpite < numero_secreto:
        print("O número secreto é maior que", palpite)
    elif palpite > numero_secreto:
        print("O número secreto é menor que", palpite)
    else:
        print("Parabéns! Você acertou o número secreto:", numero_secreto)
        break

if tentativa == max_tentativas and palpite != numero_secreto:
    print("Suas tentativas acabaram. O número secreto era:", numero_secreto)
