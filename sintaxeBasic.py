# Sitaxes Basicas de python
#inteiros
x = 1
#string
nome = 'Python'
#float
y = 3.14

#Print comando que imprimi na tela

print(x, type(x)) #type para descobri o tipo da variavel
print(nome, type(nome), len(nome))
print(y, type(y))


#comentario de uma linhs "#"
"""
comentario de mutiplas linhas
"""
"""
Listas podem ser alteradas pois sao mutavel
Tuplas nao podem ser alteradas pois sao imutavel
Dicionarios podem ser alterados pois sao mutavel
OBS: Dicionarios trabalham com chaves
"""
#Criando uma lista []
lista = [1, 3.14, 'Python']

#Criando uma Tupla ()
tupla = (1, 3.14,'Python')

#Criando um dicionario {} com o separador :
dicionario = {'idade':34, 'nota':7.5, 'aluno':'Python'}

print(lista, type(lista), len(lista))
print(tupla, type(tupla), len(tupla))
print(dicionario, type(dicionario), len(dicionario))

#Condicional
nota = 10
if (nota % 2 == 0): #% resto da divisao
	print('Numero e par!')
else:
	print('Numero e impar!')
#Laço de repetiçao while
numero = 0
while (numero<11):
	print(numero)
	numero = numero+1
#Laço de repetiçao for
for dic in dicionario:
	print(dicionario[dic])
