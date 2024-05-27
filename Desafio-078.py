'''Faça um programa que leia 5 valores númericos e guarde-os em uma lista.

No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista'''
menor = maior = c = 0
num = list()
for c in range (0, 5):
    num.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        menor = maior = num[c]
    else:
        if num[c] > maior:
            maior = num[c]
        if num[c] < menor:
            menor = num[c]
print(f'Você digitou os valores {num}')
print(f'Os maiores valores foram {maior} que estão nas posições: ', end='')
for i, v in enumerate(num):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'Os menores valores foram {menor} que estão nas posições: ', end='')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i}...', end='')
print()
