'''Escreva um programa que leia a velocidade de um carro.
se ele ultrapassar a velocidade de 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada km acimda do limite.'''
vel = float(input('Digite a velocidade: km'))
if vel > 80:
    print('\033[1;32mVocê ultrapassou a velocidade máxima de 80km/h, passando a {}km/h. '
          '\nO valor da sua multa é de R${:.2f}!'.format(vel, (vel-80)*7))
else:
    print('Você está dentro do limite de velocidade!')