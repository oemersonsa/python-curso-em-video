'''faça um programa que leia um número qualquer e mostre seu fatorial
Ex: 5! = 5x4x3x2x1 = 120'''

#from math import factorial
n = int(input('Digite um número: '))
c = n
f = 1
#f = factorial(num)
#print('O fatorial de {} é {}.'.format(num, f))
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' X ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
