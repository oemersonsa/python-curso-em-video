for c in range(10, 0, -1): # Contagem regressiva 
    print(c)
print('Fim!')

for c in range(0, 10, 2): # Contagem pulando de 2 em 2 
    print(c)
print('Fim!')

for c in range(0, 10): # Contagem normal 
    print(c)
print('Fim!')

n = int(input('Digite um número: ')) # Contagem até o número digitado 
for c in range(0, n+1):
    print(c)
print('Fim!')

i = int(input('Inicio: ')) # Contagem de um numero a outro pulando uma quantidade de numeros 
f = int(input('Final: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('Fim!')

for c in range (0, 3): # repete inputs 
    n = int(input('Digite um número: '))

s = 0
for c in range (0, 4):
    n = int(input('Digite um número: '))
    s += n # Ou s = s + n
print('A soma de todos os números é {}'.format(s))