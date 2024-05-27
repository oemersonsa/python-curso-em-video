#faça um programa que leia uma frase e mostre:
#quantas vezes aparece a letra 'a'
#em que posição ela aparece pela primeira vez
# #em qual ela aperece a última vez
frase = str(input('Digite sua frase: ')).strip().lower()
print('A letra A aparece {} vezes na frase.'.format(frase.count('a')))
print('A primeira letra A aparce na posição {}.'.format(frase.find('a')+1))
print('A última letra A aparece na posição {}.'.format(frase.rfind('a')+1))