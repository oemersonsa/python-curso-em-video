'''faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário
O programa será interrompido quando o valor solicitado for negativo'''


t = 'Tabuada'
c = m = 0
print(f'{t:-^40}')
while True:
    n = int(input('Quer ver a tabuada de qual número: '))
    print('-' * 25)
    if n < 0:
        break
    for num in range (1, 11):
         print(f'{n:2} X {num:2} = {n * num}')
    print('-' * 25)
    c += 1
print(f'Você Calculou a TABUADA de {c} números diferentes')
print('Fim do programa')

   
   
