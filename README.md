# Conversor de moedas
Este projeto é um Conversor de Moedas simples, desenvolvido utilizando a biblioteca customtkinter para criar uma interface gráfica com o usuário (GUI). A aplicação permite ao usuário selecionar uma moeda de origem e uma moeda de destino, e com base nessas seleções, o valor em uma moeda será convertido para a outra.

# Tecnologias
- customtkinter
- Python
- os
- requests
- xmltodict

# PRÉ REQUISTOS
1) Instale Python3 (https://www.python.org/downloads/)
![image](https://github.com/user-attachments/assets/0ded5cf5-4d7d-4fe6-96ca-42eee8fce90e)

2) No arquivo pegar_moedas (nas linhas 4 á 6) Troque o caminho dos arquivos .xml
````
# Caminho absoluto dos arquivos
file_path_moedas = r'E:\\Projetos maiores\\API\\projeto\\moedas.xml'
file_path_conversoes = r'E:\\Projetos maiores\\API\\projeto\\conversoes.xml'
````
3) Instale as dependências:
PARA INSTALAMENTO GERAL USE:
````pip install -r requirements.txt````

As dependências necessárias para o funcionamento do código são:
customtkinter: Para o GUI em python.
  - Instalação: ````pip install customtkinter````
requests: Para requisição da API (<a href="https://docs.awesomeapi.com.br/api-de-moedas">API da Awesome<a>)
  - Instalação: ````pip install requests````
xmltodict: Para modificar e visualizar arquivos .xml
  - Instalação: ````pip install xmltodict````
os: Para gerenciar arquivos. Geralmente já está incluído com a instalação padrão do Python.
Além disso, o código utiliza módulo internos do Python, como ````os````.

# Como Rodar
1. Clone o repositório:
  git clone https://github.com/devBorges14/conversor-de-moedas
2. Instale os prés requisitos
3. Execute o programa:
   ````bash python main.py````

- <a href="https://docs.awesomeapi.com.br/api-de-moedas">API da Awesome<a>
  - <a href="https://github.com/TomSchimansky/CustomTkinter">CustomTkinter .doc<a>
