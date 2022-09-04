# Faça uma PA que mostre os 10 primeiros termos

term = int(input('Informe o valor do primeiro termo da PA: '))
reason_pa =  int(input('Informe o valor da razão da PA: '))
counter = 1 

# while counter <= 10:
#     if counter == 1:
#         print(term)
#     else:
#         term += reason_pa
#         print(term)

while counter < 11:
    print(term)
    term += reason_pa
    counter += 1

# for counter in range(1, 10 + 1):
#     if counter == 1:
#         print(term)
#     else:
#         term += reason_pa
#         print(term)