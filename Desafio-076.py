'''Crie um programa que tenha uma tupla única com nomes
de produtos e seus respectivos preços, na sequência.

No final, mostre uma listagem de preços, organizando os dados em forma tabular
'''

t = ('Celular', 1500, 'Capa', 25, 'Pelicula', 10, 'Fone Bluetooth', 200, 'Chip', 5)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for p in range(0, len(t)):
    if p % 2 ==0:
        print(f'{t[p]:.<30}', end='')
    else:
        print(f'R${t[p]:>8.2f}')
print('-' * 40)
