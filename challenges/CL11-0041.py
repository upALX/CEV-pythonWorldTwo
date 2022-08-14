#Um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade. 9 mirim, 14 infantil, 19 sênior, 20 pra cima: master.

ageSwimmer = int(input('Informe a sua idade: '))

if ageSwimmer >= 9 and ageSwimmer < 14:
    print('Você está na categoria mirim!')
elif ageSwimmer >= 14 and ageSwimmer < 19:
    print('Você está na categoria infantil!')
elif ageSwimmer == 19:
    print('Você está na categoria sênior, parabéns!')
else:
    print('Incrivel, você é um MASTER!')