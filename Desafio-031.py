'''Desenvolva um progama que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando
R$0,50 por km para viages até 200km e R$0,45 para viagens mais longas.'''

dis = float(input('Calcule o preço da Sua viagem.\nDigite a distâcia em km do seu destino: '))
if dis <= 200.00:
    print('O valor da sua viagem é de R${:.2f}'.format(dis * 0.50))
else:
    print('O Valor da sua viagem é de R${:.2f}'.format(dis * 0.45))
