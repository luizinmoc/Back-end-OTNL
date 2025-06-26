import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sympify, lambdify
import os

def gerar_grafico_newton(funcao_str, variaveis_str, ponto_inicial, nome_arquivo='grafico_newton.png'):
    variaveis = symbols(variaveis_str)
    funcao = sympify(funcao_str)

    f_lamb = lambdify(variaveis, funcao, modules='numpy')

    x_range = np.linspace(-5, 5, 100)
    y_range = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x_range, y_range)

    Z = f_lamb(X, Y)

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.9)

    f0 = f_lamb(*ponto_inicial)
    ax.scatter(ponto_inicial[0], ponto_inicial[1], f0, c='r', s=50, label='Ponto Inicial')

    ax.set_xlabel(variaveis_str.split()[0])
    ax.set_ylabel(variaveis_str.split()[1])
    ax.set_zlabel('f(x, y)')
    ax.set_title('Superfície da Função com Ponto Inicial')
    ax.legend()

    path = os.path.join('static', nome_arquivo)
    plt.savefig(path)
    plt.close()
    return path
