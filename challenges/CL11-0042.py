#Receba três valores e mostre se esses podem ser um triângulo, assim como diga qual o tipo de triângulo eles pode formar
# Equilatero: todos os lados iguais 
# Dois lados iguais
# Todos os lados diferetens
#|10 – 9| < 5 < 10 + 9 and 1 < 5 <19 (VERDADEIRO)

valueOneTriangule = int(input('Informe um valor inteiro: '))
valueTwoTriangule = int(input('Informe um valor inteiro: '))
valueThreeTriangule = int(input('Informe um valor inteiro: '))

if valueOneTriangule > valueTwoTriangule - valueThreeTriangule and valueTwoTriangule > valueOneTriangule - valueThreeTriangule and valueThreeTriangule > valueTwoTriangule - valueOneTriangule: 
    if valueOneTriangule == valueTwoTriangule and valueOneTriangule == valueThreeTriangule and valueTwoTriangule == valueThreeTriangule:
        print('É uma triangulo Equilatero!')
    elif valueOneTriangule == valueTwoTriangule or valueTwoTriangule == valueThreeTriangule or valueOneTriangule == valueThreeTriangule:
        print('É um triângulo Isóceles!')
    else: 
        print('É um triângulo Escaleno!')
else:
    print('Esses valores não podem formar um triângulo!')
