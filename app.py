from flask import Flask
from routes.otimizar_route import otimizar_bp
from routes.newton_route import newton_bp
from routes.historico_route import historico_bp
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join('static')

app.register_blueprint(otimizar_bp)
app.register_blueprint(newton_bp)
app.register_blueprint(historico_bp)

@app.route('/')
def index():
    return {'mensagem': 'API de Otimização Não Linear - Online'}

if __name__ == '__main__':
    app.run(debug=True)
