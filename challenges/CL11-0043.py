#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela:
#abaixo de 18.5: abaixo do peso
#entre 18.5 e 25: peso ideal
#25 até 30: sobrepeso
#30 até 40: obesidade
#acima de 40: obesidade mórbida

weigth = float(input('Informe o seu peso: '))
height = float(input('informe a sua altura: '))
imc = weigth / (height**2)

if imc < 18.5:
    print('Vocẽ está abaixo do peso, ganhe peso! Seu IMC é de {:.2f}'.format(imc))
elif imc < 26:
    print('Você está com o peso normal, mantenha! Seu IMC é de {:.2f}.'.format(imc))
elif imc < 31:
    print('Você está com sobrepeso, cuidado! Seu IMC é de {:.2f}'.format(imc))
elif imc < 41:
    print('Você está com obesidade mórbida, perca peso imediatamente! Seu IMC é de {:.2f},'.format(imc))
else:
    print('Ocorreu um erro, você deve informar números na digitação, caracteres não são contados!')