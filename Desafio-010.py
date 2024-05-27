# crie um codigo que leia quanto dinheiro uma pessoa tem na carteira e diga quantos dolares ela pode comprar

v = float(input('Insira o valor em carteira: R$'))
d = v / 5.24
e = v / 5.22
print('O valor em carteira é de R${:.2f} \nO valor que pode ser adquirido em doláres é de US${:.2f} \nO valor que pode ser adquirido em euros é de £{:.2f}'.format(v, d, e))