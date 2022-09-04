#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos da progressão.

fist_term = int(input('Informe o valor inteiro do termo: '))
reason_delta_t = int(input('Informe o valor da razão do termo: '))

for counter in range(1, 11):
    pa = fist_term + (counter - 1) * reason_delta_t
    print(pa)