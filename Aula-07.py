# OPeradores aritimeticos:
# + soma ex: (5+2==7)
# - subtração ex: (5-2==3)
# * mutiplicação ex: (5*2==10)
# / divisão ex: (5/2==2.5)
# ** potêncialização ex: (5**2==25)
# // divisão inteira ex: (5//2==2) o resultado é apenas do número inteiro
# % resto da divisão ex: (5%2==1) o resultado da sobra da divisão inteira
# == resultado

# Ordem de precedência:
# 1 () - vai ser o primeiro a ser resolvido
# 2 ** - vai ser o segundo a ser resolvido
# 3 *, /, //, %. (resolve quem aparecer primeiro no codigo) - vai ser o terceiro a ser resolvido
# 4 +, -. - vai ser o último a ser resolvido

# **(1/2) para caulcular raiz quadrada de um numero ex: 81**(1/2)==9
# **(1/3) para caulcular raiz cúbica de um número ex: 127**(1/3)==5.026525695313479

# /n quebra linha ou cria uma nova linha
# end='' não quebra a linha ou deixa tudo na mesma linha mesmo que tenha mais de um print
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end='')
print('. A divisão inteira é {} e potência {}'.format(di, e))

