def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite apenas números inteiros!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número!\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite apenas números reais!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número!\033[m')
            return 0
        else:
            return n


num = leiaInt('Digite um número inteiro: ')
print(f'O valor digitado foi {num}!')
num2 = leiaFloat('Digite um número real: ')
print(f'O valor digitado foi {num2}!')
