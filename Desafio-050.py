'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas dauqeles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.'''

soma = 0
cont = 0
for c in range (1, 7):
    n = int(input('Digite o {}° valor: '.format(c)))
    if n % 2 == 0:  
        soma += n 
        cont += 1
print('Você digitou {} números pares é a soma entre eles é {}'.format(cont, soma))
