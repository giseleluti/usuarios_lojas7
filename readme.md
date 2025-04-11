# API de Gerenciamento de Usuários

## Propósito

Esta API RESTful foi desenvolvida para gerenciar o cadastro e autenticação de usuários. Ela oferece funcionalidades para criar, buscar, atualizar e deletar usuários, além de autenticar usuários existentes.

## Especificação

A API foi construída usando Flask (Python) e utiliza SQLite para persistência de dados. A documentação da API está disponível no Swagger UI, acessível em `http://127.0.0.1:5002/swagger` após a execução da aplicação.

## Requisitos

* Python 3.9 ou superior
* Pip (gerenciador de pacotes do Python)
* Docker (opcional, para execução em contêiner)

## Dependências

As seguintes bibliotecas Python são necessárias para executar a API:

* Flask
* flask-swagger-ui
* validate-docbr
* validators

## Instalação

1.  Clone o repositório.
e depois acesse em

    ```bash
    cd <usuarios_lojas7>
    ```

2.  Crie um ambiente virtual (opcional, mas recomendado):

    ```bash
    python -m venv venv
    ```

3.  Ative o ambiente virtual:

    * No Windows:

        ```bash
        venv\Scripts\activate
        ```

    * No macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4.  Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

## Execução

1.  Execute a aplicação:

    ```bash
    python app.py
    ```


Construa a imagem Docker:
Bash
Copiar o código
docker build -t usuarios_lojas7 .
3. 
Execute o container:
Bash
Copiar o código
docker run -p 5002:5002 usuarios_lojas7 
4. 
Acesse a aplicação em http://localhost:5002/swagger
