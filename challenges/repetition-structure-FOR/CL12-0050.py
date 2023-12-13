#Escreva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o!

numberOne = int(input('Informe um valor: '))
numberTwo = int(input('Informe um valor: '))
numberThree = int(input('Informe um valor: '))
numberFour = int(input('Informe um valor: '))
numberFive = int(input('Informe um valor: '))
numberSix = int(input('Informe um valor: '))

arrayOfNumbers = [numberOne, numberTwo, numberThree, numberFour, numberFive, numberSix]

for counter in arrayOfNumbers:
    sumNumbers = 0
    if counter % 2 == 0: 
        sumNumbers += counter
        print('{} mais {} é igual a {}!'.format(counter, sumNumbers, sumNumbers))
    else:
        print('{} é impar!'.format(counter))
