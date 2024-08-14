"""
Documentando funçoes com Doctrings.

OBS: Podemos ter acesso a documentação de uma função em Python utilizando a Propriedade especial __doc__

# Exemplos

def diz_oi():
    'Uma função simples que retorna diz oi'
    return 'oi'

print(diz_oi())
print(diz_oi.__doc__)


"""


def exponencial(numero, potencia = 2):

    """
    Por padrao Pycharm tras a Doc informando aspas triplas

    Função que por padraão retorna o quadrado de um 'numero' ou numero a pontencia informada
    :param numero: Numero que desejamos gerar o exponencial
    :param potencia: Potencia que queremos gerar o exponencial. Por padrão é 2
    :return: Retorna numero por potencia
    """

    return numero**potencia


print(exponencial(50))
print(exponencial.__doc__)