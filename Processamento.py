from MaquinaNorma import MaquinaNorma


def executar_programa(texto_registradores, texto_programa):
    maquina = MaquinaNorma()
    maquina.executar(texto_registradores, texto_programa)
    return maquina.saida

# Teste
# texto_registradores = "a: 0, b: 5"
# texto_programa = "1: se zero_b então vá_para 5 senão vá_para 2\n2: faça add_a vá_para 3\n3: faça add_a vá_para 4\n4: faça sub_b vá_para 1\n5: faça zerar_a vá_para 9"
# executar_programa(texto_registradores, texto_programa)