'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas ainda não 
atingiram a maioridade e quantas já são maiores.'''

from datetime import date 
maior = 0
menor = 0 
atual = date.today().year 
for c in range (1, 8):
    nasc = int(input('Digite o ano de nascimento da {}° pessoa: '.format(c)))
    idade = atual - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('Ao total temos {} pessoas maiores de idade'.format(maior))
print('E também {} pessoa menores idade'.format(menor))