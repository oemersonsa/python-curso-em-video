# crie um codigo que leia um numero e mostre na tela o seu sucessor e o seu antecessor

n = int(input('Digite um número: '))
print('O número é {} seu antecessor é {} e o seu sucessor é {}'.format(n, (n-1), (n+1)))

# se for apenas para obter o resultado o modo com apenas uma variavel é o suficiente.
# porém caso seja nescessário guardar o valor do resultado para um uso futuro é recomendado o uso de mais váriaveis