import customtkinter
from pegar_moedas import nomes_moedas, conversoes_disponiveis

# Criar e configurar janela
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
janela = customtkinter.CTk()
janela.geometry("500x600")

dic_conversoes = conversoes_disponiveis()

# Criar os botões, textos e outros elementos
titulo = customtkinter.CTkLabel(janela, text="Conversor de moedas", font=("", 25))
texto_moeda_de_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem")
texto_moeda_de_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de destino")

def carregar_moedas_de_destino(moeda_selecionada):
    lista_moedas_destino = dic_conversoes[moeda_selecionada]
    campo_moeda_de_destino.configure(values=lista_moedas_destino)
    campo_moeda_de_destino.set(lista_moedas_destino[0])

campo_moeda_de_origem = customtkinter.CTkOptionMenu(janela, values=list(dic_conversoes.keys()),
                                                    command=carregar_moedas_de_destino)
campo_moeda_de_destino = customtkinter.CTkOptionMenu(janela, values=["Selecione a moeda de origem"],)

def converter_moedas():
    print("Converter")

botao_converter = customtkinter.CTkButton(janela, text="Converter", command=converter_moedas)

# Scrollable Frame para listar moedas
lista_de_moedas = customtkinter.CTkScrollableFrame(janela)

# Obter dicionário de moedas disponíveis
moedas_disponiveis = nomes_moedas()

# Exibir cada moeda disponível
for codigo_moeda, nome_moeda in moedas_disponiveis.items():
    texto_moeda = customtkinter.CTkLabel(lista_de_moedas, text=f"{codigo_moeda}: {nome_moeda}")
    texto_moeda.pack()

# Colocar todos os elementos na tela
titulo.pack(padx=10, pady=10)
texto_moeda_de_origem.pack(padx=10, pady=3)
campo_moeda_de_origem.pack(padx=10)
texto_moeda_de_destino.pack(padx=10, pady=3)
campo_moeda_de_destino.pack(padx=10)
botao_converter.pack(padx=10, pady=10)
lista_de_moedas.pack(padx=10, pady=10)

# Rodar Janela
janela.mainloop()
