# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
d = int(input('Insira a quantidade de dias de uso: '))
km = float(input('Insira os quilometros rodados: Km'))
print('Veiculo usado por {} dias. \nRodou {:.2f}Km. \nTotal a pagar: R${:.2f}.'.format(d, km, d * 60 + km * 0.15))