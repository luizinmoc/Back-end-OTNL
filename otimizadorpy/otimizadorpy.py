from sympy import Matrix, lambdify
import numpy as np

def gradiente_conjugado_simbolico(funcao, variaveis, ponto_inicial, tolerancia=1e-6, max_iter=100):
    gradiente = [funcao.diff(v) for v in variaveis]
    gradiente_func = lambdify(variaveis, gradiente, modules='numpy')
    funcao_func = lambdify(variaveis, funcao, modules='numpy')

    x = np.array(ponto_inicial, dtype=float)
    g = np.array(gradiente_func(*x)).astype(np.float64)
    d = -g
    iteracoes = 0

    while np.linalg.norm(g) > tolerancia and iteracoes < max_iter:
        alpha_num = -np.dot(g, d)
        x_temp = x + 1e-4 * d
        g_temp = np.array(gradiente_func(*x_temp)).astype(np.float64)
        beta_den = np.dot(d, g_temp - g)
        alpha = alpha_num / (beta_den + 1e-8)

        x = x + alpha * d
        g_novo = np.array(gradiente_func(*x)).astype(np.float64)
        beta = np.dot(g_novo, g_novo) / (np.dot(g, g) + 1e-8)
        d = -g_novo + beta * d
        g = g_novo
        iteracoes += 1

    return {
        'minimo': x.tolist(),
        'valor_funcao': float(funcao_func(*x)),
        'iteracoes': iteracoes
    }
