#um professor quer sortear um de seus quatro alunos para apagar o quadro.
#faça um programa que ajude ele, lendo os nomes deles e escrevendo o nome do escolhido.

'''import random
a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')
l = [a1, a2, a3, a4]
e = random.choice(l)
print('O aluno sorteado foi {}!'.format(e))'''

from random import choice
a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')
l = [a1, a2, a3, a4]
e = choice(l)
print('O aluno sorteado foi {}!'.format(e))