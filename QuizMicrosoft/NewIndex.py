import tkinter as tk
from tkinter import PhotoImage
import pandas as pd
import random
from PIL import Image, ImageTk

df = pd.read_excel('QuizManeiro.xlsx')  # Puxa o arquivo Excel
questoes = df.sample(n=10).values.tolist()  # Puxando as perguntas aleatoriamente da tabela

# Variáveis Globais
pontuacao = 0
lista_atual = 0  # A pergunta atual a ser mostrada

# ============================ Funções =================================

def exibir_pergunta():
    global lista_atual
    Questao, op1, op2, op3, op4, resposta = questoes[lista_atual]  # Pega a primeira lista das questões do arquivo dados (excel)
    pergunta.config(text=Questao)

    opcao1.config(text=op1, state=tk.NORMAL, command=lambda: verificar_resposta(1, resposta))
    opcao2.config(text=op2, state=tk.NORMAL, command=lambda: verificar_resposta(2, resposta))
    opcao3.config(text=op3, state=tk.NORMAL, command=lambda: verificar_resposta(3, resposta))
    opcao4.config(text=op4, state=tk.NORMAL, command=lambda: verificar_resposta(4, resposta))

def verificar_resposta(opcao_selecionada, resposta_correta):
    global pontuacao, lista_atual
    
    if opcao_selecionada == resposta_correta:
        pontuacao += 1

    lista_atual += 1

    if lista_atual < len(questoes):
        exibir_pergunta()
    else:
        mostrar_result()

def jogar_denovo():
    global pontuacao, lista_atual
    
    # Resetar variáveis
    pontuacao = 0
    lista_atual = 0

    # Reabilitar as opções
    opcao1.config(state=tk.NORMAL)
    opcao2.config(state=tk.NORMAL)
    opcao3.config(state=tk.NORMAL)
    opcao4.config(state=tk.NORMAL)

    # Esconder a tela de resultado
    tela_final.destroy()

    # Iniciar o quiz novamente
    exibir_pergunta()

def mostrar_result():
    global tela_final
    # Cria uma nova janela para mostrar o resultado
    tela_final = tk.Tk()
    tela_final.title('Ao Infinito e Allen!')  # Título da janela
    tela_final.rowconfigure(0, weight=1)
    tela_final.columnconfigure(0, weight=1)
    tela_final.geometry(tamanho)
    tela_final.config(bg=cor_fundo)  # Cor do background
    tela_final.option_add('*Font', 'Arial')

    # Imagem da tela de resultado


    # Mostrar a pontuação
    resultado_texto = f"Pontuação: {pontuacao} / {len(questoes)}"
    resultado_label = tk.Label(tela_final, text=resultado_texto, bg=cor_fundo, fg=cor_texto, font=('Arial', 20, 'bold'))
    resultado_label.pack()

    # Botão para jogar novamente
    jogar = tk.Button(tela_final, command=jogar_denovo, text='Jogar Novamente', width=25, bg=cor_botao, fg=cor_buton, font=('Arial', 17, 'bold'))
    jogar.pack(pady=10)  # Usando pack para centralizar e ajustar o botão

# =====================================================================

# Configuração do dimensionamento da tela do quiz
quizur = tk.Tk()

quizur.title('Quiz Allen do conhecimento!')  # Título da janela
quizur.rowconfigure(0, weight=1)
quizur.columnconfigure(0, weight=1)

tamanho = '1100x550'
quizur.geometry(tamanho)  # Definição das dimensões da janela

# Cores gerais
cor_fundo = "#e6f0ff"
cor_botao = "#b4b2f2"
cor_texto = '#000000'
cor_buton = '#ffffff'

# Cores e fonte do quiz
quizur.config(bg=cor_fundo)  # Cor do background
quizur.option_add('*Font', 'Arial')

# Imagem da tela, logo do milhão
icone = PhotoImage(file="caricatura.png")

# Cria o Label para exibir a imagem e posiciona à esquerda
position = tk.Label(quizur, image=icone, bg=cor_fundo)
position.place(x=0, y=-110)  # Posiciona à esquerda da janela 

# Componentes da interface visual
pergunta = tk.Label(quizur, text='', wraplength=600, bg=cor_fundo, fg=cor_texto, font=('Arial', 20, 'bold'), justify='left')
pergunta.place(x=510, y=85)

opcao1 = tk.Button(quizur, text='', width=40, bg=cor_botao, fg=cor_buton, state=tk.DISABLED, font=('Arial', 15, 'bold'))
opcao1.place(x=510, y=200)

opcao2 = tk.Button(quizur, text='', width=40, bg=cor_botao, fg=cor_buton, state=tk.DISABLED, font=('Arial', 15, 'bold'))
opcao2.place(x=510, y=260)

opcao3 = tk.Button(quizur, text='', width=40, bg=cor_botao, fg=cor_buton, state=tk.DISABLED, font=('Arial', 15, 'bold'))
opcao3.place(x=510, y=320)

opcao4 = tk.Button(quizur, text='', width=40, bg=cor_botao, fg=cor_buton, state=tk.DISABLED, font=('Arial', 15, 'bold'))
opcao4.place(x=510, y=380)

# Iniciar o quiz
exibir_pergunta()

quizur.mainloop()
