from flask import Blueprint, request, jsonify
from otimizadorpy.otimizadorpy import gradiente_conjugado_simbolico
from sympy import symbols, sympify
import json
import os

otimizar_bp = Blueprint('otimizar', __name__)

@otimizar_bp.route('/otimizar', methods=['POST'])
def otimizar():
    try:
        data = request.json
        funcao_str = data.get('funcao')
        variaveis_str = data.get('variaveis', 'x y')
        ponto_inicial = data.get('ponto_inicial', [0.0, 0.0])
        tolerancia = data.get('tolerancia', 1e-6)
        max_iter = data.get('max_iter', 100)

        variaveis = symbols(variaveis_str)
        funcao = sympify(funcao_str)

        resultado = gradiente_conjugado_simbolico(
            funcao, variaveis, ponto_inicial, tolerancia, max_iter
        )

        # Salvar no histórico
        registro = {
            'entrada': {
                'funcao': funcao_str,
                'variaveis': variaveis_str,
                'ponto_inicial': ponto_inicial,
                'tolerancia': tolerancia,
                'max_iter': max_iter
            },
            'resultado': resultado
        }

        os.makedirs('data', exist_ok=True)
        caminho = os.path.join('data', 'historico.json')

        try:
            if os.path.exists(caminho):
                with open(caminho, 'r', encoding='utf-8') as f:
                    historico = json.load(f)
            else:
                historico = []
        except json.JSONDecodeError:
            historico = []

        historico.append(registro)

        with open(caminho, 'w', encoding='utf-8') as f:
            json.dump(historico, f, indent=4, ensure_ascii=False)

        return jsonify({
            'minimo': resultado['minimo'],
            'valor_funcao': resultado['valor_funcao'],
            'iteracoes': resultado['iteracoes']
        })

    except Exception as e:
        return jsonify({'erro': str(e)}), 400
