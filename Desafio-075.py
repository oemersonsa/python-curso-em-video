'''Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9
B) Em que posição foi digitado o primeiro valor 3
C) Quais foram os números pares'''

n = ((int(input('Digite um número: '))), (int(input('Digite outro número: '))),
    (int(input('Digite mais um número: '))), (int(input('Digite o úlitmo número: '))))
print(f'Você digitou os valores {n}')
if 9 in n:
    print(f'O número 9 apareceu {n.count(9)} vezes')
else:
    print('O número 9 não aparceu nenhuma vez!')
if 3 in n:
    print(f'O número 3 foi digitado primeiro na posição {n.index(3) + 1}')
else:
    print('O número 3 não foi digitado nenhuma vez')
print(f'Os números pares são: ', end='')
for c in n:
    if c % 2 == 0:
        print(f'{c} ', end='')
