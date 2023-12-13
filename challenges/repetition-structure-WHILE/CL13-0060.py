# Escreva um programa que leia um valor e faça o fatorial desse valor.
#O fatorial (!) de um número n, representado por n!, é a multiplicação de n por seus antecessores maiores ou iguais a 1. 

from math import factorial


value_fatorial = int(input('Informe o valor para calcular o seu fatorial: '))

fatorial = 1 

for counter in range(1, value_fatorial + 1):
    fatorial *= counter
    print(fatorial)

# Criar modelos do SQL Alchemy para as tables
# Na models 1 arquivo para cada table

#Nem sempre o calculo matemático deve ser levado ao pé da letra em programação. Adapte.