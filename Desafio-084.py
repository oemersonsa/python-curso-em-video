'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

pessoas = list()
dados = list()
maisp = menosp = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maisp = menosp = dados[1]
    else:
        if dados[1] > maisp:
            maisp = dados[1]
        if dados[1] < menosp:
            menosp = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    cont = ' '
    while cont not in 'NS':
        cont = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break  
print('-' * 30)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O menor peso foi {menosp}KG. Peso de ', end='')
for p in pessoas:
    if p[1] == maisp:
        print(f'[{p[0]}]', end='')
print()
print(f'O maior peso foi {maisp}KG. Peso de ', end='')
for p in pessoas:
    if p[1] == menosp:
        print(f'[{p[0]}]', end='')
print()