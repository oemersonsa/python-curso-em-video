''' Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
 Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''
from time import sleep


def maior(* valores):
    cont = m = 0
    print('-' * 30)
    print('Analisando os valores informados...')
    for valor in valores:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            m = valor
        else:
            if valor > m:
                m = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {m}.')


# Programa Principal
maior(1, 5, 6, 79, 15)
maior(79, 25, 36)
maior(8)
maior(0)
