"""
TIPO NUMERICO

+  -> ADIÇÃO
-  -> SUBTRAÇÃO
/  -> DIVISÃO
*  -> MULTIPLICAÇÃO
// -> DIVISÃO PEGANDO O INTEIRO
%  -> MODULO (RESTO DA DIVISÃO)
** -> ELEVAR AO NUMERO

5/2 = 2.5 (float)

int(2/5) = 2 (int) -> 5//2 É A MESMA COISA QUE INT (2/5)

4%2 (MODULO, PEGA O RESTO DA DIVISÃO) NUMERO PAR DIVIDIDO POR 2 TEM RESTO IGUAL A 0
                                      NUMERO IMPAR DIVIDIDO POR 2 TEM RESTO IGUAL A 1
ASSIM SABEMOS SE O NUMERO É PAR OU IMPAR UTILIZANDO A OPERAÇÃO DO MODULO

3**3 = 27 (O NUMERO MAX DE BYTES DEPENDE DA MEMORIA DO COMPUTADOR SOMENTE)

NUMEROS GRANDES SÃO ESCRITOS COM UNDERLINE 1_000_000_000

num = 10
num + 1 = 11

num => Aqui num é igual a 10, porem

num+=1
num é igual a 11 agora

Podemos fazer a mesma coisa com vezes(*) divisão(/) divisao inteira (//)
num =2
num*=2
num = 4
--
num/=2
num=1
--
num = 5
num//=2
num = 2

FUNÇÃO TYPE()

TYPE(numero) = Mostra o tipo de dado
type(23) = int
type(5.5) = float

DIR(NUM) -> VEMOS AS OPERAÇÕES QUE PODEMOS ULTILIZAR COM NUM

EX:
NUM = 10

NUM.__add__(10)
NUM = 20


"""

num = 1

#print(help(num))
#print(type(num))
#print(dir(num))

print(f'Add Operation {num.__add__(10)}')
print(type(num))