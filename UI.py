#Processamento
import Processamento as Processamento

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
    rotulo_a=tk.Label(quadro_principal, text="Insira os registradores, separando-os por vírgula. Exemplo: a: 1, b: 2", bg="#f0f0f0", font=("Arial", 14))
    rotulo_a.pack(anchor='w', padx=20)
    entrada_a=tk.Entry(quadro_principal, width=80, font=("Arial", 14))
    entrada_a.pack(pady=5, padx=20)
    rotulo_b=tk.Label(quadro_principal, text="Insira os códigos do programa, separando-os com ENTER", bg="#f0f0f0", font=("Arial", 14))
    rotulo_b.pack(anchor='w',padx=20)
    entrada_comandos=tk.Text(quadro_principal, height=5, width=80, font=("Arial", 14))
    entrada_comandos.pack(pady=5,padx= 20)
    quadro_botoes=tk.Frame(quadro_principal, bg="#f0f0f0")
    quadro_botoes.pack(pady=20)
    botao_enviar=tk.Button(quadro_botoes, text="Enviar", font=("Arial", 14), width=15, bg="green", fg="white", command=lambda:enviar())
    botao_enviar.pack(side=tk.LEFT,padx=10)
    botao_cancelar=tk.Button(quadro_botoes, text="Cancelar",font=("Arial", 14), width=15, command=lambda:cancelar())
    botao_cancelar.pack(side=tk.LEFT, padx=10)
    console_saida=tk.Text(quadro_principal, height=15, width=80,font=("Arial", 12), state=tk.DISABLED)
    console_saida.pack(pady=20, padx=20)


    def adicionar_ao_console(texto):
        console_saida.config(state=tk.NORMAL)
        console_saida.insert(tk.END, texto+"\n")
        console_saida.see(tk.END)
        console_saida.config(state=tk.DISABLED)
        
    adicionar_ao_console("Preencha os campos acima e clique em 'enviar' para iniciar o processamento.")
        
        
    def enviar():
        try:
            texto_registradores=entrada_a.get()
            texto_programa=entrada_comandos.get("1.0", tk.END).strip()
            limpar_console()
            saida=Processamento.executar_programa(texto_registradores, texto_programa)
            adicionar_ao_console(str(saida))
            
        except Exception as e:
            limpar_console()
            adicionar_ao_console("Encontramos um erro ao processar os dados fornecidos no formato indicado.")



    def cancelar():
        entrada_a.delete(0,tk.END)
        entrada_comandos.delete("1.0",tk.END)
        limpar_console()
        adicionar_ao_console("Preencha os campos acima e clique em 'enviar' para iniciar o processamento.")
        
        
    def limpar_console():
        console_saida.config(state=tk.NORMAL)
        console_saida.delete("1.0",tk.END)
        console_saida.config(state=tk.DISABLED)


    root.mainloop()

#execucao()