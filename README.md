
# Conversor de Moedas

Este projeto é um **Conversor de Moedas** desenvolvido em Python, utilizando a biblioteca **CustomTkinter** para criar uma interface gráfica de usuário (GUI). Ele permite ao usuário selecionar uma moeda de origem e uma moeda de destino e, com base nas seleções, realizar a conversão de valores entre as moedas. 

## Funcionalidades
- Seleção de moedas de origem e destino.
- Interface gráfica interativa.
- Conversões baseadas em dados de arquivos `.xml` ou de uma API externa.

---

## Tecnologias Utilizadas
- **Python**: Linguagem principal do projeto.
- **CustomTkinter**: Para criar a GUI.
- **Requests**: Para requisições de dados de APIs.
- **Xmltodict**: Para manipulação e leitura de arquivos `.xml`.
- **Os**: Para gerenciar caminhos de arquivos.

---

## Pré-Requisitos

Antes de executar o projeto, certifique-se de ter as ferramentas necessárias instaladas:

1. **Python 3+**  
   - Faça o download em [python.org/downloads](https://www.python.org/downloads/).  
   Após a instalação, verifique se o Python foi instalado corretamente:
   ```bash
   python --version
   ```
   ou
   ```bash
   python3 --version
   ```

2. **Dependências Python**  
   Instale as dependências listadas no arquivo `requirements.txt` com o comando:  
   ```bash
   pip install -r requirements.txt
   ```

   **Ou instale manualmente:**  
   - **CustomTkinter**: Biblioteca para interface gráfica.
     ```bash
     pip install customtkinter
     ```
   - **Requests**: Para chamadas de API.
     ```bash
     pip install requests
     ```
   - **Xmltodict**: Para manipulação de XML.
     ```bash
     pip install xmltodict
     ```
   - **Os**: Gerenciamento de arquivos (já incluso no Python).

3. **Configuração de Caminhos para Arquivos XML**  
   No arquivo `pegar_moedas.py` (linhas 4 a 6), atualize os caminhos dos arquivos XML para corresponder à localização dos arquivos em sua máquina. Exemplo:
   ```python
   # Caminho absoluto dos arquivos
   file_path_moedas = r'E:\\Projetos maiores\\API\\projeto\\moedas.xml'
   file_path_conversoes = r'E:\\Projetos maiores\\API\\projeto\\conversoes.xml'
   ```
---
## Como Rodar o Projeto

1. **Clone este repositório**:
   ```bash
   git clone https://github.com/devBorges14/conversor-de-moedas
   cd conversor-de-moedas
   ```

2. **Instale os pré-requisitos** conforme listado acima.

3. **Execute o programa**:
   ```bash
   python main.py
   ```

---

## Recursos Adicionais

- [Documentação da API Awesome Moedas](https://docs.awesomeapi.com.br/api-de-moedas)  
- [CustomTkinter Documentation](https://github.com/TomSchimansky/CustomTkinter)

---

## Estrutura do Projeto

```plaintext
├── conversor/ # Pasta para os arquivos
  ├── main.py                 # Arquivo principal da aplicação
  ├── pegar_moedas.py         # Código para manipulação de moedas e conversões
  ├── moedas.xml              # Arquivo XML com os nomes e códigos das moedas
  ├── conversoes.xml          # Arquivo XML com as taxas de conversão
├── requirements.txt        # Lista de dependências do projeto
└── README.md               # Documentação do projeto
```

---

## Licença
Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

--- 

### Observação
Certifique-se de que os arquivos XML estejam no caminho correto e atualizados antes de executar o programa. Caso deseje utilizar dados de API ao invés de XML, ajuste o código em `````pegar_moedas.py````` para fazer a requisição diretamente.
---
