"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.

# Biblioteca para trabalhar com dados estatísticos.
import statistics

*********** Dados coletados de algum sensor ***********

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

#Calculando a média dos dados utilizando a função mean() 'Mean = Media'
media = statistics.mean(dados)
print(media)

#OBS: Assim como a função map(), a filter() recebe dois parâmetros, sendo
# uma função e um iterável.

res = filter(lambda valor: valor > media, dados)
print(type(res))
print(list(res))

# OBS: Assim como na função map(), após serem utilizados os dados de filter() eles são excluídos da memória.

*********** Removendo os Dados Faltantes ***********

paises = ['', 'Argentina', 'Brasil', '', '', 'Venezuela', '', 'Chile', 'Equado', '', '', '', 'Paraguay']
print(paises)

Podemos realizar de 3 ou mais maneiras

#res = filter(lambda pais: len(pais) > 0, paises)
res = filter(None, paises)
res = filter(lambda pais: pais!= '', paises)
print(list(res))

********** A diferença entre map() e filter() é: **********

# map() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função para cada elemento do iterável
# filter() -> Recebe dois parâmetros, uma função e um iterável e retorna um obejeto filtrando apenas os elementos de acordo com a função.

# Na realidade o que muda é o tipo de função.
# Filter > retorna somente True ou False. Eles valores que vão determinar se o dado vai ser ou não selecionado.
# Map> retornar todos valores. (Claro que podemos gerar expressões condicionais/logicas)

*********** Exemplo mais complexo ***********

usuarios = [
    {"username": "Samuel", "tweets": ["Eu adoro Bolos", "Eu adoro Pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu Gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de Cachorros", "Eu Vou Sair hoje"]},
    {"username": "gal", "tweets": []}
]
print(usuarios)

Filtrar os usuários que estão inativos no Twitter

# Forma 1
inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0 , usuarios))

# Forma 2
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))

print(inativos)

*********** Combinar filter() e map() ***********

 nomes = ['Vanessa', 'Ana', 'Maria']

 # Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres

 lista = list(max(lambda nome: f'Sua Instrutora é {nome}', filter(lambda nome: len(nome) <5, nomes)))
 print(lista)

# Tudo começa pelo filtro, primeiros estamos filtrando a lista e o resultado disso estamos passando para o
# MAP. Que entao exacuta e converte para lista.
"""




