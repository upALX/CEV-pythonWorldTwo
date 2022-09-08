#Escreva um programa que mostre tabuadas tendo como base da tabuada o valor digitado pelo usuário, o programa deve mostrar uma tabuada por vez e quando o usuário digitar um valor negativo ele deve se encerrar mostrando que o programa foi encerrado.

table_result = 0

while True:
    table_base = int(input('Informe o valor base da tabuada: ')) 
    if table_base < 0:
        print('A tabuada foi encerrada!') 
        break
    else:
        for counter in range(0, 11):
            table_result = table_base * counter
            print(f'{counter} x {table_base} == {table_result}')