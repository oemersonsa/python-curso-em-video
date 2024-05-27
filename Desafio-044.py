''' Elabore um programa que calcule o valor a ser pago por um produto. considerando o seu preço normal a condiÇão de pagamento:
- à vista dinheiro/chequa: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros'''

print('{:=^40}'.format(' LOJAS EMERSON '))
preco = float(input('Insira o valor da compra: R$'))
print('''Escolha a forma de pagamento:
[1] Á Vista em Dinheiro/Cheque
[2] Á Vista no Cartão
[3] Parcelado em 2X no Cartão
[4] Parcelado em 3X ou mais no Cartão''')
pagamento = int(input('Escolha a forma de pagamento: '))
if pagamento == 1:
    print('A compra no valor de R${:.2f}, Á vista no dinheiro/chueque custará R${:.2f}'.format(preco, preco - (preco * 10 / 100)))
    print('Desconto de 10% no valor de R${:.2f}'.format(preco * 10 / 100))
elif pagamento == 2:
    print('A compra no valor de R${:.2f}, Á vista no cartão custará R${:.2f}'.format(preco, preco - (preco * 5 / 100)))
    print('Desconto de 5% no valor de R${:.2f}'.format(preco * 5 / 100))
elif pagamento == 3:
    print('A compra no valor de R${:.2f}, parcelado em 2X custará R${:.2f}'.format(preco, preco))
    print('Em 2 parcelas de R${:.2f} cada.'.format(preco / 2))
elif pagamento == 4:
    parcelas = int(input('Quantas parcelas? '))
    print('A compra no valor de R${:.2f}, parcelado em {}x custará R${:.2f}'.format(preco, parcelas, preco + (preco * 20 / 100)))
    print('Em {} parcelas de R${:.2f} cada com JUROS.'.format(parcelas, (preco + (preco * 20 / 100)) / parcelas))
    print('JUROS de R${:.2f}.'.format(preco * 20 / 100))
