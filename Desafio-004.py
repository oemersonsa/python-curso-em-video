x = input('Digite algo:')
print('O tipo primitivo desse valor é:', type(x))
print('Tem espaços?', x.isspace())
print('Esse valor é númerico?', x.isnumeric())
print('Esse valor é alfabetico?', x.isalpha())
print('Esse valor esta em maiusculo?', x.isupper())
print('Esse valor esta em minusculo?', x.islower())
print('Esse valor está capitalizado?', x.istitle())
print('Esse valor é alfanumerico?', x.isalnum())
print('Esse valor pode ser impresso?', x.isprintable())

# .isspace = Afirma se o valor digitado só tem espaços
# .isnumeric = Afirma se o valor digitado é um número
# .isalpha = Afirma se o valor digitado é alfabetico (apenas com letras)
# .isupper = Afirma se o valor foi digitado apenas em maiusculo
# .islower = Afirma se o valor foi digitado apenas em minusculo
# .isalnum = Afirma se o valor digitado contem letra e numeros
# .isprintable = Afirma se o valor digitado pode ser impresso
# .istitle = Afirma se o valor está capitalizado (com a primeira  letra maiscula)