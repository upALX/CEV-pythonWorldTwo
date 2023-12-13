#Faça um programa que calcule a soma de todos os números impares que são multiplos de três e que se encontram no intervalo de 1 até 500

for counter in range(1,501):
    calcSum = 0
    if counter % 3 == 0 and counter % 2 != 0:
        calcSum += counter
        print('{} é ímpar e divisivel por 3!'.format(calcSum))
    else:
        print('{} é par ou não é divisivel por 3!!'.format(counter))