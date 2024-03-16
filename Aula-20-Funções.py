#Criação de 'Rotinas' para otimizar meus programas 
def titulo(msg):
    print('-='*30)
    print(F"{msg:^60}")
    print('-='*30)


titulo("CURSO EM VÍDEO PYTHON")


def contador(*num):
    cont = len(num)
    print(f'Foram registrados {cont} valores.')


contador(8,2,3,5,7,4,2,5,7,4,2,5,7,5,3,2,12,5,6,7,5,4,33,)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(lst)
        
valores = [7,5,7,5,3,3,6,7,4,3,6,7,]
dobra(valores)
