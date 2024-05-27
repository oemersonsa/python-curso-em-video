'''A Confederação Nacional de Natação
precisa de um programa que laia o ano da nascimento de um atleta a mostra sua catagoria. de acordo com a idade:
Até 9 anos : MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JUNIOR
Até 20 anos: SÊNIOR
Acima: MASTER'''

from datetime import date
atual = date.today().year
nasc = int(input('Digite a data de nascimento do atleta: '))
idade = atual - nasc 
if idade <= 9:
    print('A categoria do atleta é MIRIM!')
elif idade <= 14:
    print('A categoria do atleta é INFANTIL!')
elif idade <= 19:
    print('A categoria do atleta é JUNIOR!')
elif idade <= 25:
    print('A categoria do atleta é SÊNIOR!')
else:
    print('A categoria do atleta é MASTER!')
