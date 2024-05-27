'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC a mostra seu status,
de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 g 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: obesidade
- Acima de 40: obesidade mórbida'''

print('Calcule seu IMC!!!')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: ')) 
imc = (peso / altura ** 2)
if imc < 18.5:
    print('Analisando seu IMC no valor de {:.1f} você está ABAIXO DO PESO!'.format(imc))
elif 18.5 <= imc < 25:
    print('Analisando seu IMC no valor de {:.1f} você está no PESO IDEAL!'.format(imc))
elif 25 <= imc < 30:
    print('Analisando seu IMC no valor de {:.1f} você está com SOBREPESO!'.format(imc))
elif 30 <= imc < 40:
    print('Analisando seu IMC no valor de {:.1f} você está com OBESIDADE!'.format(imc))
else:
    print('Analisando seu IMC no valor de {:.1f} você está com OBESIDADE (SEVERA)!'.format(imc))