import tkinter as tk
from random import randint


def rolar_d20():
    #Faz o sorteio entre 1 e 20 (assim como um d20 padrão...)
    resultado = randint(1, 20)

    #Atualiza o texto na tela
    label_resultado.config(text=str(resultado))

    #Para Sucesso e Falha Crítica
    if resultado == 20:
        label_mensagem.config(text="CRÍTICO!!!!".upper(), fg="green")
    elif resultado == 1:
        label_mensagem.config(text="FALHA CRÍTICA!".upper(), fg="red")
    else:
        label_mensagem.config(text="Rolagem concluída", fg="black")


#Janela principal
janela = tk.Tk()
janela.title("Simulador D20")
janela.geometry("600x500")
janela.configure(padx=100, pady=100)

#Título
titulo = tk.Label(janela, text="Dado de 20 Faces", font=("Arial", 16, "bold"))
titulo.pack(pady=10)

#Número do Resultado
label_resultado = tk.Label(
    janela, text="-", font=("Arial", 36, "bold"), fg="black"
)
label_resultado.pack(pady=10)

#Mensagem de Crítico e Falha
label_mensagem = tk.Label(janela, text="", font=("Arial", 10))
label_mensagem.pack(pady=5)

#O Botão para rolar
botao_rolar = tk.Button(
    janela,
    text="🎲 Rolar Dado",
    font=("Arial", 12, "bold"),
    command=rolar_d20,  # Chama a função quando clicado
    bg="#B81717",
    fg="white",
    padx=15,
    pady=10,
)
botao_rolar.pack(pady=10)

# Rodar o programa em janela
janela.mainloop()