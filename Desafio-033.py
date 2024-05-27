'''Faça um programa que leia 3 números e diga qual é o maior é qual é o menor.'''

n1 = int(input('Digigte um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
print('Analisando os 3 números: ')
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
menor = n2
if n1 < n2 and n2 < n3:
    menor = n1
if n3 < n1 and n3 < n2:
    menor = n3
print('O maior número é {}.'.format(maior))
print('O menor número é {}.'.format(menor))