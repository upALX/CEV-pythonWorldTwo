# Mostre uma PA, capturando o primeiro termo e a razão do usuário. Esse PA deve ser mostrada primeiramente nos seus 10 primeiros termos, e depois deve ser perguntado quantos termos mais o usuário deseja que mostre

term = int(input('Informe o valor do primeiro termo da PA: '))
reason_pa =  int(input('Informe o valor da razão da PA: '))
number_of_terms = int(input('Digite a quantidade de termos que você deseja dessa PA: '))
counter = 0
while_value = True 

while counter < number_of_terms:
    print(f'{term}', end=' ')
    term += reason_pa
    counter += 1

while while_value:
    number_more_terms = int(input('\nDigite quantos termos a mais você deseja vizualizar: '))
    if number_more_terms != 0:
        while counter < number_of_terms + number_more_terms:
            term += reason_pa
            print(f'{term}', end=' ')
            counter += 1
    else:
        print(f'A PA terminou com {counter} termos!')
        while_value = False
