'''Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário
tenatr descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu!'''
from random import randint
from time import sleep
print('_*_' * 10)
print('Adivinhe o número de 0 a 5!')
print('_*_' * 10)
num = randint(0, 5)
palpite = int(input('Digite seu palpite: '))
print('PROCESSANDO....')
sleep(3)
if palpite == num:
    print('Parabéns você acertou o número é {}!'.format(num))
else:
    print('Que pena você errou!')