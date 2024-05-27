'''Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
 e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''

pessoa = dict()
galera = list()
soma = media  = 0 
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'FM':
            break
        print('ERRO! Por favor digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        cont = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
        if cont in 'NS':
            break
        print('ERRO! Por favor digite apenas S ou N.')
    if cont in 'N':
        break
print('-' * 50)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A média de idade é de {media:5.2f} anos.')
print('As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}, ', end='')
print()
print('Lista das pessoas que estão acima da média de idade: ')
for p in galera:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print(f'{" ENCERRADO ":-^50}')