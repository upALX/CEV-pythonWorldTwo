#Elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e condição de pagamentos:
# A vista ou cheque: 10% de desconto
# A vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: juros de 20%

normalValueProduct = float(input('Informe o valor do produto: '))
paymentCondiction = input('Informe a condição de pagamento: ').upper().strip()

conditionsToPayment = ['DEBIT', 'CREDIT-ONE','CREDIT-TWO', 'CREDIT']

if conditionsToPayment.index('DEBIT') == conditionsToPayment.index(paymentCondiction):
    tenPercentOff = (normalValueProduct * 10) / 100
    priceProductDebit = normalValueProduct - tenPercentOff
    print('Você vai comprar à vista, o preço com desconto fica de R$ {} por R$ {} reais!'.format(normalValueProduct, priceProductDebit))
elif conditionsToPayment.index('CREDIT-ONE') == conditionsToPayment.index(paymentCondiction):
    fiveOff = (normalValueProduct * 5) / 100
    priceProductCreditOne = normalValueProduct - fiveOff
    print('Você vai pagar no crédito, uma vez, o preço saí de R$ {} reais para R$ {} reais!'.format(normalValueProduct, priceProductCreditOne))
elif conditionsToPayment.index('CREDIT-TWO') == conditionsToPayment.index(paymentCondiction):
    print('O valor total da compra é igual a R$ {} reias!'.format(normalValueProduct))
elif conditionsToPayment.index('CREDIT') == conditionsToPayment.index(paymentCondiction):
    taxeCalc = (normalValueProduct * 20) / 100
    priceCredit = normalValueProduct + taxeCalc
    print('O valor total da compra é R$ {} reais!'.format(priceCredit))
else:
    print('Algo deu errado... Verifique os valores digitados!')
 