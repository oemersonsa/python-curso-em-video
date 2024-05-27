# crie um codigo que leia a largura e altura de uma parede em metros,
# e calcule a sua área e a qauntidade de tinta nescessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2m²

a = float(input('Insira a altura da parede: '))
l = float(input('Insira a largura da parede: '))
ar = a * l
print('Sua parede tem a dimensão de {}m X {}m e sua área é de {}m². \nSerá nescessário {}l de tinta para pintá-la!'.format(a, l, ar, (ar / 2)))