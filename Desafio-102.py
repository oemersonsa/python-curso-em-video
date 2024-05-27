'''Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''
from math import factorial


def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    print(f)


num = int(input('Digite um número: '))
mostrar = str(input('Deseja Mostrar o fatorial: [S/N] ')).strip().upper()[0]
while True:
    if mostrar in 'S':
        mostrar = True
    else:
        mostrar = False
        break
fatorial(num, mostrar)
