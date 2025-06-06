# 🎓 Sistema de Gerenciamento de Inventário

API REST simples desenvolvida com Python e Flask para gerenciar o inventário de produtos de uma loja, com foco em boas práticas de desenvolvimento e TDD.

## ✅ Funcionalidades

- Cadastro, atualização, consulta e remoção de produtos.
- Listagem de produtos com filtros por nome e categoria.
- Controle de entrada e saída de estoque.
- Validação de dados e regras de negócio.

## 🛠️ Requisitos Técnicos

- Python 3.8+
- Flask
- Pytest

## 🚀 Como Executar

### 1. Preparação do Ambiente

Clone este repositório e navegue até a pasta do projeto.

```bash
git clone https://github.com/ailonTeixeira/sistemaInventario
cd sistemaInventario
```

Criar ambiente virtual

```bash
# Para Windows
python -m venv venv
.\venv\Scripts\activate

# Para macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

### 2. Executando os Testes

Para garantir que tudo está funcionando corretamente, execute os testes automatizados:

```bash
pytest -v
```
Todos os testes devem passar.

### 3. Executando a Aplicação

Para iniciar o servidor da API, execute:

```bash
python app.py
```

A API estará disponível em `http://127.0.0.1:5000`.

## 📖 Documentação da API

### `POST /produtos`
Cria um novo produto.

**Exemplo com cURL:**
```bash
curl -X POST -H "Content-Type: application/json" -d '{
    "nome": "Mouse sem Fio",
    "categoria": "Periféricos",
    "preco_unitario": 89.90,
    "quantidade_inicial": 50
}' http://127.0.0.1:5000/produtos
```

### `GET /produtos`
Lista todos os produtos. Suporta filtros via query string.

**Exemplos:**
```bash
# Listar todos
curl http://127.0.0.1:5000/produtos

# Filtrar por nome
curl "http://127.0.0.1:5000/produtos?nome=mouse"

# Filtrar por categoria
curl "http://127.0.0.1:5000/produtos?categoria=Periféricos"
```

### `GET /produtos/<id>`
Consulta um produto específico pelo ID.

```bash
curl http://127.0.0.1:5000/produtos/1
```

### `PUT /produtos/<id>`
Atualiza os dados de um produto.

```bash
curl -X PUT -H "Content-Type: application/json" -d '{
    "preco_unitario": 95.00
}' http://127.0.0.1:5000/produtos/1
```

### `DELETE /produtos/<id>`
Remove um produto do inventário.

```bash
curl -X DELETE http://127.0.0.1:5000/produtos/1
```

### `POST /produtos/<id>/estoque`
Registra uma operação de entrada ou saída no estoque.

**Exemplo (Entrada):**
```bash
curl -X POST -H "Content-Type: application/json" -d '{
    "tipo": "entrada",
    "quantidade": 10
}' http://127.0.0.1:5000/produtos/1/estoque
```

**Exemplo (Saída):**
```bash
curl -X POST -H "Content-Type: application/json" -d '{
    "tipo": "saida",
    "quantidade": 5
}' http://127.0.0.1:5000/produtos/1/estoque
```
