#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a idade:
#Se ele ainda vai se alistar no exercito
#Se está no momento de se alistar
#Se já passou do tempo do alistamento

yearDate = int(input('Informe o seu ano de nascimento: '))

if yearDate == 18:
    print('Você deve se alistar!')
elif yearDate < 18:
    print('Você ainda não tem idade para se alistar! Faltam {} anos para o alistamento.'.format(18 - yearDate))
elif yearDate > 18:
    print('Você já deveria ter se alistado! Você está atrasado {} anos!'.format(yearDate - 18))