# crie um codigo que leia o salario de um funcionario e informe o novo valor deste salario com um aumento de 15%

s = float(input('Insira o valor do sálario do funcionario: R$'))
a = float(input('Insira o valor percentual de aumento: %'))
print('O valor atual do sálario do funcionario é de R${:.2f}. \nCom o aumento de {}% = R${:.2f}. \nO novo sálario será de R${:.2f}'.format(s, a, (s * a / 100), s + (s * a / 100)))