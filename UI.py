#Definiçoes da janela e seus componentes
import tkinter as tk


def execucao():
    
    root=tk.Tk()
    root.title("Computabilidade - Grupo M")
    root.configure(bg="#f0f0f0")
    root.geometry("800x600") 
    root.resizable(False, False) 
    quadro_principal=tk.Frame(root, bg="#f0f0f0")
    quadro_principal.pack(expand=True)
    rotulo_titulo=tk.Label(quadro_principal, text="Computabilidade - Grupo M",bg="#f0f0f0", font=("Arial",24))
    rotulo_titulo.pack(pady=20)
    rotulo_a=tk.Label(quadro_principal, text="Insira os registradores, separando-os por vírgula:", bg="#f0f0f0", font=("Arial", 14))
    rotulo_a.pack(anchor='w', padx=20)
    entrada_a=tk.Entry(quadro_principal, width=80, font=("Arial", 14))
    entrada_a.pack(pady=5, padx=20)
    rotulo_b=tk.Label(quadro_principal, text="Entradas:", bg="#f0f0f0", font=("Arial", 14))
    rotulo_b.pack(anchor='w',padx=20)
    entrada_comandos=tk.Text(quadro_principal, height=5, width=80, font=("Arial", 14))
    entrada_comandos.pack(pady=5,padx= 20)
    quadro_botoes=tk.Frame(quadro_principal, bg="#f0f0f0")
    quadro_botoes.pack(pady=20)
    botao_enviar=tk.Button(quadro_botoes, text="Enviar", font=("Arial", 14), width=15, bg="green", fg="white")
    botao_enviar.pack(side=tk.LEFT,padx=10)
    botao_cancelar=tk.Button(quadro_botoes, text="Cancelar", font=("Arial", 14), width=15)
    botao_cancelar.pack(side=tk.LEFT, padx=10)
    console_saida=tk.Text(quadro_principal, height=15, width=80, font=("Arial", 12), state=tk.DISABLED)
    console_saida.pack(pady=20, padx=20)


    def adicionar_ao_console(texto):
        console_saida.config(state=tk.NORMAL)
        console_saida.insert(tk.END, texto+"\n")
        console_saida.see(tk.END)
        console_saida.config(state=tk.DISABLED)


    adicionar_ao_console("Insira os comandos a serem processados e clique em 'enviar' para iniciar o processamento.")
    root.mainloop()


#execucao()
