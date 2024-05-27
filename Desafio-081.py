'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''


numeros = []
while True:
    numeros.append(int(input('Digite um número: ')))
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break 
numeros.sort(reverse=True)
print(f'Foram digitados {len(numeros)} números')
print(f'A lista em ordem decrescente fica: {numeros}')
if 5 in numeros:
    print(f'O número 5 foi digitado e está na lista')
else:
    print('O número 5 não foi digitado!')


