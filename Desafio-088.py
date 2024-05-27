'''Faça um programa que ajude um jogador da mega sena a criar palpites. 
O programa vai perguntar quanots jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
cadastrando tudo em uma lista composta'''

from random import randint
from time import sleep
mega = list()
jogos = list()
print('-' * 40)
print(f'{" BOLÃO MEGA SENA ":-^40}')
print('-' * 40)
quant = int(input('Quantos jogos você quer sortear: '))
tot = 1
while tot <= quant:
    cont = 0 
    while True:
        num = randint(1, 60)
        if num not in mega:
            mega.append(num)
            cont += 1
        if cont >= 6:
            break 
    mega.sort()
    jogos.append(mega[:])
    mega.clear()
    tot += 1
print(f'----- SORTEANDO {quant} JOGOS ------')
for i, l in enumerate(jogos):
    sleep(1)
    print(f'Jogo {i+1}: {l}')
print(f'{" BOA SORTE ":-^40}')

