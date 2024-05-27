'''Cria um programa qua faça o computador jogar JOKENPO com você.'''

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
#Jogada do computador
computador = randint(0, 2) 
#Jogada do jogador
print('''\033[1;35mSuas opções:
[0] PEDRA 
[1] PAPEL 
[2] TESOURA \033[m''') 
jogador = int(input('\033[1;31mDigite a sua escolha:\033[m ')) 
#JO KEN PO
print('\033[1;33mJO')
sleep(1)
print('\033[1;33mKEN')
sleep(1)
print('\033[1;33mPÔ...')
sleep(2)
print('\033[1;33m-=-' * 20)
#Resultado
print('Computador Jogou {}'.format(itens[computador]))
print('Você jogou {}'.format(itens[jogador]))
print('\033[1;33m-=-\033[m' * 20)
# 0 = pedra, 1 = papel, 2 = tesoura
if computador == 0: #Computador jogou pedra
    if jogador == 0:
        print('\033[1;33mEMPATE!\033[m')
    elif jogador == 1:
        print('\033[1;32mVOCÊ VENCEU!\033[m')
    elif jogador == 2:
        print('\033[1;31mVOCÊ PERDEU A VITÓRIA É DO COMPUTADOR!\033[m')
    else: 
        print('JOGADA ÍNVALIDA!!!')
if computador == 1: #Computador jogou papel
    if jogador == 2:
        print('\033[1;32mVOCÊ VENCEU!\033[m')
    elif jogador == 1:
        print('\033[1;33mEMPATE!\033[m')
    elif jogador == 0:
        print('\033[1;31mVOCÊ PERDEU A VITÓRIA É DO COMPUTADOR!\033[m')
    else: 
        print('JOGADA ÍNVALIDA!!!')
if computador == 2: #Computador jogou tesoura
    if jogador == 1:
        print('\033[1;31mVOCÊ PERDEU A VITÓRIA É DO COMPUTADOR!\033[m')
    elif jogador == 0:
        print('\033[1;32mVOCÊ VENCEU!\033[m')
    elif jogador == 2:
        print('\033[1;33mEMPATE!\033[m')    
    else:
        print('JOGADA ÍNVALIDA!!!')