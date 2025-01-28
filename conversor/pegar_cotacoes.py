import requests

def pegar_cotacao_moeda(moeda_origem, moeda_destino):
    link = f"https://economia.awesomeapi.com.br/last/{moeda_origem}-{moeda_destino}" # Link da API da Awesome
    requisicao = requests.get(link) # Fazendo o request

    cotacao = float(requisicao.json()[f"{moeda_origem}{moeda_destino}"]["bid"]) # Convertendo para float
    return cotacao

    
