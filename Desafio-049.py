'''Refaça o Desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora 
utilizando um laço for.'''

n = int(input('Insira o número para saber a sua tabuada: ')) 
print('*' * 13)
print('Tabuada de {}'.format(n))
print('*' * 13)
for c in range (0, 11):
    print('{:2} X {:2} = {}'.format(c, n, (c * n)))
print('*' * 13)