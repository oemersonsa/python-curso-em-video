#condições
'''tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print("Seu carro é novo!")
else:
    print('Seu carro não é novo!')
print('--FIM--')'''
tempo = int(input('Quantos anos seu carro tem? '))
print('Seu carro é novo!' if tempo <= 3 else 'Seu carro não é novo!')
print('--FIM--')