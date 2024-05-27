#Faça um programa que leia o nome completo de uma pessoa e mostre o primeiro e o último nome separadamente
#ex: Ana Maria de Souza
#Primeiro: Ana
#Último: Souza
nome = str(input('Digite o nome: ')).strip()
n = nome.split()
print('Prazer em te conhecer! \nSeu primeiro nome é: {}. '
      '\nE seu último nome é: {}'.format(n[0], (n[len(n)-1])))