'''def contador(i, f, p): # Exemplo 1 função help()
    """
    -> Faz uma contagem e mostra na tela
    :param i: início da contagem;
    :param f: fim da contagem;
    :param p: passo da contagem;
    :return: sem retorno.
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print("FIM!")


# Programa Principal
help(contador)


def somar(a=0, b=0, c=0): # Exemplo 2 paramatros opcionais
    """
    -> soma três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    Função criada por @oemersonsa.
"""
    s = a + b + c
    print(f'A soma vale {s}')


# Programa Principal
somar(3, 2, 5)
somar(8, 4)


def teste(b): # Exemplo 3 Escopo de variaveis
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


# Progrma Principal
a = 5
teste(a)
print(f'A fora vale {a}')


def soma(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = soma(3, 2, 5)
r2 = soma(2, 2)
r3 = soma(6)
print(f'As somas valem {r1}, {r2} e {r3}')'''


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = int(input('Digite um número: '))
print(f'O fatorial de {f1} é igual a {fatorial(f1)}')
