'''Crie um programa que leia vários números inteiros pelo teclado. No Final da execução, mostre a média 
entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar'''

resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'S':
    n = int(input('Digite um número: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n         
    resp = str(input('Deseja Continuar o prorama? S/N: ')).strip().upper()[0]
media = soma / quant
print('A média entre os números {} digitados é {}. O maior número digitado foi {} e o menor {}.'.format(quant, media, maior, menor))

