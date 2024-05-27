'''Escreva um programa que leia um número qualquer e peça pro usuário escolher qual vai ser a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal'''

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases de conversão:
[ 1 ] converter para BÍNARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Digite sua opção: '))
if opcao == 1:
    print('{} convertido em BÍNARIO é: {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido em OCTAL é: {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido em HEXADECIMAL é: {}'.format(num, hex(num)[2:]))
else: 
    print('OPção ínvalida!!!')