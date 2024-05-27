'''Faça um programa que leia um ano qualquer e diga se ele é bissexto.'''

from calendar import isleap
from datetime import date
ano = int(input('Digite um ano e descubra se ele é ou não BISSEXTO: '))
if ano == 0:
    ano = date.today().year
'''if ano % 4 == 0 and ano % 100 != 0 or 400 == 0:
    print('Sim o ano de {} é BISSEXTO!'.format(ano))
else:
    print('Não o ano de {} não é BISSEXTO!'.format(ano))'''
if isleap(ano):
    print('Sim o ano de {} é BISSEXTO!'.format(ano))
else:
    print('Não o ano de {} não é BISSEXTO!'.format(ano))