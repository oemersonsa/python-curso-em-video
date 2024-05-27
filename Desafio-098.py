"""Exercício Python 098: Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada"""
from time import sleep


def contador(a, b, c):
    if c < 0:
        c *= -1
    if c == 0:
        c = 1
    print('-=' * 20)
    print(f'Contagem de {a} a {b} de {c} em {c}.')
    sleep(1.5)

    if a <= b:
        cont = a
        while cont <= b:
            sleep(0.5)
            print(f'{cont}, ', end='', flush=True)
            cont += c
        print('FIM!')
    else:
        if a >= b:
            cont = a
            while cont >= b:
                sleep(0.5)
                print(f'{cont}, ', end='', flush=True)
                cont -= c
            print('FIM!')


# Programa Principal
contador(0, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é a sua vez de fazer a contagem personalizada.')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
