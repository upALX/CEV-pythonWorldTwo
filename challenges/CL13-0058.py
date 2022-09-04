#Escreva um jogo da adivinhação, onde a máquina escolhe um número aleatório de 0 à 10 e o usuário tenta acertar o número
#O usuário deve permanecer com a possibilidade de chute até que acerte!

from random import randrange


machineChoice = randrange(0, 10)
true_value = 0
counter = 0

while true_value != 1:
    counter += 1
    userInput = int(input('Escreva um número de 0 à 10: '))
    if userInput == machineChoice:
        print('Parabéns! Você escolheu o mesmo númeor que a máquina: {}! Você precisou de apenas {} tentativas.'.format(machineChoice, counter))
        true_value = 1
    elif userInput > 10 or userInput < 0:
        print('Você está digitando um valor maior que 10 ou menor que 0! Digite um valor entre 0 e 10'.format(machineChoice))
    elif userInput.isnumeric() == True:
        print('Você digitou valores em caractere, só é aceito valores em númerico.')
    else:
        print('Algo de errado aconteceu!.')