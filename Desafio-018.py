#faça um programa que leia um ângulo qualquer
#e mostre o valor de sen, cosseno e tangente desse ângulo
import math
a = float(input('Insira o ângulo: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('O ângulo de {} tem o SENO de {:.2f} \nO ângulo de {} tem o COSSENO de {:.2f} \nO ângulo de {} tem a TANGENTE de {:.2f}'.format(a, s, a, c, a, t))

#também da pra dar 'from math import radians, sin, cos, tan' e tirar as referências 'math.'