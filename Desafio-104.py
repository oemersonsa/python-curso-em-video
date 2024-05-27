'''Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')'''


def leiaInt(num):
    ok = False
    valor = 0
    while True:
        num = (input(num))
        if num.isnumeric():
            valor = int
            ok = True
            print(f'Você digitou o número {num}')
        else:
            print('\033[31mERRO! Digite Apenas números inteiros!\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')

