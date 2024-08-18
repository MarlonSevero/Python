"""
Decoradores : Decorators

O que sao ?

>> Decorators sao funcoes
>> Decorators envolvem outras funcoes e aprimoram seu comportamento.
>> Decorators sao um exemplo de HOF.

Decorators tem uma sintax propria, utilizando '@'. 'Syntax Sugar'

>>

FUNCTION DECORATORS
#Decorator como funcao. Sintax nao recomendada sem SugarSintax

def be_nice(fuction):
    def been():
        print('Hello, you re nice!')
        fuction()
        print('GoodBy')
    return been()


def saudacao():
    print('Welcome')

be_nice(saudacao)

------------------------------------------------------------------------------------------------

DECORATORS

#Com Sugar Syntax

def be_nice(funcao):
    def been():
        print('Hello, you re nice!')
        funcao()
        print('GoodBy \n')
    return been


@be_nice
def welcome():
    print('Welcome')


welcome()
@be_nice
def sleep():
    print('Want Sleep')

sleep()

# Um exemplo de utilizacao seria por exemplo para acessar uma guia especifica em uma pagina web  o sistema precisa
fazer uma verificao em outra funcao para validar o check_login. Podiamos decorar a funcao de acesso a guia para passar
pelo decorator antes de redirecionar.


#OBS, NAO CONFUNDA DECORATOR COM DECORATOR FUNCTION.

"""

def be_nice(funcao):
    def been():
        print('Hello, you re nice!')
        funcao()
        print('GoodBy \n')
    return been


@be_nice
def welcome():
    print('Welcome')


welcome()
@be_nice
def sleep():
    print('Want Sleep')

sleep()


