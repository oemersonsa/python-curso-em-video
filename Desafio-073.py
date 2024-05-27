'''Crie uma tupla preenchida com os 20 primeiros colocados
da tabela do brasileirão, na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados
B) Os 4 últimos colocados
C) Uma lista com os times em ordem alfabética
D) Em que posição está o time Corinthians'''

tabela = ('Palmeiras', 'Internacional', 'Fluminense', 'Flamengo', 'Corinthians', 'Athletico-PR', 'Atlético-MG', 'América-MG', 'Goiás',
'Botafogo', 'Santos', 'Bragantino', 'São Paulo', 'Fortaleza', 'Ceará', 'Coritiba', 'Avaí', 'Cuiabá', 'Atlético-GO', 'Juventude')
print('-' * 25)
print(f'Lista de Times do Brasileirão: {tabela}')
print('-' * 25)
print(f'Os cinco primeiros colocados são: {tabela[:5]}')
print('-' * 25)
print(f'Os quatro últimos colocados são: {tabela[-5:]}')
print('-' * 25)
print(f'Tabela em ordem alfabética: {sorted(tabela)}')
print('-' * 25)
print(f'O Corinthians está na {tabela.index("Corinthians")+1}° posição')
