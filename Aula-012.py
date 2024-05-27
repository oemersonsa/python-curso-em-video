nome = str(input('Digite seu nome: ')).strip()
if nome == 'Emerson':
    print('Seu nome é bem bonito!')
elif nome == 'Maria' or nome == 'José' or nome == 'João':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Juliana Carol Leticia':
    print('Belo nome feminino!')
#else:
#    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))
