import sqlite3
from flask import current_app, g

from src.model.usuario import Usuario

class BaseUsuarios:
    def __init__(self):
        self.app = current_app

    def get_db(self):
        if 'db' not in g:
            g.db = sqlite3.connect(
                self.app.config['DATABASE'],
                detect_types=sqlite3.PARSE_DECLTYPES
            )
            g.db.row_factory = sqlite3.Row
        return g.db

    def close_db(self, e=None):
        db = g.pop('db', None)
        if db is not None:
            db.close()

    def criar_tabela(self):
        try:
            cursor = self.get_db().cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS usuarios (
                    nome TEXT,
                    senha TEXT,
                    documento TEXT PRIMARY KEY,
                    email TEXT
                )
            ''')
            self.get_db().commit()
        except sqlite3.Error as e:
            print(f"Erro ao criar tabela: {e}")

    def inserir_usuario(self, usuario):
        try:
            cursor = self.get_db().cursor()
            cursor.execute('''
                INSERT INTO usuarios (nome, senha, documento, email)
                VALUES (?, ?, ?, ?)
            ''', (usuario.nome, usuario.senha, usuario.documento, usuario.email))
            self.get_db().commit()
            return True
        except sqlite3.Error as e:
            print(f"Erro ao inserir usuário: {e}")
            return False

    def buscar_usuario(self, documento):
        try:
            cursor = self.get_db().cursor()
            cursor.execute('''
                SELECT nome, documento, senha, email FROM usuarios WHERE documento = ?
            ''', (documento,))
            resultado = cursor.fetchone()
            if resultado:
                usuario_data = {
                    'nome': resultado['nome'],
                    'senha': resultado['senha'],
                    'email': resultado['email']
                }
                return Usuario(**usuario_data)
            return None
        except sqlite3.Error as e:
            print(f"Erro ao buscar usuário: {e}")
            return None

    def atualizar_usuario(self, usuario):
        try:
            cursor = self.get_db().cursor()
            cursor.execute(''' 
                UPDATE usuarios SET senha = ?, email = ? WHERE documento = ?
            ''', (usuario.senha, usuario.email, usuario.documento))
            self.get_db().commit()
            return True
        except sqlite3.Error as e:
            print(f"Erro ao atualizar usuário: {e}")
            return False

    def deletar_usuario(self, documento):
        try:
            cursor = self.get_db().cursor()
            cursor.execute('''
                DELETE FROM usuarios WHERE documento = ?
                ''', (documento,))
            self.get_db().commit()
            return True
        except sqlite3.Error as e:
            print(f"Erro ao deletar usuário: {e}")
            return False
