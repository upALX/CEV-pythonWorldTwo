# Escreva um programa que leia idade e sexo de varias pessoas. A cada pessoa cadastrada, o programa, deverá perguntar se o usuário quer ou não continuar. No final deve mostrar
# quantas pessoas são maiores de 18
# quantos homens foram cadastrados
# Quantas mulheres tem menos de 20 anos
counter_male = 0
counter_minor_twenty = 0
counter_bigger_eighteen = 0

while True:
    value_age = int(input('Digite sua idade: '))
    value_gender = input('Informe seu gênero: ').upper()
    if value_gender == 'M':
        counter_male += 1 
    elif value_gender == 'F':
        if value_age < 20:
            counter_minor_twenty += 1    
    else:
        print('Valor informado diferente de F ou M')

    if value_age >= 18:
        counter_bigger_eighteen += 1

    continue_user = input('Deseja continuar? ').upper()
    if continue_user == 'N':
        print(f'Foram cadastrados {counter_male} pessoas do gênero masculino!')
        print(f'Foram encontradas {counter_minor_twenty} mulheres menores de 20 anos!')
        print(f'Foram encontradas {counter_bigger_eighteen} pessoas acima de 18 anos!')
        break
