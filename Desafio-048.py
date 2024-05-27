'''Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que 
se encontram no intervalo de 1 até 500.'''
s = 0
ct = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        s = s + c
        ct = ct + 1 
print('A soma dos {} valores é {}.'.format(ct, s))
# Ambos os jeitos vão dar o mesmo resultado
soma = 0
cont = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma dos {} valores é {}.'.format(cont, soma))