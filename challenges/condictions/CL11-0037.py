#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de converção:
#1: binário
#2: octal
#3: hexadecimal

numberToConvert = int(input('Informe um número para converção: '))
typeSelected = int(input('Informe o qual o tipo de conversão'))

if typeSelected != 1 and typeSelected != 2 and typeSelected != 3:
    print('Você digitou um número diferente de 1, 2 ou 3!')
elif typeSelected == 1:
    numberBinary = bin(numberToConvert)
    print('O número {} em binário é {}!'.format(numberToConvert, numberBinary)) 
elif typeSelected == 2:
    numberOctal == oct(numberToConvert)
    print('O número {} em octal é {0:}!'.format(numberToConvert, numberOctal)) 
elif typeSelected == 3:
    numberHexadecimal = hex(numberToConvert)
    print('O número {} em Hexadecimal é {0:e}!'.format(numberToConvert, numberHexadecimal))