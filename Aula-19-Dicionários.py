pessoas = {'nome': 'Lucas', 'Sexo': 'M', 'Idade': 18}
print(f'O {pessoas["nome"]} tem {pessoas["Idade"]} anos')
print(pessoas.items())
print(pessoas.values())
print(pessoas.keys())
for k, v in pessoas.items():
    print(f'{k} = {v}')

Brasil = []
estado1 = {'Uf': 'Rio de Janeiro','Sigla': 'Rj', }
estado2 = {'Uf': 'Brasília', 'Sigla': 'Bsp'}
Brasil.append(estado1)
Brasil.append(estado2)
print(Brasil)

estado = {}
Brasil = []
for c in range(0,3):
    estado['Uf'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    Brasil.append(estado.copy())
print(Brasil)