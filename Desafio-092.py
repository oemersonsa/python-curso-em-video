'''Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''

from datetime import datetime
dados = dict()
trabalhador = list()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nasc.: '))
dados['idade'] = datetime.now().year - nasc
dados['carteira'] = int(input('N° da CTPS: '))
if dados['carteira'] != 0:
        dados['contrato'] = int(input('Ano de contratação: '))
        dados['salario'] = float(input('Salário: R$'))
        dados['aposentadoria'] = dados['idade'] + ((dados['contrato'] + 35) - datetime.now().year)
print('-' * 30)
for k, i in dados.items():
    print(f' - {k} tem o valor {i}.')