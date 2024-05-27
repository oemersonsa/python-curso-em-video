p = float(input('Insira o valor do produto: R$'))
print('Valor do produto a vista com 10% de desconto é {:.2f}, valor do produto a prazo é de {:.2f}'.format((p - (p * 10 / 100)), (p + (p * 8 / 100))))