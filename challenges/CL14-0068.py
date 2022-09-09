#Crie um programa de PAR ou Ímpar e jogue contra a máquina. O usuário deve informar o valor e se ele quer PAR ou IMPAR. enquanto o usuário estiver ganhando o programa deve continuar.
from random import randint


while True:
    value_game = input('Diga o valor que você quer?')
    value_decision = input('Informe se você quer par ou impar: [P ou I]').upper()
    value_game_machine = randint(0, 11)
    sum_values = int(value_game) + value_game_machine
    if int(value_game) < 0:
        print('Por favor, informe um valor válido igual ou maior que 0!')
    elif value_decision.isdigit():
        print('Por favor, informe um valor em caractere!')
    elif value_decision == 'P':
        print('Você escolheu par!')
        if (int(value_game) + value_game_machine) % 2 == 0:
            print(f'Você venceu! A maquina escolheu {value_game_machine}. O total de {sum_values} é par!')
        else:
            print(f'Você perdeu! A maquina escolheu {value_game_machine}. O total de {sum_values} é ímpar!')
            break
    elif value_decision == 'I':
        print('Você escolheu ímpar!')
        if (int(value_game) + value_game_machine) % 2 != 0:
            print(f'Você venceu! A maquina escolheu {value_game_machine}. O total de {sum_values} é ímpar!')
        else:
            print(f'Você perdeu! A maquina escolheu {value_game_machine}. O total de {sum_values} é par!')
            break
    else:
        print('Você informou um valor diferente de números e letras!')
        