# crie um codigo que leia um valor em metros e o exiba convertido em centimetros e milimetros

mt = float(input('Insira o valor em metros: '))
print('Calculadora de Medidas:')
print('-' * 40)
print('Valor em Quilômetros: {:.2f}km;'
      '\nValor em Hectômetros: {:.2f}hm;'
      '\nValor em Decâmetros: {:.2f}dam;'
      '\nValor em Metros: {:.2f}m;'
      '\nValor em Decímetros: {:.2f}dm;'
      '\nValor em Centímetros: {:.2f}cm;'
      '\nValor em Milímetros: {:.2f}mm.'.format(mt / 1000, mt / 100, mt / 10, mt, mt * 10, mt * 100, mt * 1000))
print('-' * 40)
