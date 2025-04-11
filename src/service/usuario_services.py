import hashlib

import validators
from validate_docbr import CPF, CNPJ

from  src.repository.base_usuarios import BaseUsuarios


class UsuarioService:
    def __init__(self):
        self.db = BaseUsuarios()


    def cadastrar_usuario(self, usuario):
        if not self.validar_documento(usuario.documento):
            raise ValueError('Documento inválido!')
        if not self.validar_email(usuario.email):
            raise ValueError('Email inválido!')
        usuario.senha = self.criptografar_senha(usuario.senha)
        self.db.inserir_usuario(usuario)

    def autenticar_usuario(self, documento, senha):
        usuario = self.db.buscar_usuario(documento)

        if usuario and usuario.senha == self.criptografar_senha(senha):
            return usuario
        return None

    def buscar_usuario(self, documento):
        usuario = self.db.buscar_usuario(documento)
        return usuario

    def atualizar_usuario(self, usuario):
        if not self.validar_email(usuario.email):
            raise ValueError('Email inválido!')
        usuario.senha = self.criptografar_senha(usuario.senha)
        self.db.atualizar_usuario(usuario)

    def deletar_usuario(self, documento):
        return self.db.deletar_usuario(documento)

    def criptografar_senha(self, senha):
        return hashlib.sha256(senha.encode()).hexdigest()

    def validar_documento(self, documento):
        cpf = CPF()
        cnpj = CNPJ()
        return cpf.validate(documento) or cnpj.validate(documento)

    def validar_email(self, email):
        return validators.email(email)

    def close(self):
        self.db.close_db()
