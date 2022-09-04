# Crie um programa que leia leia um número inteiro e diga se ele é ou nõa um número primo!

inter_number = int(input('Informe um número inteiro: '))

for counter in range(2):
    if inter_number % inter_number == 0 and inter_number % 1 == 0:
        print('O número {} é um número primo!'.format(inter_number))
    else:
        print('O número {} não é um número primo!'.format(inter_number))
