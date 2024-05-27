'''Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar 999, que é a condição
de parada. No final mostre quantos números foram digitados e qual foi a
soma entre eles (desconsiderando a flag)'''

s = c = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    c += 1
    s += n
print(f'A soma dos {c} valores é {s}')