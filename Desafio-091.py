'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado.'''

from random import randint 
from time import sleep
from operator import itemgetter
jogo = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}
ranking = list()
print('=' * 25)
print(f'{" Valores sorteados :":^25}')
print('=' * 25)
for k, v in jogo.items():
    sleep(1)
    print(f'{k} tirou {v} no dado.')
print('=' * 25)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    sleep(1)
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')
    print('-' * 25)
print(f'{" Fim ":-^25}')