"""
Metadados: Dados intrisecos.

wraps : Sao funcoes que envolvem elementos com diversas funcionalidades. Um exemplo seria o proprio decorator.

# The problem ...

def see_logs(login_function):
    def login(*args, **kwargs):
        I am a doc of this functions
        print(f"Its calling :  {login_function.__name__}")
        print(f"Function Doc : {login_function.__doc__}")
        return login_function(*args, **kwargs)
    return login


@see_logs
def sum_numbers(num1, num2):
    Sum two numbers given
    return num1 + num2

print(sum_numbers(10, 10))

print(sum_numbers.__doc__) #thats the problem, esta retornando a doc errada
print(sum_numbers.__name__) #Thats the problem, esta retornando o nome errado




"""

# Solve The problem

from functools import wraps

def see_logs(login_function):
    @wraps(login_function)                  #Apply Wraps
    def login(*args, **kwargs):
        """I am a doc of this functions"""
        print(f"Its calling :  {login_function.__name__}")
        print(f"Function Doc : {login_function.__doc__}")
        return login_function(*args, **kwargs)
    return login


@see_logs
def sum_numbers(num1, num2):
    """Sum two numbers given"""
    return num1 + num2

print(sum_numbers(10, 10))

print(sum_numbers.__doc__) #Now its return the rigth doc
print(sum_numbers.__name__) #Now its return the rigth doc


