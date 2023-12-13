#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida!

firstSemestry = float(input('Informe a nota do primeiro semestre: '))
secondSemestry = float(input('Informe a nota do primeiro semestre: '))

listNotes = [firstSemestry, secondSemestry]

avarege = sum(listNotes) / len(listNotes)

if avarege < 5:
    print('Sua média está a baixo de 5. Reprovado!')
elif avarege >= 5 and avarege < 7:
    print('Está de recuperação!')
else:
    print('Você passou!')