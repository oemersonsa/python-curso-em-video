# crie um codigo que leia o preco de um produto e que de o novo preço do produto com 5% de desconto

p = float(input('Insira o valor do produto: R$'))
d = int(input('Insira a porcentagem de desconto: %'))
print('O produto que custava R${:.2f}, com o desconto de {}%, custara R${:.2f}'.format(p, d, (p - (p * d / 100))))
print('Valor do desconto R${:.2f}'.format(p * d / 100))
