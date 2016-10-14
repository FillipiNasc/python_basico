#Heranças
class Transporte:
	def __init__(self, nome, peso, preco):
		self.nome = nome
		self.peso = peso
		self.preco = preco
	def getNome(self):
		return self.nome
	def getPeso(self):
		return self.peso
	def getPreco(self):
		return self.preco
	def setNome(self,nome):
		self.nome = nome

class Carro(Transporte):
	def __init__(self, nome, peso, preco, seguro):
		Transporte.__init__(self, nome, peso, preco)
		self.seguro = seguro
	def getSeguro(self):
		return self.seguro

carro = Carro('Fusca', 300, 3500.00, 800.00)
print(carro.getNome())
print(carro.getPeso())
print(carro.getPreco())
print(carro.getSeguro())
