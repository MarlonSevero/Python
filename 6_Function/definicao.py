"""

- Funções são pequenas partes de código que realizam tarefas específicas.
- Podem ou nao receber entrada de dados e retornar uma saida de dados;
- Muito uteis para executar procedimentos similares por repetidas vezes;

OBS: Se voce escrever uma função que realiza varias tarefas dentro dela,
é bom fazer uma verificação para que a função seja simplificada.

Já utilizamos várias funções desde que iniciamos esse curso:

- print()
- len()
- max()
- min()
- Count()
- e muitas outras;



"""

# Exemplo de utilização de funções:

#cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando uma função integrada (Built-in) do Python print()

#print(cores)

#curso = 'Python'

#print(curso)

#cores.append('roxo')

# print(cores)

# curso.append('Mais dados...')  # AttributeError =>'str' object has no attribute 'append'

# Em algumas funções podemos utilizar qualquer tipo de dados e simplismente chamar a funções e executa-la
# como o 'print()'. Outras funções estão integradas a algum tipo de dado especifico,
# como por exemplo a função append(), nao podemos utilizar essa função em qualquer lugar,
# podemos quando estamos trabalhando com o tipo de dado lista por exemplo.

# cores.clear()
# print(cores)

# DRY - Don't Repeat Yourself - Não repita você mesmo / Não repita seu código.

# Mas então, como definir funções?

"""
Em Python a forma geral de definir funcao é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao
    
Onde

nome_da_funcao -> SEMPRE, com letras minúsculas, e se for composto, separado por underline (Snake Case)

parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por virgula, podendo ser opcional ou não.

bloco_da_funcao -> Tambem chamado de corpo da função ou implementação, é onde o processamento da função acontece.
Neste bloco, pode ter ou não retorno da função.

OBS: Veja que para definir uma função, utilizamos a palavra reservada 'def' informando ao Python que 
estamos definindo uma função. Também abrimos o bloco de código com o já conhecido dois pontos : que é
utilizado em Python para definir blocos

def = definition

# Definindo a primeira função:

 #EXEMPLO 1
 
def diz_oi():
    print('OI')

OBS: 
1- Veja que, dentro das nossas funções podemos utilizar outras funções;
2- Veja que esta função só executa 1 tarefa, ou seja, a unica coisa que ela faz é dizer oi;
3- Veja que esta função não recebe nenhum parametro;
4- Veja que esta função não retorna a nada;
# Utilizando Funções

# Chamada de execução
diz_oi()

ATENÇAO:
Nunca se essqueça de utilizar o parenteses ao executar uma função.

# Exemplo 2
def cantar_parabens():
    print('Parabens')
    print('Parabens')
    print('Parabens')
    print('Parabens')

for n in range(5):
    cantar_parabens()


Em Python, podemos inclusive criar variaveis do tipo de uma função e executar esta função atraves da variável.

canta = cantar_parabens
canta()

"""