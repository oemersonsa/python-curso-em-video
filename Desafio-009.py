# crie um codigo que leia um numero e mostre na tela a sua tabuada

#n = int(input('Insira o número: '))
#t = n * 1, n * 2, n * 3, n * 4, n * 5, n * 6, n * 7, n * 8, n * 9, n * 10
#print('O número inserido foi {} e a sua tabuada é {}'.format(n, t))

n = int(input('Insira o número para saber a sua tabuada: '))
i = 1
print('*' * 13)
print('Tabuada de {}'.format(n))
print('*' * 13)
while(i <= 10):
    print('{:2} X {:2} = {}'.format(i, n, (i * n)))
    i = i + 1
print('*' * 13)