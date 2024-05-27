'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar 
- Se é a hora de se alistar 
- Se já passou do tempo de alistamento
Seu programa também deve mostra o tempo que falta ou que passou do prazo.'''

from datetime import date
print('\033[1;32m#\033[m' * 50)
print('\033[1;32mDescubra aqui seu prazo pro alistamento militar!\033[m')
print('\033[1;32m#\033[m' * 50)
atual = date.today().year
nasc = int(input('Digite seu ano de nascimento: '))
idade = atual - nasc
if idade == 18:
    print('\033[1;34mEstá na hora de se alistar!\033[m')
elif idade < 18:
    saldo = 18 - idade 
    print('\033[1;33mAinda faltam\033[m \033[1;4m{}\033[m \033[1;33manos para você se alistar.'.format(saldo))
    ano = atual + saldo
    print('\033[1;33mSeu alistamento será em\033[m \033[1;4m{}\033[m'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('\033[1;31mSeu prazo para se alistar venceu a\033[m \033[1;4m{}\033[m \033[1;31manos.'.format(saldo))
    ano = atual - saldo
    print('\033[1;31mSeu ano de alistamento foi em\033[m \033[1;4m{}\033[m'.format(ano))