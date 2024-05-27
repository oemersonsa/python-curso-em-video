'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo 
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.'''

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for c in range (1, 5):
    print('-----{}° PESSOA-----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip()
    somaidade += idade
    if c == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {:.0f} anos.'.format(mediaidade))
print('O homem mais velho se chama {} e tem {} anos.'.format(nomevelho, maioridadehomem))
print('Ao todo {} mulheres tem menos de 20 anos.'.format(totmulher20))
