# Some os valores que o usuário digitar, e se ele digitar 999, mostre a soma dos valores digitados sem contar o 999

while_value = True
list_numbers = []

while while_value:
    value_sum = int(input('Informe um valor [digite 999 para parar!]: '))
    list_numbers.append(value_sum)
    if value_sum == 999:
        result = sum(list_numbers) - 999
        print(f'Foram digitados {len(list_numbers)} numeros e a soma desses é igual a {result}!')
        while_value = False