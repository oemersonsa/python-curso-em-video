#crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome
nome = str(input('Digite o nome complto: ')).strip().lower()
print('Seu nome tem Silva?','silva' in nome)