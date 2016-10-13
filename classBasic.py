class Pessoa: #Pessoa e um objeto
	def __init__(self, nome, idade): #init metodo construtor
		self.nome=nome
		self.idade=idade
	def obterNome(self):
		return self.nome
	def obterIdade(self):
		return self.idade
	def setNome(self, nome):
		self.nome=nome
	def setIdade(self, idade):
		self.idade=idade

p = Pessoa('Python', 10)
print('Nome: %s' % p.obterNome())
print('Idade: %d' % p.obterIdade())
p.setIdade(20) #funcao setIdade para alterar a idade
print('Idade: %d' % p.obterIdade())
#Exemplo de lista com objeto
p1 = Pessoa('Maria', 20)
p2 = Pessoa('Joao', 22)
p3 = Pessoa('Carlos', 30)

pessoas = [] #lista vazia
pessoas.append(p1) #Append para adicionar no final da lista
pessoas.append(p2)
pessoas.append(p3)

for pessoa in pessoas:
	print(pessoa.obterNome())
