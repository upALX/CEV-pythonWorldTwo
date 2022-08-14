# Crie um programa que jogue pedra, papel, tesoura com você!

from platform import machine
from random import choice

valueUser = int(input(
    'Informe o que você escolhe para essa rodada | [PEDRA - 0, PAPEL - 1, TESOURA - 2] : '))
valuesGame = ['PEDRA', 'PAPEL', 'TESOURA']
machineChoice = choice(valuesGame)
userChoice = valuesGame[valueUser]

print(machineChoice)
print(userChoice)

if machineChoice == userChoice:
    valueUser = int(input(
        'Informe o que você escolhe para essa rodada | [PEDRA - 0, PAPEL - 1, TESOURA - 2] : '))
    valuesGame = ['PEDRA', 'PAPEL', 'TESOURA']
    machineChoice = choice(valuesGame)
    userChoice = valuesGame[valueUser]
else:
    if machineChoice == 'PEDRA' and userChoice == 'TESOURA':
        print('Eu escolhi {}. Você perdeu, e eu ganhei! Afinal pedra quebra tesoura!'.format(machineChoice))
    elif machineChoice == 'TESOURA' and userChoice == 'PEDRA':
        print('Eu escolhi {}. Você ganhou! Afinal pedra quebra tesoura!'.format(machineChoice))
    elif machineChoice == 'PAPEL' and userChoice == 'TESOURA':
        print('Eu escolhi {}. Você ganhou! Afinal tesoura corta papel!'.format(machineChoice))
    elif machineChoice == 'TESOURA' and userChoice == 'PAPEL':
        print('Eu escolhi {}. Eu ganhei, afinal tesoura corta papel!'.format(machineChoice))
    elif machineChoice == 'PAPEL' and userChoice == 'PEDRA':
        print('Eu escolhi {}. Eu ganhei, afinal papel enrola pedra!'.format(machineChoice))
    elif machineChoice == 'PEDRA' and userChoice == 'PAPEL':
        print('Eu escolhi {}. Eu perdi, afinal papel enrola pedra!'.format(machineChoice))
    else:
        print('Um erro ocorreu, entre em contato com o suporte!')