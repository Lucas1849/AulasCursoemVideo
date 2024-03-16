#Estrutura Try e Except
try:
    a = int(input('Digite um número: '))
    b = int(input('Digite um número: '))
    d = a/b
except Exception as erro:
    print(f'O problema encontrado foi {erro.__class__}')
else:
    print(d)
finally:
    print('Volte sempre!')