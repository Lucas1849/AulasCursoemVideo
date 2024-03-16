'Listas compostas'

pessoas = ['Leonardo',18,'Gabriel',19,'Maria',19,'Lucas',18]
registro = []
registro.append(pessoas[:])
#Outra forma de adicionar listas dentro de listas
'registro = [[Leonardo, 18], [Gabriel,19], [Maria,19], [Lucas,18]]'
#Usando cópias
teste = []
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 19
galera.append(teste[:])

