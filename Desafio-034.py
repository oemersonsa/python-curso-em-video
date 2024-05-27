'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para saários de até R%1250,00 calcule um aumento de 10%
Para os inferiores ou igual calcule um aumento de 15%'''

sal = float(input('Digite o salário do funcionário: R$'))
if sal > 1250.00:
    print('O valor do novo salário é de R${:.2f}'.format(sal + (sal * 10 / 100)))
else:
    print('O valor do novo salário é de R${:.2f}'.format(sal + (sal * 15 / 100)))