# Exemplo 1 
'''def mensagem(msg):
    print('-' * 30)
    print(f'{msg:^30}')
    print('-' * 30)


# Programa Principal
mensagem('SISTEMA DE ALUNOS')
mensagem('CADASTRO DE FUNCIONÁRIOS')
mensagem('ERRO DE SISTEMA')'''
# Exemplo 2
'''def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A Soma A + B = {s}')


# Programa Principal 
soma(a=4, b=5) # Posso declarar o valor diretamente 
soma(b=8, a=9)
soma(2, 1) # Ou declarar o valor indiretamente''' 

# Exemplo 3 
'''def contador(* num):
    tam = len(num)
    print(f'Recebi os valroes {num} e são ao todo {tam} números.')

contador(1, 0)
contador(1, 3, 6, 9, 8)'''

# Exemplo 4 
'''def dobra(lst):
    pos = 0 
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dobra(valores)
print(valores)'''

# Exemplo 5 
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}.')


soma(5, 2)
soma(6, 9, 15)
soma(56, 56, 23)