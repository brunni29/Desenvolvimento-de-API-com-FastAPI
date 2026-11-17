# API de Consulta ao Acervo de uma Biblioteca

API desenvolvida em Python utilizando FastAPI para consulta ao acervo de uma biblioteca.

A aplicação permite consultar todos os livros cadastrados ou buscar um livro específico pelo seu identificador.

## Tecnologias utilizadas

- Python
- FastAPI
- Uvicorn
- Pydantic

## Estrutura do projeto


atividade_biblioteca/
│
├── README.md
├── modelos.py
├── livro_repositorio.py
├── servico_livros.py
└── livros.py


### Descrição dos arquivos

- modelos.py: contém o modelo `Livro` e as validações dos dados.
- livro_repositorio.p: armazena os livros em memória e realiza o acesso à coleção.
- servico_livros.py: contém as regras de negócio e a exceção para livro não encontrado.
- livros.py: contém as rotas da API e o tratamento das requisições HTTP.

## Requisitos

É necessário ter o Python instalado no computador.

Para verificar a instalação:
python --version


## Instalação

Abra o terminal na pasta do projeto e crie um ambiente virtual:

python -m venv .venv


Ative o ambiente virtual no Windows:


.venv\Scripts\activate


Depois, instale as dependências:


pip install fastapi uvicorn


## Executando a aplicação

Com o ambiente virtual ativado, execute:


uvicorn livros:app --reload


A API ficará disponível em:


http://127.0.0.1:8000


## Documentação Swagger

O FastAPI disponibiliza uma documentação interativa automaticamente.

Acesse no navegador:


http://127.0.0.1:8000/docs


Nessa página é possível visualizar e testar as rotas da API.

## Rotas disponíveis

### Listar todos os livros


GET /livros


Retorna a lista de livros cadastrados.

Exemplo:


[
  {
    "id": 1,
    "titulo": "Dom Casmurro",
    "autor": "Machado de Assis",
    "ano_publicacao": 1899,
    "disponivel": true
  }
]


### Buscar livro por identificador


GET /livros/{livro_id}


Exemplo:


GET /livros/1


Retorna o livro correspondente ao identificador informado.

## Códigos de resposta

- 200 OK: livro encontrado ou lista de livros retornada com sucesso.
- 404 Not Found: identificador válido, mas não existe livro correspondente.
- 422 Unprocessable Entity: identificador inválido, como zero, número negativo ou texto.

## Validações

Cada livro possui os seguintes campos:

- `id`: inteiro maior que zero.
- `titulo`: texto que não pode ser vazio.
- `autor`: texto que não pode ser vazio.
- `ano_publicacao`: inteiro maior que zero.
- `disponivel`: valor booleano que indica se o livro está disponível para empréstimo.

## Acervo

O acervo é armazenado em memória e possui pelo menos cinco livros cadastrados.

Como os dados são armazenados em memória, eles são reiniciados quando a aplicação é encerrada.

## Execução

Para encerrar a aplicação, pressione:


CTRL + C