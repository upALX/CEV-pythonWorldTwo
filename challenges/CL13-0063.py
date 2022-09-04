# Crie um programa que mostre termos da sequência de Fibonacci. A quantidade de termos deve ser informada pelo usuário.and

number_terms = int(input('Informe o número de termos que você deseja da Sequência de Fibonacci: ')) 
counter = 1
f1 = 1
f2 = 1
fibonacci = 0

while counter < number_terms:
    fibonacci += f1 + f2
    print(fibonacci)
    counter += 1 

# Fazer