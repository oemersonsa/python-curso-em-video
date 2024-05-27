'''Melhore o jogo do desasfio 028 onde o computador vai "pensar" em um número de 0 a 10.
Só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites 
foram nescessários para vencer'''

from random import randint
from time import sleep
print('\033[1m_*_\033[m' * 10)
print('\033[1mAdivinhe o número de 0 a 10!\033[m')
print('\033[m_*_\033[m' * 10)
computador = randint(0, 10)
acertou = False
palpite = 0 
while not acertou:
    jogador = int(input('\033[1mDigite seu palpite:\033[m '))
    palpite += 1
    print('\033[1;33mPROCESSANDO....\033[m')
    sleep(1)
    if jogador == computador:
        acertou = True 
    else:
        if jogador < computador:
            print('\033[1;31mMais... Tente outra vez!\033[m')
        else:
            print('\033[1;31mMenos... Tente outra vez!\033[m')
print('\033[1;32mAcertou com \033[4m{} tentativas\033[m, \033[1;32mParabéns!\033m'.format(palpite))
