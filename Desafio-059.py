'''Crie um programa que leia dois valores e mostre um menu na tela: 
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa 
Seu programa deverá realizar a operação desejada em cada caso'''

n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
opcao = 0 
while opcao != 5:
    print('''[1] Somar 
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')
    opcao = int(input('Digite sua opção: '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}.'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O produto de {} X {} é {}.'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1 
        else:
            maior = n2
            print('Entre {} e {} o maior número é {}.'.format(n1, n2, maior))
    elif opcao == 4:
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida tente novamente!')
print('Fim do programa!')