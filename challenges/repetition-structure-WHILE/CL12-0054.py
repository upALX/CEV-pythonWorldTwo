#Escreva um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade
#e quantas já são maiores.

from datetime import datetime

datetime_today = datetime.now()
sumYounger = 0
sumAdult = 0
array_dates = []
for counter in range(1,8):
    name_one = int(input('Informe o ano de nascimento da {} pessoa: '.format(counter)))
    array_dates.append(name_one)

for date in range(len(array_dates)):
    if array_dates[date] + 18 <= datetime_today.year:
        sumAdult += 1
    else:
        sumYounger += 1

print('{} pessoas são menores de idade!'.format(sumYounger))
print('{} pessoas são maiores de idade!'.format(sumAdult))
