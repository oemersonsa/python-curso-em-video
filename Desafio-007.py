# crie um código que leia as notas de um aluno é de a média
n1 = int(input('Nota 1: '))
n2 = int(input('Nota 2: '))
n3 = int(input('Nota 3: '))
n4 = int(input('Nota 4: '))
m = float((n1+n2+n3+n4)/4)
print('A média do Aluno é {}'.format(m))

if m >= 7:
    print('Aluno aprovado!')
else:
    print('aluno reprovado!')