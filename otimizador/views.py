from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

def newton_method(f, grad_f, hess_f, x0, tol=1e-5, max_iter=50):
    x = x0
    for _ in range(max_iter):
        grad = grad_f(x)
        hess = hess_f(x)
        if np.linalg.norm(grad) < tol:
            break
        delta_x = np.linalg.solve(hess, -grad)
        x = x + delta_x
    return x

def f(x):
    return x[0]**2 + x[1]**2

def grad_f(x):
    return np.array([2*x[0], 2*x[1]])

def hess_f(x):
    return np.array([[2, 0], [0, 2]])

def gerar_plot(x0, x_final):
    fig, ax = plt.subplots()
    ax.plot([x0[0], x_final[0]], [x0[1], x_final[1]], 'ro-')
    ax.set_title("Trajetória do Método de Newton")
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    imagem_base64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close(fig)
    return imagem_base64

@csrf_exempt
def otimizar_view(request):
    if request.method == 'POST':
        try:
            dados = json.loads(request.body)
            x0 = np.array(dados.get("x0", [1.0, 1.0]))
            tol = float(dados.get("tol", 1e-5))
            max_iter = int(dados.get("max_iter", 50))
            x_final = newton_method(f, grad_f, hess_f, x0, tol, max_iter)
            imagem = gerar_plot(x0, x_final)
            return JsonResponse({
                "x_final": x_final.tolist(),
                "imagem_base64": imagem
            })
        except Exception as e:
            return JsonResponse({"erro": str(e)}, status=400)
    else:
        return JsonResponse({"mensagem": "Apenas POST é permitido."}, status=405)
