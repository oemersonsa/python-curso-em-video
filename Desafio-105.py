'''Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de aluno
 e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor.'''


def notas(*n, sit=False):
    alunos = dict()
    alunos['total'] = len(n)
    alunos['maior'] = max(n)
    alunos['menor'] = min(n)
    alunos['media'] = sum(n) / len(n)
    if sit:
        if alunos['media'] >= 7:
            alunos['situação'] = "BOA!"
        elif alunos ['media'] >= 5:
            alunos['situação'] = "RAZOáVEL!"
        else:
            alunos['situação'] = "RUIM!"
    return alunos


resp = notas(5.5, 8, 9, sit=True)
print(resp)
