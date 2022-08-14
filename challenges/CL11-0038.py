#Escreva um programa que leia dois valores inteiros e compareos, mostrando na tela as mensagems:
#O primeiro número é maior
#O segundo número é maior
#Não existe valor maior, ambos são iguais!

from curses.ascii import isdigit


firstValue = int(input('Informe o primeiro valor: '))
secondValue = int(input('Informe o segundo valor: '))

if firstValue < 0 or secondValue < 0:
    print('Um dos valores é negativo!')
elif firstValue == secondValue:
    print('Ambos os valores são iguais!')
elif firstValue > secondValue:
    print('O primeiro valor é maior!')
elif secondValue > firstValue:
    print('O segundo valor é maior!')
else: 
    print('Um dos valores é igual a zero, tente novamente somente com valores positivos!')