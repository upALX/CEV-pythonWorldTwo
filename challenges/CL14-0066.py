# Escreva um programa que leia valores e ao usuário digitar o número 999, o programa se mostrando quantos números o usuário digitou e a soma entre eles desconsiderando o 999.

counter = sum_input_numbers = 0

while True:
    number_sum = int(input('Informe um valor: '))
    if number_sum == 999:
        break
    sum_input_numbers += number_sum
    counter += 1

print(f'Você digitou {counter} valores e a soma entre eles é {sum_input_numbers}')
