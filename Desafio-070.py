'''Crie um programa que leia o nome e preço de vários produtos. O programa deve perguntar se o usuário vai
continuar. No final, mostre:
A- Qual é o total gasto na compra
B- Quantos produtos custam mais de R$1000
C- Qual é o nome do produto mais barato'''

maisdemil = maisbarato = total = contador = 0
nomemaisbarato = ''
print('{:=^35}'.format(' MERCADÃO '))
while True: 
    nome = str(input('Digite o nome do produto: ')).strip()
    preco = float(input('Insira o valor do produto: R$'))
    total += preco
    contador += 1
    if preco >= 1000:
        maisdemil += 1
    if contador == 1 or preco < maisbarato:
        maisbarato = preco 
        nomemaisbarato = nome
    cont = ' '
    print('-' * 30 )
    while cont not in 'SN':
        cont = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
        print('-' * 30 )
    if cont == 'N':
        break    
print('{:=^35}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi {total:.2f}')
print(f'Temos {maisdemil} produtos que custaram mais de R$1000.00')
print(f'O produto mais barato foi {nomemaisbarato} que custou {maisbarato:.2f}')
print('=' * 35)