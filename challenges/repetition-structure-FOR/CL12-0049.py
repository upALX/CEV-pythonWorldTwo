#Crie uma tabuada até 10 de qualquer número

numberTable = int(input('Informe a tabuada que você deseja através do número: '))

for counter in range(0, 11):
    tableResult = counter * numberTable
    print('{} X {} é igual a {}!'.format(counter, numberTable, tableResult))