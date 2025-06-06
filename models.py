

# Usado um dicionário para acesso rápido por ID O(1)
estoque = {}
proximo_id = 1

def resetar_estoque():
    """Função auxiliar para limpar o estoque durante os testes."""
    global estoque, proximo_id
    estoque = {}
    proximo_id = 1

def criar_produto(dados):
    """
    Cria um novo produto no inventário.
    Valida os dados de entrada.
    """
    global proximo_id
    
    # Validação dos campos obrigatórios
    campos_obrigatorios = ["nome", "categoria", "preco_unitario", "quantidade_inicial"]
    for campo in campos_obrigatorios:
        if campo not in dados:
            return None, f"Campo '{campo}' é obrigatório."

    nome = dados["nome"]
    categoria = dados["categoria"]
    preco = dados["preco_unitario"]
    qtd = dados["quantidade_inicial"]
    
    # Validação das regras de negócio
    if not isinstance(nome, str) or not nome.strip():
        return None, "O campo 'nome' não pode ser vazio."
    if not isinstance(categoria, str) or not categoria.strip():
        return None, "O campo 'categoria' não pode ser vazio."
    if not isinstance(preco, (int, float)) or preco <= 0:
        return None, "O preço unitário deve ser um número positivo."
    if not isinstance(qtd, int) or qtd < 0:
        return None, "A quantidade inicial deve ser um número inteiro maior ou igual a zero."

    # Criação do produto
    produto = {
        "id": proximo_id,
        "nome": nome.strip(),
        "categoria": categoria.strip(),
        "preco_unitario": preco,
        "quantidade": qtd
    }
    
    estoque[proximo_id] = produto
    proximo_id += 1
    
    return produto, None

def listar_produtos(nome=None, categoria=None):
    """
    Lista todos os produtos, com suporte a filtros por nome e/ou categoria.
    """
    resultados = list(estoque.values())
    
    if nome:
        resultados = [p for p in resultados if nome.lower() in p['nome'].lower()]
    
    if categoria:
        resultados = [p for p in resultados if categoria.lower() in p['categoria'].lower()]
        
    return resultados

def obter_produto_por_id(produto_id):
    """Retorna um único produto pelo seu ID."""
    return estoque.get(produto_id)

def atualizar_produto(produto_id, dados):
    """Atualiza os dados de um produto existente."""
    produto = obter_produto_por_id(produto_id)
    if not produto:
        return None, "Produto não encontrado."

    # Atualiza os campos permitidos
    if "nome" in dados:
        nome = dados["nome"]
        if not isinstance(nome, str) or not nome.strip():
            return None, "O campo 'nome' não pode ser vazio."
        produto["nome"] = nome.strip()

    if "categoria" in dados:
        categoria = dados["categoria"]
        if not isinstance(categoria, str) or not categoria.strip():
            return None, "O campo 'categoria' não pode ser vazio."
        produto["categoria"] = categoria.strip()
    
    if "preco_unitario" in dados:
        preco = dados["preco_unitario"]
        if not isinstance(preco, (int, float)) or preco <= 0:
            return None, "O preço unitário deve ser um número positivo."
        produto["preco_unitario"] = preco

    estoque[produto_id] = produto
    return produto, None

def remover_produto(produto_id):
    """Remove um produto do inventário."""
    if produto_id in estoque:
        del estoque[produto_id]
        return True
    return False

def registrar_operacao_estoque(produto_id, tipo, quantidade):
    """
    Registra uma entrada ou saída de estoque.
    'tipo' pode ser 'entrada' ou 'saida'.
    """
    produto = obter_produto_por_id(produto_id)
    if not produto:
        return None, "Produto não encontrado."

    if not isinstance(quantidade, int) or quantidade <= 0:
        return None, "A quantidade deve ser um número inteiro positivo."
        
    if tipo == "entrada":
        produto["quantidade"] += quantidade
    elif tipo == "saida":
        if produto["quantidade"] < quantidade:
            return None, "Estoque insuficiente para a saída."
        produto["quantidade"] -= quantidade
    else:
        return None, "Tipo de operação inválida. Use 'entrada' ou 'saida'."

    estoque[produto_id] = produto
    return produto, None