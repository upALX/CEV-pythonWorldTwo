# Faça um programa que o usuário digite números quantas vez quiser, e a cada numero digitado o programa pergunta se ele deseja continuar digitando. 
# Quando o usuário não quiser mais digitar números, deve ser devolvido para ele a quantidade de números digitados, o maior valor digitado, o menor valor digitado e a média desses valores.

from operator import indexOf


value_while = True
list_numbers = []

while value_while:
    user_values = input('Digite um número: ')
    if user_values.isdigit():
        list_numbers.append(int(user_values))
        continue_user = input('Deseja continuar informando valores: ').upper()

        if continue_user == 'Y':
            value_while
        else:
            value_while = False

# print(f'Foram digitados {len(list_numbers)} números. O maior valor digitado foi {max(list_numbers)}. \n O menor valor digitado foi {min(list_numbers)}. A média desses valores é de {sum(list_numbers) / len(list_numbers)}.')


for number in list_numbers:
    index = list_numbers.index(number)
    min_value = list_numbers[index] < list_numbers[index + 1]
    
print(min_value)