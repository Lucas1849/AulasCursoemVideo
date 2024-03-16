#A função help()
help(print)
#Docstrings 
def contador (i,f,p):
    """
    ->Realiza uma contagem com 3 parâmetros:
    1º parâmetro: Inicio da contagem
    2º parâmetro: Fim da contagem
    3º parâmetro; Passo da contagem
    return = sem retorno
    """
    c = i
    while c <=f :
        print(f'{c}',end='  ')
        c += p
print()

help(contador)

contador(2,20,1)
#Parâmetros opcionais
def soma (a=0,b=0,c=0):
    s = a + b + c
    #Várias somas com resultados diferentes
    return s


r1 = soma(1,3)
r2 = soma(3)
r3 = soma(9,6,3)
print(f'Meus cálculos deram {r1} {r2} {r3}')

#Escopo de variáveis
def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro recebe {a}')
    print(f'B dentro recebe {b}')
    print(f'C dentro recebe {c}')   
    '-------------------> escopo local'


a = 5 
'-----------> escopo global'
teste(a)
print(f'A fora recebe {a}')
#Prática

def fatorial(num=1):
    fact = 1
    print(f'5! = ',end='')
    for c in range(1,num+1):
        fact *= c
        print(c,end='')
        print(' x ' if c < num else '' ,end='')
    return fact
       


r1 = fatorial(6)
print(f' = {r1}')

