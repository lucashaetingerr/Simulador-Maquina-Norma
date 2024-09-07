import re

from Operacao import Operacao, OperacaoDeAcao, OperacaoDeTeste

class Programa:
	def __init__(self):
		self.nome: str = ""
		self.operacoes: dict[int, Operacao] = {}
		self.rotulo_inicial: int | None = None

	def interpretar_programa_string(self, nome: str, programa: str):
		linhas = programa.split('\n')
		self.interpretar_programa(nome, linhas)

	def interpretar_programa(self, nome: str, linhas: list[str]):
		self.nome = nome
		self.operacoes = {}
		self.rotulo_inicial = None

		for linha in linhas:
			# Remover espaços no início e fim da linha
			linha = linha.strip()
   
			# Identificar comentários e ignorá-los
			if linha.startswith("#") or len(linha) == 0:
				continue

			operacao = self.__interpretar_linha(linha)
			if operacao is None:
				raise Exception(f"Programa {nome} | A linha: \"{linha}\" não é válida")

			# Verificar rótulos repetidos
			if operacao.rotulo in self.operacoes:
				raise Exception(f"Programa {nome} | O rótulo {operacao.rotulo} está repetido no programa")

			self.operacoes[operacao.rotulo] = operacao

			if self.rotulo_inicial is None:
				self.rotulo_inicial = operacao.rotulo

	def __interpretar_linha(self, linha: str) -> Operacao | None:     
		teste_regex = re.search("^(\d+): se (\w+) ent(?:ã|a)o v(?:á|a)_para (\d+) sen(?:ã|a)o v(?:á|a)_para (\d+)$", linha, re.IGNORECASE)
		if teste_regex:
			rotulo = teste_regex.group(1)
			teste = teste_regex.group(2)
			rotulo_se_verdadeiro = teste_regex.group(3)
			rotulo_se_falso = teste_regex.group(4)
			operacao = OperacaoDeTeste(rotulo, teste, rotulo_se_verdadeiro, rotulo_se_falso)
			return operacao

		teste_acao = re.search("^(\d+): fa(?:ç|c)a (\w+) v(?:á|a)_para (\d+)$", linha, re.IGNORECASE)
		if teste_acao:
			rotulo = teste_acao.group(1)
			acao = teste_acao.group(2)
			rotulo_seguinte = teste_acao.group(3)
			operacao = OperacaoDeAcao(rotulo, acao, rotulo_seguinte)
			return operacao

		return None