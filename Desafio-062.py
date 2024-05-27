'''Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
 O programa encerra quando ele disser que quer mostrar O termos'''

print('GERADOR DE PA:')
print('=' * 15)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1 
total = 0
mais = 10 
while mais != 0:
    total += mais 
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1 
    print('Pausa')
    mais = int(input('Quantos termos mais você quer mostrar? '))
print('Fim do programa, foram mostrados ao todo {} termos.'.format(total))