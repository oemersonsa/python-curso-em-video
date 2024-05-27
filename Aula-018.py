'''dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0])
print(dados[1])

pessoas = list()
pessoas.append(dados[:])

pessoas = [['Pedro', 25],['Maria', 19],['João', 32]]
print(pessoas[0][0]) #Pedro
print(pessoas[1][1]) #19
print(pessoas[2][0]) #João
print(pessoas[1]) #['Maria', 19]'''

'''teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''

'''galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)
print(galera[0])
print(galera[0][0])
print(galera[2][1])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')'''

galera = list()
dado = list()
totmaior = totmenor = 0
for c in range (0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

print(galera)
for p in galera:
    if p[1] >= 21:
        totmaior += 1
        print(f'{p[0]} é maior de idade!')
    else:
        print(f'{p[0]} é menor de idade')
        totmenor += 1

print(f'temos {totmaior} maiores e {totmenor} menores de idade')