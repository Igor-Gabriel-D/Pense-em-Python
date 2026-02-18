#Exercício 3.1
#Escreva uma função chamada right_justify, que receba uma string chamada s como
#parâmetro e exiba a string com espaços suficientes à frente para que a última letra da
#string esteja na coluna 70 da tela:
def right_justfy(s):
    print((" "*(70 -len(s))) + s  )


right_justfy("hello")

'''
Exercício 3.2
Um objeto de função é um valor que pode ser atribuído a uma variável ou passado como
argumento. Por exemplo, do_twice é uma função que toma um objeto de função como
argumento e o chama duas vezes:
def do_twice(f):
f()
f()
Aqui está um exemplo que usa do_twice para chamar uma função chamada print_spam
duas vezes:
def print_spam():print('spam')
do_twice(print_spam)
1. Digite este exemplo em um script e teste-o.
2. Altere do_twice para que receba dois argumentos, um objeto de função e um valor, e
chame a função duas vezes, passando o valor como um argumento.
3. Copie a definição de print_twice que aparece anteriormente neste capítulo no seu
script.
4. Use a versão alterada de do_twice para chamar print_twice duas vezes, passando
spam como um argumento.
5. Defina uma função nova chamada do_four que receba um objeto de função e um
valor e chame a função quatro vezes, passando o valor como um parâmetro. Deve
haver só duas afirmações no corpo desta função, não q uatro.
'''

def do_twice(f, val):
    f(val)
    f(val)

def print_spam(val):
    print(val)

def print_twice(bruce):
    print(bruce)
    print(bruce)

def do_four(f, val):
    f(val)
    f(val)

do_four(print_twice, "spam")

'''
Exercício 3.3
Nota: Este exercício deve ser feito usando-se apenas as instruções e os outros
recursos que aprendemos até agora.
1. Escreva uma função que desenhe uma grade como a seguinte:

Dica: para exibir mais de um valor em uma linha, podemos usar uma sequência de
valores separados por vírgula:
print('+', '-')
Por padrão, print avança para a linha seguinte, mas podemos ignorar esse
comportamento e inserir um espaço no fim, desta forma: python print('+', end='
') print('-') A saída dessas instruções é + -. Uma instrução print sem argumento
termina a linha atual e vai para a próxima linha.
2. Escreva uma função que desenhe uma grade semelhante com quatro linhas e quatro
colunas.

'''




print( (("+" + (" -"*4) + " "  )*2 + "+\n" + ((("|" + (" "*9))*2 + "|"  )+"\n") * 4)*2 + (("+" + (" -"*4) + " "  )*2 + "+\n") )

print(  (  (("+" + (" -"*4) + " "  )*4 + "+\n" + ((("|" + (" "*9))*4 + "|"  )+"\n") * 4)*4 + (("+" + (" -"*4) + " "  )*4 + "+\n")  )  )


