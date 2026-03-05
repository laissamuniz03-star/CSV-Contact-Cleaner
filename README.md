# Limpeza de Contatos CSV com Python

Projeto em Python para limpar e padronizar contatos telefônicos exportados em CSV.

## Funcionalidades

- Remove contatos inválidos
- Identifica números suspeitos
- Organiza nome e telefone
- Gera arquivos prontos para reimportação no celular

## Arquivos gerados

- `contatos_limpos.csv` → contatos válidos
- `contatos_suspeitos.csv` → números que precisam de revisão

## Tecnologias usadas

- Python
- Manipulação de arquivos CSV

## Como usar

1. Coloque o arquivo `contatos.csv` na pasta do projeto
2. Execute o script:

python limpar_contatos.py

3. O programa irá gerar os arquivos limpos automaticamente.