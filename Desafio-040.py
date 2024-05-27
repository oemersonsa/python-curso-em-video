'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo
com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
if (nota1 + nota2) / 2 < 5:
    print('\033[31mALUNO REPROVADO!\033[m')
elif (nota1 + nota2) / 2 < 6.9 and (nota1 + nota2) / 2 > 5:
    print('ALUNO EM RECUPERAÇÂO!')
else:
    print('\033[34mALUNO APROVADO\033[m')