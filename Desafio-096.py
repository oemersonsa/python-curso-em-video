'''Exercício Python 096: Faça um programa que tenha uma função chamada área(), 
que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''

def area(l, c):
    r = l * c
    print(f'A área de um terreno {l}x{c} é de {r:.1f}m².')    

    
print('-' * 30)
print(f'{"Controle de Terrenos":^30}')
print('-' * 30)
l = float(input('Largura(m): '))
c = float(input('Comprimento(m): '))
area(l=l, c=c)

