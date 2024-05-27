from Desafio115.lib.interface import *
from Desafio115.lib.arquivo import *
from time import sleep

arq = 'cadastro.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas',
                    'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('Saindo do sistema...')
        sleep(0.5)
        print('Até logo!')
        break
    else:
        print('\033[31mERRO! Opção inválida!\033[m')
    sleep(1.5)
