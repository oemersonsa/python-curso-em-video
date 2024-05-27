'''Refaça o DESAFIO 035 dos triângulos. acrescentando o recurso de mostrar que tipo da triângulo será formado:
- Equilátero: todos os lados iquais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes'''

r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Sim é possível formar um triângulo ', end= '')
    if r1 == r2 == r3:
        print('EQUILATERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!') 
    else:
        print('ISÓCELES!') 
else:
    print('Não é possível formar um triângulo com as retas!')
