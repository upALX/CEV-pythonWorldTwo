#Escreva um programa que leia o peso de 5 pessoas e mostre o maior e o menor peso!

max_weight = 0 
min_weight = 0

list_weight = []
for people in range(1,6):
    weight = float(input('Informe o peso da pessoa {}: '.format(people)))
    list_weight.append(weight)

for weight in range(len(list_weight)):
    if weight == 1:
        max_weight = list_weight[weight]
        min_weight = list_weight[weight]
    elif max_weight > min_weight:
        max_weight == max_weight
    else:
        print('{} é um peso normal.'.format(list_weight[weight]))