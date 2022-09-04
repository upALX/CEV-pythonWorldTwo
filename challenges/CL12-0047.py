#Crie um programa que mostre todos os números pares de 1 à 50.
#Mostrando junto o número que não é par
for counter in range(1, 51):
    if counter % 2 == 0:
        print(counter)
    # else:
        # print('{} não é par!'.format(counter))
