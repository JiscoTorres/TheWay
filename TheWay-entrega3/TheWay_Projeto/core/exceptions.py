class EstoqueInsuficienteException(Exception):
    def __init__(self, produto_nome=''):
        self.produto_nome = produto_nome
        super().__init__(f"Estoque insuficiente para: {produto_nome}")
