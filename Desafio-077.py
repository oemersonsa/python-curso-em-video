'''Crie um programa qie tenha uma tupla com várias palavras (não usar acentos)
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais '''


palavras = ('linguagem', 'python', 'video', 'programa', 'emerson', 'desafio', 'aula')
for p in palavras:
        print(f'\nNa Palavra {p} temos as seguintes vogais: ', end='')
        for letra in p:
            if letra.lower() in 'aeiou':
                print(f'{letra} ', end='')



