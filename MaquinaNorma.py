import re
import os
from Operacao import OperacaoDeAcao, OperacaoDeTeste
from Programa import Programa

class MaquinaNorma:
	def __init__(self):
		self.registradores: dict[str, int] = {}
		self.macros: dict[str, Programa] = {}
		self.debug: bool = False
		self.saida: str = ""

	def executar(self, texto_registradores: str, texto_programa: str) -> bool:
		self.__inicializar_registradores(texto_registradores)
		self.__load_macros()

		programa = Programa()
		programa.interpretar_programa_string("main", texto_programa)
		self.__executar_programa(programa)

		return True


	def __inicializar_registradores(self, texto_registradores: str):
		if len(texto_registradores) == 0:
			return

		linhas = texto_registradores.split(',')

		for linha in linhas:
			registrador_regex = re.search("^(\w+):[ ]*(\d+)$", linha.strip(), re.IGNORECASE)
			if registrador_regex is None:
				raise Exception(f"Registradores | A linha: \"{linha}\" não é válida")

			nome_registrador = registrador_regex.group(1)
			valor_registrador = int(registrador_regex.group(2))

			if self.debug:
				print(f"Atribuindo o valor {valor_registrador} ao registrador {nome_registrador}")

			self.registradores[nome_registrador] = valor_registrador


	def __load_macros(self):
		current_dir = os.path.dirname(os.path.realpath(__file__))
		macros_dir = os.path.join(current_dir, "macros")

		if not os.path.isdir(macros_dir):
			return

		for nome_arquivo in os.listdir(macros_dir):
			caminho_arquivo = os.path.join(macros_dir, nome_arquivo)
			if not os.path.isfile(caminho_arquivo) or not nome_arquivo.endswith(".txt"):
				continue

			with open(caminho_arquivo, 'r', encoding="utf-8") as arquivo:
				nome_macro = os.path.splitext(nome_arquivo)[0]

				linhas = arquivo.readlines()
				programa = Programa()
				programa.interpretar_programa(nome_macro, linhas)

				if self.debug:
					print(f"Macro {nome_macro} carregada")

				self.macros[nome_macro] = programa


	def __executar_programa(self, programa: Programa):
		if programa.rotulo_inicial is None:
			raise Exception(f"Rótulo inicial do programa não definido")

		proximo_rotulo = programa.rotulo_inicial

		while True:
			rotulo_atual = proximo_rotulo

			str_regs = ""
			for reg_name in self.registradores:
				if len(str_regs) > 0:
					str_regs += ", "
				str_regs += f"{self.registradores[reg_name]}"

			if len(self.registradores) > 1:
				str_regs = f"({str_regs})"

			self.saida += f"{programa.nome} | ({rotulo_atual}, {str_regs})\n"

			# Caso um rótulo inexistente seja encontrado é porque chegou ao fim do programa
			if rotulo_atual not in programa.operacoes:
				return

			operacao = programa.operacoes[rotulo_atual]
			if self.debug:
				print(f"Executando: {operacao}")

			if type(operacao) is OperacaoDeTeste:
				teste_regex = re.search("^zero_(\w+)$", operacao.teste, re.IGNORECASE)
				if teste_regex is None:
					raise Exception(f"Teste: \"{operacao.teste}\" não é válido. O teste deve iniciar com \"zero_\" e depois conter o nome do registrador. Ex: \"zero_a\"")

				nome_registrador = teste_regex.group(1)
				if self.__teste_registrador(nome_registrador):
					proximo_rotulo = operacao.rotulo_se_verdadeiro
				else:
					proximo_rotulo = operacao.rotulo_se_falso

			elif type(operacao) is OperacaoDeAcao:
				if add_regex := re.search("^add_(\w+)$", operacao.acao, re.IGNORECASE):
					nome_registrador = add_regex.group(1)
					self.__add_registrador(nome_registrador)

				elif sub_regex := re.search("^sub_(\w+)$", operacao.acao, re.IGNORECASE):
					nome_registrador = sub_regex.group(1)
					self.__sub_registrador(nome_registrador)

				elif operacao.acao in self.macros:
					programa_macro = self.macros[operacao.acao]
					self.__executar_programa(programa_macro)

				else:
					raise Exception(f"Operação {operacao.acao} não suportada. Utilize apenas: add_x, sub_x ou alguma macro")

				proximo_rotulo = operacao.rotulo_seguinte

			else:
				raise Exception(f"Operação {type(operacao)} não implementada")


	def __teste_registrador(self, nome_registrador):
		if nome_registrador not in self.registradores:
			#self.registradores[nome_registrador] = 0
			raise Exception(f"Registrador {nome_registrador} não definido")


		valor_registrador = self.registradores[nome_registrador]
		resultado = valor_registrador == 0

		if self.debug:
			print(f"teste_registrador {nome_registrador} = {valor_registrador} | resultado = {resultado}")

		return resultado

	def __add_registrador(self, nome_registrador):
		if nome_registrador not in self.registradores:
			#self.registradores[nome_registrador] = 0
			raise Exception(f"Registrador {nome_registrador} não definido")

		self.registradores[nome_registrador] += 1

		if self.debug:
			print(f"add_registrador {nome_registrador} | novo valor = {self.registradores[nome_registrador]}")

	def __sub_registrador(self, nome_registrador):
		if nome_registrador not in self.registradores:
			#self.registradores[nome_registrador] = 0
			raise Exception(f"Registrador {nome_registrador} não definido")

		self.registradores[nome_registrador] -= 1

		if self.debug:
			print(f"sub_registrador {nome_registrador} | novo valor = {self.registradores[nome_registrador]}")

	def exibir_registradores(self):
		for nome_registrador in self.registradores:
			print(f"{nome_registrador}: {self.registradores[nome_registrador]}")

