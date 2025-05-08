from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def otimizar(request):
    dados = request.data
    resultado = {
        "x_otimo": [1.23, 4.56],
        "iteracoes": 10,
        "convergiu": True
    }
    return Response(resultado)
