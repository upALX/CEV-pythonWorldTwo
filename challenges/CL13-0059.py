# Escreva um programa que leia dois valores e pergunte qual tipo de operação matemática básica ele deseja realizar com os dois numeros
list_numbers = []

true_while = 1

while true_while == 1:
    for counter in range(2):
        number_calculate = int(input('Digite um número: '))
        list_numbers.append(number_calculate)
        counter += 1
    
    if counter == 2:
        choice_operation = int(input('''Qual operação você deseja fazer: 
        1 - Soma 
        2 - Multiplicação 
        3 - Maior valor 
        4 - Selecionar novos valores 
        5 - Finalizar programa '''))
        if choice_operation == 1:
            print(f'A soma dos valores é: {sum(list_numbers)}')
        elif choice_operation == 2:
            print(f'{list_numbers[0] * list_numbers[1]}')
            true_while = 0
        elif choice_operation == 3:
            print(f'O maior valor entre eles é {max(list_numbers)}')
        elif choice_operation == 4:
            true_while = 1
        elif choice_operation == 5:
            true_while = 0