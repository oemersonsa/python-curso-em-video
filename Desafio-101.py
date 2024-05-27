'''Exercício Python 101: Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''


def voto(a):
    from datetime import datetime
    atual = datetime.now().year
    idade = atual - nasc
    if idade == 16 or idade <= 18 or idade >= 65:
        print(f'Com {idade} anos: VOTO OPCIONAL!')
    elif idade >= 18 or idade <= 65:
        print(f'Com {idade} anos: VOTO OBRIGATóRIO!')
    else:
        if idade < 16:
            print(f'Com {idade} anos: NÃO VOTA!')


print('-' * 35)
nasc = int(input('Digite o ano de nascimento: '))
voto(nasc)
