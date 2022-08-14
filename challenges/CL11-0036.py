#Escreva um programa que aprove um emprestimo bancário para compra de casas. 
#Receba o valor da casa, o salario do comprador e os anos de quitação.
#Para o calculo da prestação mensal, o valor não pode ser maior que 30% do salário do comprador.

houseValue = float(input('Informe o preço da casa: '))
montlyIncome = float(input('Informe a sua receita mensal: '))
paymentTime = int(input('Informe em meses, o tempo para pagamento total: '))

approvedLoan = houseValue / paymentTime <= (montlyIncome * 30) / 100

if(approvedLoan):
    print('Você pode comprar esse imóvel dentro do tempo estipulado!')
else:
    print('Você não foi aprovado!')