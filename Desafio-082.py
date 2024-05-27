'''Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, 
respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''

lista = list()
pares = list()
impares = list()
while True:
    lista.append(int(input('Digite um número: ')))
    cont = ' '
    while cont not in "SN":
        cont = str(input('Dejesa continuar: [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'A lista geral é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')