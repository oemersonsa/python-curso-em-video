#O mesmo professor do do desafio anterior quer sortear a ordem de apresentação dos trabalhos
#faça um programa que leia o nome dos 4 alunos e mostre a ordem sorteada.

from random import shuffle
a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')
l = [a1, a2, a3, a4]
shuffle(l)
print('A ordem de apresentação de trabalho será ')
print(l)