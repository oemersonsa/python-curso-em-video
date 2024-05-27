def metade(n=0, f=False):
    res = n / 2
    return res if not f else moeda(res)


def dobro(n=0, f=False):
    res = n * 2
    return res if not f else moeda(res)


def aumentar(n=0, v=0, f=False):
    res = n + (n * v / 100)
    return res if not f else moeda(res)


def diminuir(n=0, v=0, f=False):
    res = n - (n * v / 100)
    return res if not f else moeda(res)


def moeda(p=0, moeda='R$'):
    return f'{moeda}{p:.2f}'.replace('.', ',')


def resumo(p=0, txa=10, txd=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Dobro do preço: \t{dobro(p, True)}')
    print(f'Metade do preço: \t{metade(p, True)}')
    print(f'{txa}% de aumento: \t{aumentar(p, txa, True)}')
    print(f'{txd}% de redução: \t{diminuir(p, txd, True)}')
    print('-' * 30)




