'''Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. o programa vai perguntar o valor da casa,
o salário do comprador e em quantos anos ele vai pagar.

Caucule o valor da prestação mensal, sabendo que não pode exceder 30% do salário do comprador ou então o empréstimo será negado'''

print('\033[1;34m*' * 30)
print('\033[1;34mSimule aqui seu empréstimo!!!\033[m')
print('\033[1;34m*' * 30)
valor = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o valor do seu salário: R$'))
anos = int(input('Insira a quantidade de anos em que deseja pagar: '))
calc = salario * 30 / 100
prest = valor / (anos * 12)
if prest <= calc:
   print('\033[1;32mSeu empréstimo foi aprovado, o valor da sua prestação será de \033[m{:.2f}'.format(prest))
else:
    print('\033[1;31mInfelizmente seu empréstimo foi negado. Pois o valor da prestação de \033[m{:.2f} excede 30% do seu sálario!'.fomrat(prest))
print(prest)
