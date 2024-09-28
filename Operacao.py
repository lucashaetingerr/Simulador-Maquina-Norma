class Operacao:
	def __init__(self, rotulo):
		self.rotulo = int(rotulo)

class OperacaoDeAcao(Operacao):
	def __init__(self, rotulo, acao, rotulo_seguinte):
		super().__init__(rotulo)
		self.acao = acao
		self.rotulo_seguinte = int(rotulo_seguinte)

	def __str__(self):
		return f"rotulo = {self.rotulo} | acao = {self.acao} | rotulo_seguinte = {self.rotulo_seguinte}"

class OperacaoDeTeste(Operacao):
	def __init__(self, rotulo, teste, rotulo_se_verdadeiro, rotulo_se_falso):
		super().__init__(rotulo)
		self.teste = teste
		self.rotulo_se_verdadeiro = int(rotulo_se_verdadeiro)
		self.rotulo_se_falso = int(rotulo_se_falso)

	def __str__(self):
		return f"rotulo = {self.rotulo} | teste = {self.teste} | rotulo_se_verdadeiro = {self.rotulo_se_verdadeiro} | rotulo_se_falso = {self.rotulo_se_falso}"