'''faça um programa que jogue par ou ímpar com o computador. O jogo só sera interrompido quando o
jogador perder, mostrando o total de vitorios do jogador'''

from random import randint 

v = 0
print('=*=' * 15)
print('----- VAMOS JOGAR PAR OU ÍMPAR -----')
print('=*=' * 15)
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador 
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o Computador jogou {computador}, o total foi {total}', end=' ')
    print('DEU PAR!' if total % 2 == 0 else 'DEU ÍMPAR!')
    if tipo == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            break
    elif tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER... Você veceu {v} vezes!')    

