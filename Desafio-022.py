#crie um programa que leia o nome completo de uma pessoa e mostre:
#o nome com todas as letras minusculas e maisculas
#quantas letras sem considerar os espaços
#quantas letras tem o primeiro nome
nome = str(input('Insira seu nome completo: ')).strip()
print('Seu nome em maisculo é: {}.'.format(nome.upper()))
print('Seu nome em minusculo é: {}.'.format(nome.lower()))
print('Seu nome tem {} letras . '.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))
print('Seu primeiro tem {} letras'.format(nome.find(' ')))
