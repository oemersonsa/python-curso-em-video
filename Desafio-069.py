'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá
perguntar se o usuário quer ou não continuar. No final, mostre:
A- Quantas pessoas tem mais de 18 anos
B- Quantos homens foram cadastrados
C- Quantas mulheres tem menos de 20 anos'''

maioridade = homens = mulheres = mulher20 = 0
print('-' * 30)
print('CADASTRO DE PESSOAS')
print('-' * 30)
while True:
    idade = int(input('Digite a idade: '))
    if idade > 18:
        maioridade += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Escolha o sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        homens += 1
    else:
        mulheres += 1
    print('-' * 30)
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if cont == 'N':
        break
    if sexo == 'F' and idade < 20:
        mulher20 += 1
print('-' * 30)
print(f'Cadastro finalizado com sucesso. Ao todo {maioridade} tem mais de 18 anos')
print(f'{homens} homens foram cadastrados e {mulheres} mulheres tem menos de 20 anos.')
