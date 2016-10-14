#Sobre o modulo random

import random

#Retorna um numeros aleatorio
print(random.randint(1, 10))
print(random.randrange(10))

#Escolher um elemento de uma lista aleatorio
lista = [1,2,3,4]
print(random.choice(lista))
#Embaralha a sequancia
random.shuffle(lista)
print(lista)
#Pegar uma quantidade de elementos de uma lista
print(random.sample(lista,2))
