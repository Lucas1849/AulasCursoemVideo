def fatorial(n):
    fat = 1
    for c in range(1,n+1):
        fat *= c
    return fat


cores = [ '\033[m'  ,     #0 - sem cor
          '\033[0;30;41m',#1 - vermelho
          '\033[0;30;42m',#2 - verde
          '\033[0;30;43m',#3 - amarelo
          '\033[0;30;44m',#4 - azul
          '\033[0;30;45m',#5 - roxo
          '\033[7;30m'    #6 - branco
]