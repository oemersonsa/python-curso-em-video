#crieum programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
#ex: digite um numero:
#o numero 6.127 tem a parte inteira 6.

'''import math
n = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}'.format(n, math.trunc(n)))'''

'''from math import trunc
n = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}'.format(n, trunc(n)))'''

n = float(input('Digite um número: '))
print('o número {} tem a parte inteira {}'.format(n, int(n)))