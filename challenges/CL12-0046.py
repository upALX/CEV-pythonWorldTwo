#Faça um programa que mostre na tela uma contagem regressiva, de 0 a 10, com uma pause de 1 segundo entre elas.

from time import sleep

for counter in range(10, -1, -1):
    print(counter)
    # sleep(1.6)