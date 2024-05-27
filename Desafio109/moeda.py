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

