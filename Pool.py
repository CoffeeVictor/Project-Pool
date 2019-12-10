from random import randint
from math import ceil
from opensimplex import OpenSimplex

class Pool:
	def __init__(self, n_linhas, n_colunas, largura, altura):
		self.ox_off = 0
		self.db_off = randint(10, 100)
		self.linhas = n_linhas
		self.colunas = n_colunas
		self.largura_total = largura
		self.altura_total = altura
		self.largura_tile = ceil(largura/n_colunas)
		self.altura_tile = ceil(altura/n_linhas)
		self.OxMatrix = [[0 for x in range(n_colunas)] for y in range(n_linhas)]
		self.DbMatrix = [[0 for x in range(n_colunas)] for y in range(n_linhas)]

	def update():
		noise = OpenSimplex()
		loff = 0
		self.ox_off += 0.05
		for linha in range(self.n_linhas):
			coff = 0
			for coluna in range(self.n_colunas):
				self.OxMatrix[linha][coluna] = noise.noise3d(x = coff, y = loff, z = self.ox_off)
				coff += 0.2
			loff += 0.2
