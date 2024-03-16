#instrução para aparecer algo na tela
print("Olá mundo")

print(7+4)

#Utilização do "+" ou ","
#print ('Olá mundo' + 5) = ERROR
print ('Olá mundo', 5)

# -DESAFIOS GUANABARA-

#Desafio Aula 4
nome = input('Qual o seu nome ?')
print('Boas vindas!', nome, 'É um prazer em te conhecer!')

#Desafio Aula 4

Dia = input('Qual o dia do seu nascimento ?')
Mês = input('Qual o mês do seu nascimento ?')
Ano = input('Qual o ano do seu nascimento ?')

print('Você nasceu no dia', Dia,'de',Mês,'de',Ano,'Correto?')

#Desafio Aula 4
numero1 =int(input('Primeiro número'))
numero2 =int(input('Segundo número'))

print('A soma é', numero1 + numero2 )

#Tipos primitivos
'''
int = 7; -4; 0; 9875
float = 4.5; 0.0076; -15.223; 7.0
bool = True; False
str = 'Olá'; '7.5'; ''

'''

#Outra forma de realizar a função print
'''
name = input('Qual é o seu nome ?')
print('Boas vindas {}!'.format(name))
'''
#Desafio Aula 6

n1 = int(input('Digite um número:'))
n2 = int(input('Digite mais um número:'))
soma = n1 + n2
#print('A soma entre',n1,'e',n2,'é:',soma)
print('A soma entre {} e {} é:{}'.format(n1, n2, soma))

#Operadores aritméticos
'''
+ = Adição
- = Subtração
* = Multiplicação
/ = Divisão
** = Potência
// = Divisão inteira
% = Resto da divisão
'''
#Ordem de procedência
'''
1 - ()
2 - **
3 - *; /; //; %
4 - +; -

'''
#Trabalhando com Módulos

'''
import 'biblioteca'


from 'biblioteca' import café
'''
'''
Biblioteca MATH

ceil = arredondar para cima 
floor = arredondar para baixo
trunc = truncar o número(tirar as casas decimais)
pow = potência 
sqrt = raiz quadrada
factorial
'''
from math import sqrt

número = int(input('Digite um número: '))
raiz = sqrt(número)

print('A raiz quadrada de {} digitado é : {:.2f}'.format(número, raiz))

#Manipulando texto

#Index
frase = 'Curso em Vídeo Python'
#        01234567891011121314151617181920 = Curso em Vídeo Python

#print(frase[0:14])
print(frase[:14])

#Análise

print(len(frase))
print(frase.count('o'))
print(frase.find('deo'))
print('Python' in frase)

#Transformação

print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

'''
.strip : remover espaços inúteis
.rstrip : right strip
.lstrip : left strip
''' 
sentença =    'Aprenda Pyhton'     
print(sentença.strip())

frase.split()
'-'.join(frase)

#Condições

'''
carro.siga()
if carro.esquerda():
    carro.siga()
    carro.direita()
    carro.siga()
    carro.direita()
    carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()
else:
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.esquerda()
    carro.siga()
carro.pare()   
'''
tempo = int(input('Quantos anos tem o seu carro ?'))
if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')

#Condição simplificada
'''
tempo = int(input('Quantos anos tem o seu carro ?'))
print('Carro novo') if tempo <=3 else print('Carro velho')
print('--FIM--')
'''
#Cores para o terminal
'''
\033[0;33;44m
 \033[Style;Text;Backgroundm

Style
0 - None
1 - bold
4 - underline
7 - negative

Text           background
30 - branco       40
31 - vermelho     41
32 - verde        42
33 - amarelo      43
34 - azul         44
35 - roxo         45
36 - azul claro   46
37 - cinza        47
'''
print('\033[4;31;46mOlá mundo')


#AULAS MUNDO 2

#Condições aninhadas - Condições colocadas umas dentro de outras

'''
carro.siga()
if carro.esquerda():
    carro.siga()
    carro.direita()
    carro.siga()
    carro.direita()
    carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()
elif carro.direita():
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.esquerda()
    carro.siga()
else:
    carro.siga()
carro.pare()   
'''

nome = str(input('Qual é o seu nome ?'))

if nome == 'Lucas':
    print('Que nome bonito !')
elif nome == 'Maria' or 'Alessandra' or 'Luiz':
    print('Que nome lindo !')
else:
    print('Seu nome é bem normal')

'''
passo
passo
passo
passo
passo
passo
passo
passo
passo
pega

laço c no intervalor(1,10) ------>    for c in range(1,10)
    passo                                 passo
pega                                  pega

'''

'''
passo
pula
passo
pula
passo
pula
passo
pega

laço c no intervalo(0,3) ------>    for c in range(0,3)
    passo                               passo
    pula                                pula
passo                               passo
pega                                pega
'''

#Situação com moedas

'''
laço c no intervalo(0,3)
    if moeda
        pega
    else:
        passo
        pula
passo
pega
'''
'''
for loop precisa de um limite definido para funcinar.
for: estrutura de repetição com variável de controle

While: estrutura de repetição com teste lógico

enquanto não maçã:               while not maçã:
    passo                           passo
pega                            pega

enquanto não maçã:               while not maçã:
    se chão:                        if chão:
        passo                           passo
    se buraco:                      if buraco:
        pula                            pula
    se moeda:                       if moeda:
        pega                            pega
pega                             pega

'''

'''
for c in range(1,10):
    print(c)
print('Fim')
'''
c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')
'''
enquanto verdadeiro:               while True:
    se chão:                        if chão:
        passo                           passo
    se buraco:                      if buraco:
        pula                            pula
    se moeda:                       if moeda:
        pega                            pega
    se troféu                       if troféu:
        pula                            pula
        interrompa                      break           
pega                             pega

'''
#Tuplas
lanche = ('Pizza', 'Suco', 'Batata', 'Pudim')

'''for c in range (0,len(lanche)):
    print(f'Eu vou comer {lanche[c]} na posição {c}')

for pos, c in enumerate(lanche):
    print(f'Eu vou comer {lanche} na posição {pos}')
print('Comi pra caramba!')'''
#Colocar tuplas em ordem alfabética

'sorted(lanche)'

a = (1,2,4)
b = (5,8,4,7)
c = a + b
print(c.index(4))

#Listas - Mutáveis 
'''
 Para adicionar um item a uma lista é necessário usar o método append()
- Adicionar item no final
list  = ['Hamburguer','Suco','Pizza','Pudim']
list.append('cookie') 
- Adicionar item onde eu quiser
lanche.insert[0,'Cachorro-Quente']
- Apagar
del lanche[3]
ou
lanche.pop[3]
ou
lanche.remove['Pizza']
'''
#Gerar lista a partir do list

valores = list(range(4,11))

#Ordenar lista
'valores.sort()'

#Ordem inversa
'valores.sort(reverse=True)'
valores = []
for count in range(0,6):
    valores.append(int('Digite um valor: '))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')

#Manipulando listas
'''
Isso é um ligamento de listas:
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
- Portanto tudo que for alterado na lista B será realizada na lista A também.

Isso é uma cópia de lista:
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
- Portando são listas diferentes, mecher no B não altera o A.
'''