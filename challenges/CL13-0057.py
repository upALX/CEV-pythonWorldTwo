#Escreva um programa que leia um valor e informe se ele é masculino ou feminino, se o valor fugir da regra, deve ser pedido
#novamente para que o usuário informe um valor

value_condition = 1

while value_condition == 1:
    value_gender = input('Informe o genero com M para masculino e F para feminino: ').upper().strip()
    if value_gender == 'M':
        value_condition = 0
        print('Você selecionou o gênero Masculino!')
    elif value_gender == 'F':
        value_condition = 0
        print('Você escolheu o gênero Feminino!')
    else:
        print('Você está informando valores diferentes de M ou F, verifique os valores digitados e tente novamente!')