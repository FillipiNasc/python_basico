#Criando função em python com o def
def par(num):
	if(num %2 == 0):
		return True
	return False
print(par(2))
print(par(3))

#Potenciacao
def pot2(x):
	return x**2
print(pot2(5))

#Fatorial
def fat(n):
	if(n == 0):
		return 1
	return (n*fat(n-1))
print(fat(5))

#Fibonacci
def fib(n):
	if(n == 1 or n == 2):
		return 1
	return fib(n-1) + fib(n-2)
print(fib(5))

#Potenciacao
def pot(base, exp):
	if(exp==0):
		return 1
	return base * pot(base, exp-1)
print(pot(2,10))
