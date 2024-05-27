lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudin')
for c in lanche:
    print(f'Eu vou comer {c}')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
   print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra caramba')

print(sorted(lanche))
print(lanche)

a = 2, 5, 4
b = 5, 8, 1, 0
c = a + b
print(c)
print(c.index(8))
print(c.count(5))