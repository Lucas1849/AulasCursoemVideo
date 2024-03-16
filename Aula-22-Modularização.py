import úteis
#from úteis import fatorial


fnum = int(input('Digite um número: '))
for c in range(1,fnum+1):
    print(f'{c}',end='')
    print(' x ' if c < fnum else ' = ',end='')
print(úteis.fatorial(fnum))