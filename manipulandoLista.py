#Manipulacao de listas

#Concartenando listas
lista1 = [1,2,3,4]
lista2 = [5,6,7,8,9]
print(lista1+lista2)

#Usando o pop para remover elementos da lista pela posicao
lista = [1,2,3,4,5,6,7]
print(len(lista)) #len ver o tamanho da lista
lista.pop(0)
lista.pop(len(lista) - 1)
print(lista)

#Usando o remove para remover elementos da lista pelo elemento
lisremove = [1,2,3,'oi',4,5,6]
lisremove.remove('oi')
print(lisremove)

#Ver se elemento existe na lista
num = 10
lisver = [1,2,3,4,5,6]
if num in lisver:
	print('Elemento encontrado')
else:
	print('Elemento nao encontrado')

#Interando elementos da lista
lista = [1,2,3,4,5]
for i in lista:
	print(i)
#Transformando uma lista em tupla
t_lista = tuple(lista)
print(type(t_lista))

#Iserindo elemento em uma determinada posicao de uma lista
lista.insert(1,10)
print(lista)
lista.insert(len(lista),20)
print(lista)

#Ordenando a lista
lista.sort()
print(lista)

#Usando slice
print(lista[0]) #0 pega o primeiro elemento
print(lista[-1]) #-1 pega o ultimo elemento
print(lista[::-1]) #::1 inverte a lista
print(lista[::1]) #::1 imprime a lista normal
