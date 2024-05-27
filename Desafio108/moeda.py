def metade(n=0):
    res = n / 2
    return res


def dobro(n=0):
    res = n * 2
    return res


def aumentar(n=0, v=0):
    res = n + (n * v / 100)
    return res


def diminuir(n=0, v=0):
    res = n - (n * v / 100)
    return res


def moeda(p=0, moeda='R$'):
    return f'{moeda}{p:.2f}'.replace('.', ',')

