'''Crie um programa onde o usuário possa digitar vários valores númericos
e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será
adicionado. No final, serão exibidos todos os valores únicos digitados,
em ordem crescente.'''

numeros = list()
while True:
    n = int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não irei adicionar...')
    s = ' '
    while s not in 'SN':
        s = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if s == 'N':
        break
print('-' * 10)
numeros.sort()
print(f'Os valores digitados foram {numeros}')