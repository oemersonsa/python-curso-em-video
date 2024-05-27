'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, 
que é a condição de parada. No final. mostre quantos números Foram digitados e qual foi a soma entre eles
(desconsiderando o Flag).'''
num = n = cont = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    n += 1 
    cont += num
    num = int(input('Digite um número [999 para parar]: '))
print('No total foram digitados {} números, e a soma entre todos eles é {}'.format(n, cont))
