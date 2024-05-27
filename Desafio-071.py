'''Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário
qual valor deverá ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

Obs: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1'''

print('=' * 35)
print('{:^35}'.format('BANCO DO EMERSON'))
print('=' * 35)
print('''NOTAS DÍSPONIVEIS:
R$ 200.00
R$ 100.00
R$ 50.00
R$ 20.00
R$ 10.00
R$ 5.00''')
saque = int(input('Valor do saque: R$'))
total = saque
cd = 200
tcd = 0
while True:
    if total >= cd:
        total -= cd
        tcd += 1 
    else:
        if tcd > 0:
            print(f'Total de {tcd} cédulas de R${cd:.2f}')
        if cd == 200:
            cd = 100
        elif cd == 100:
            cd = 50
        elif cd == 50:
            cd = 20
        elif cd == 20:
            cd = 10
        elif cd == 10:
            cd = 5
        tcd = 0
        if total == 0:
            break 
print('=' * 35)
print('{:35}'.format('FINAL DO PROGRAMA'))
print('=' * 35)
