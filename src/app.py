from src.repository.base_usuarios import BaseUsuarios
from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

from src.model.usuario import Usuario
from src.service.usuario_services import UsuarioService

app = Flask(__name__)
app.config['DATABASE'] = 'usuarios.db'
usuario_service = UsuarioService()

with app.app_context():
    usuario_service.db.criar_tabela()


@app.teardown_appcontext
def close_db(e=None):
    BaseUsuarios().close_db(e)


# swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Usuários Lojas7"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
# end swagger specific ###


@app.route('/usuarios', methods=['POST'])
def cadastrar_usuario():
    dados = request.get_json()
    usuario = Usuario(**dados)
    try:
        usuario_service.cadastrar_usuario(usuario)
        return jsonify({'mensagem': 'Usuário cadastrado com sucesso!'}), 201
    except ValueError as e:
        return jsonify({'mensagem': 'erro!, str(e)'}), 400


@app.route('/usuarios/<documento>', methods=['GET'])
def buscar_usuario(documento):
    usuario = usuario_service.buscar_usuario(documento)
    if usuario:
        usuario_data = {
            'nome': usuario.nome,
            'email': usuario.email
        }
        return jsonify({'mensagem': 'Usuário encontrado!', 'usuario_data': usuario_data}), 200
    return jsonify({'mensagem': 'Usuário não encontrado!'}), 404


@app.route('/usuarios/<documento>', methods=['PUT'])
def atualizar_usuario(documento):
    dados = request.get_json()
    try:
        usuario = Usuario(**dados)
        usuario.documento = documento
        usuario_service.atualizar_usuario(usuario)
        return jsonify({'mensagem': 'Usuário atualizado com sucesso!'}), 200
    except ValueError as e:
        return jsonify({'mensagem': 'erro ao atualizar, str(e)'}), 400


@app.route('/usuarios/<documento>', methods=['DELETE'])
def deletar_usuario(documento):
    if usuario_service.deletar_usuario(documento):
        return jsonify({'mensagem': 'Usuário deletado com sucesso!'}), 200
    return jsonify({'mensagem': 'Usuário não encontrado!'}), 500


@app.route('/login', methods=['POST'])
def login():
    dados = request.get_json()
    usuario = usuario_service.autenticar_usuario(dados['documento'], dados['senha'])
    if usuario:
        return jsonify({'mensagem': 'Login realizado com sucesso!'}), 200
    return jsonify({'mensagem': 'Credenciais inválidas!'}), 401


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
