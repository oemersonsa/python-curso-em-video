try:
    a = int(input('Numerador: '))
    b = int(input('Denomindaor: '))
    c = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero.')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados')
except Exception as erro:
    print(f'O erro foi {erro.__cause__}')
else:
    print(f'O resultado é {c}')
finally:
    print('Volte sempre, muito obrigado!')