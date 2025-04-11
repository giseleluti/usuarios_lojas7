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

Flask
flask-swagger-ui
validate-docbr
validators

## Instalação

1. Clone o repositório e acesse a pasta:

   ```bash
   git clone <URL_DO_SEU_REPOSITORIO>
   cd <nome_do_repositorio>
2. 
Crie um ambiente virtual (opcional, mas recomendado):
Bash
Copiar o código
python -m venv venv
3. 
Ative o ambiente virtual:
• 
No Windows:
Bash
Copiar o código
venv\Scripts\activate
• 
No macOS/Linux:
Bash
Copiar o código
source venv/bin/activate
4. 
Instale as dependências:
Bash
Copiar o código
pip install -r requirements.txt
Execução
1. 
Execute a aplicação:
Bash
Copiar o código
python app.py
2. 
A API estará disponível em http://127.0.0.1:5002.
Acesso à Documentação Swagger
• Acesse a documentação Swagger em http://localhost:5002/swagger.
Execução com Docker (Opcional)
1. 
Construa a imagem Docker:
Bash
Copiar o código
docker build -t usuarios_lojas7 .
2. 
Execute o container:
Bash
Copiar o código
docker run -p 5002:5002 usuarios_lojas7
3. 
Acesse a aplicação em http://localhost:5002/swagger.