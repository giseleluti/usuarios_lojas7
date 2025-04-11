class Usuario:
    def __init__(self, **kwargs):
        self.nome= kwargs.get("nome")
        self.senha = kwargs.get("senha")
        self.documento = kwargs.get("documento")
        self.email = kwargs.get("email")
