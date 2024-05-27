'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "F" e "M". Caso esteja errado,
peça a digitação novamente até ter o valor correto'''

sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'FM':
    sexo = str(input('Dados inválidos, por favor informe seu sexo [M/F]: ')).strip().upper()[0]
if sexo in 'M':
    sexo = 'MASCULINO'
else:
    sexo = 'FEMININO'
print('Sexo {} registrado com sucesso!'.format(sexo))
