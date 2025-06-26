from flask import Blueprint, jsonify
import json
import os

historico_bp = Blueprint('historico', __name__)
CAMINHO = os.path.join('data', 'historico.json')

@historico_bp.route('/historico', methods=['GET'])
def listar_historico():
    if not os.path.exists(CAMINHO):
        return jsonify([])

    with open(CAMINHO, 'r', encoding='utf-8') as f:
        try:
            historico = json.load(f)
        except json.JSONDecodeError:
            historico = []

    return jsonify(historico)
