'''Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio. indo de 
10 até 0, com uma pausa de 1 segundo entre eles.'''

from time import sleep
import emoji
print('\033[34m-=-\033[m' * 20)
print('\033[1;34mContagem regressiva paras os fogos...\033[m')
print('\033[34m-=-\033[m' * 20)
f = 0 
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('POW', emoji.emojize(":fireworks:" * 5), 'POW') 