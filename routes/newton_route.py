from flask import Blueprint, request, jsonify
from visualizacao.newton_plot import gerar_grafico_newton

newton_bp = Blueprint('newton', __name__)

@newton_bp.route('/visualizar', methods=['POST'])
def visualizar():
    try:
        data = request.json
        funcao_str = data.get('funcao')
        variaveis_str = data.get('variaveis', 'x y')
        ponto_inicial = data.get('ponto_inicial', [1.0, 1.0])
        nome_arquivo = data.get('nome_arquivo', 'grafico_newton.png')

        path = gerar_grafico_newton(funcao_str, variaveis_str, ponto_inicial, nome_arquivo)

        return jsonify({'mensagem': 'Gráfico gerado com sucesso.', 'caminho_imagem': path})

    except Exception as e:
        return jsonify({'erro': str(e)}), 400
