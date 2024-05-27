#crie um programa que leia o comprimento do cateto oposto e cateto adjacente de um triângulo retaângulo
#Calcule e mostre o comprimento da hipotenusa

'''co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai ser {:.2f}!'.format(hi))'''

'''import math
co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai ser {:.2f}'.format(hi))'''

from math import hypot
co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai ser {:.2f}'.format(hi))