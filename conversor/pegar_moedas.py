import xmltodict
import os

# Caminho absoluto dos arquivos
file_path_moedas = r'E:\\conversor\\moedas.xml'
file_path_conversoes = r'E:\\conversor\\moedas.xml' 

def nomes_moedas():
    with open(file_path_moedas, 'rb') as arquivo_moedas:
        dic_moedas = xmltodict.parse(arquivo_moedas)

    moedas = dic_moedas['xml']
    return moedas

def conversoes_disponiveis():
    with open(file_path_conversoes, 'rb') as arquivo_conversoes:
        dic_conversoes = xmltodict.parse(arquivo_conversoes)
    conversoes = dic_conversoes['xml']
    dic_conversoes = {}
    for par_conversao in conversoes:
        moeda_origem, moeda_destino = par_conversao.split('-')
        if moeda_origem in dic_conversoes:
            dic_conversoes[moeda_origem].append(moeda_destino)
        else:
            dic_conversoes[moeda_origem] = [moeda_destino]
    
    return dic_conversoes
