'''Faça um programa que leia o nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.'''

alunos = dict()
for c in range (0, 1):
    alunos['nome'] = str(input('Nome: '))
    alunos['media'] = float(input(f'Média de {alunos["nome"]}: '))
    if alunos['media'] >= 7:
        alunos['situação'] = 'Aprovado'
    else:
        alunos['situação'] = 'Reprovado'
'''print(f'Nome é igual a {alunos["nome"]}')
print(f'Média é igual a {alunos["media"]}')
print(f'A situação é {alunos["situação"]}')'''
for k, i in alunos.items():
    print(f'{k} é igual a {i}')