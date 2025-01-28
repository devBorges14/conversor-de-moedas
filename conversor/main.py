import customtkinter
from pegar_moedas import nomes_moedas, conversoes_disponiveis
from pegar_cotacoes import pegar_cotacao_moeda

# Criar e configurar janela
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
janela = customtkinter.CTk() # Criando a janela
janela.geometry("500x600") # Tamanho da janela 

dic_conversoes = conversoes_disponiveis() # Funcão para obter as moedas disponíveis da API

# Criar os botões, textos e outros elementos
titulo = customtkinter.CTkLabel(janela, text="Conversor de moedas", font=("", 25)) # Criando o titulo da janela
texto_moeda_de_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem") # Botão para a moeda de origem 
texto_quantidade_moeda_de_origem = customtkinter.CTkEntry(janela, placeholder_text="Quantidade para calcular") # Campo para a quantidade da moeda de origem
texto_moeda_de_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de destino") # Botão para a moeda de destino

def carregar_moedas_de_destino(moeda_selecionada): # Recarrega as moedas de destino quando uma moeda de origem é selecionada
    lista_moedas_destino = dic_conversoes[moeda_selecionada] # Obtendo as moedas de destino disponíveis para a moeda selecionada
    campo_moeda_de_destino.configure(values=lista_moedas_destino) # Atualizando as opções do menu
    campo_moeda_de_destino.set(lista_moedas_destino[0]) # Definindo a primeira opção como padrão

campo_moeda_de_origem = customtkinter.CTkOptionMenu(janela, values=list(dic_conversoes.keys()),
                                                    command=carregar_moedas_de_destino) # Botão para a moeda de origem
campo_moeda_de_destino = customtkinter.CTkOptionMenu(janela, values=["Selecione a moeda de origem"],) # Botão para a moeda de destino

def converter_moedas(): # Função para converter moedas
    moeda_origem = campo_moeda_de_origem.get() # Obtendo a moeda de origem selecionada e a moeda de destino
    moeda_destino = campo_moeda_de_destino.get()

    if moeda_origem and moeda_destino: # Verificando se ambas as moedas foram selecionadas
        numero = float(texto_quantidade_moeda_de_origem.get()) # Obtendo a quantidade da moeda de origem
        cotacao = pegar_cotacao_moeda
        try:
            quantidade = int(texto_quantidade_moeda_de_origem.get())
        except ValueError:
            # Handle the case where the user entered non-numeric text
            print("Please enter a valid number.")
            return
        resultado = numero * cotacao(moeda_origem, moeda_destino) # Faz o cauculo da cotação
        texto_cotacao.configure(text=f"{quantidade} {moeda_origem} = {resultado} {moeda_destino}") # Atualizando o texto da cotação 

botao_converter = customtkinter.CTkButton(janela, text="Converter", command=converter_moedas) # Botão para converter

# Scrollable Frame para listar moedas
lista_de_moedas = customtkinter.CTkScrollableFrame(janela)

texto_cotacao = customtkinter.CTkLabel(janela, text="")
# Obter dicionário de moedas disponíveis
moedas_disponiveis = nomes_moedas()

# Exibir cada moeda disponível
for codigo_moeda, nome_moeda in moedas_disponiveis.items():
    texto_moeda = customtkinter.CTkLabel(lista_de_moedas, text=f"{codigo_moeda}: {nome_moeda}")
    texto_moeda.pack()

# Colocar todos os elementos na tela
titulo.pack(padx=10, pady=10)
texto_moeda_de_origem.pack(padx=10, pady=3)
texto_quantidade_moeda_de_origem.pack(padx=10, pady=3)
campo_moeda_de_origem.pack(padx=10)
texto_moeda_de_destino.pack(padx=10, pady=3)
campo_moeda_de_destino.pack(padx=10)
botao_converter.pack(padx=10, pady=10)
texto_cotacao.pack(padx=10, pady=10)
lista_de_moedas.pack(padx=10, pady=10)

# Rodar Janela
janela.mainloop()
