# Finamove

## É uma API desenvolvida para realizar a conferência de um arquivo CNAB, ler os dados contidos, tratar e adicionar essas informações a um banco de dados.

## Tecnologias
- Python 3.10.4 (https://www.python.org/)
- Django Rest Framework (https://www.django-rest-framework.org/)
- Django (https://www.djangoproject.com/)
- Gerenciador de pacotes PIP (https://pip.pypa.io/en/stable/)

## Funcionalidades
Recebe um arquivo .txt com os dados em formato CNAB e através dele automaticamente realiza:
- Cadastro das lojas
- Cadastro de donos de loja
- Difere os tipos de operações realizada
- Balanços de caixa (saldo em caixa)
- Retorna uma lista com os dados das movimentações no ato do envio do arquivo
- Por uma rota específica (veja o exemplo de requisições) retorna as lojas e suas informações, incluindo saldo em caixa
- Os dados gerados serão guardados no banco de dados SQLite3 gerado dentro do diretório no arquivo `db.sqlite3`.

## Passo a passo para executar esta API em localhost
Considerando que você já possui o Python instalado com o gerenciador de pacotes PIP, faça o seguinte:
- Faça o clone deste repositório utilizando o comando `$ git clone https://github.com/jhonmullerfreitas/finamove.git`
- Em seguida, dentro do diretório (pasta) baixado inicie seu ambiente virtual com o comando `$ python -m venv venv`
- Logo após, inicialize o ambiente virtual com o comando `$ source venv/bin/activate` (obs. este passo é importante para que você não realize instalação das tecnologias de forma global e resulte em conflitos na sua máquina)
- Agora execute a instalação das bibliotecas necessárias para a execução do projeto com o comando `$ pip install -r requirements.txt`
- Rode as migrations com estes dois comandos `$ python manage.py makemigrations` depois `$ python manage.py migrate`
- Execute o servidor `$ python manage.py runserver`
- Faça suas requisições com um cliente HTTP como o Insomnia (https://insomnia.rest/download) ou Postman (https://www.postman.com/)

## Endpoits da API
Esta API é executada em localhost (http://127.0.0.1:8000)

- http://127.0.0.1:8000/api/movement/ (POST)
- http://127.0.0.1:8000/api/stores/ (GET)

## Exemplos de requisições

OBS. Para enviar (POST) um arquivo, seu app de requisição HTTP (Insomnia ou Postman) deve estar configurado para estrutura `Multipart Form` assim você poderá definir uma chave de requisição `document` e escolher na opção `file` o `arquivo.txt` que deseja enviar.

## Cadastrar um arquivo CNAB

<table>
  <tr>
    <th>Verbo HTTP</th>
    <th>Endpoint</th>
    <th>Body</th>
    <th>Retorno</th>
  </tr>
  <tr>
    <td>POST</td>
    <td>http://127.0.0.1:8000/api/movement/</td>
    <th>"document": "file" (veja a observação acima)</th>
    <td>Dados do CNAB tratados com informações sobre as movimentações, donos de loja, valores, cartões e tipos de operações</td>
  </tr>
</table>


## Listar lojas
<table>
  <tr>
    <th>Verbo HTTP</th>
    <th>Endpoint</th>
    <th>Body</th>
    <th>Retorno</th>
  </tr>
  <tr>
    <td>GET</td>
    <td>http://127.0.0.1:8000/api/stores/</td>
    <th>No body</th>
    <td>Retorna os dados das lojas como: nome, saldo e dono.</td>
  </tr>
</table>


## Contato

Qualquer dúvida você pode entrar em contato comigo no email: jmuller.jhon80@gmail.com





