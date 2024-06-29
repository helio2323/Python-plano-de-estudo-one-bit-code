def my_decorator(func):
    def wrapper():
        print("Antes de executar a função")
        func()
        print("Depois de executar a função")
    return wrapper

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper


# Exemplo 1 - 
@my_decorator
def my_function():
    print("Dentro da função")

my_function()

# Exemplo 2 - Deixando uma string em maiúscula

@uppercase_decorator
def say_hi():
    return 'Olá mundo'

print(say_hi())

# Exemplo 3 - Múltiplos Decorators
@split_string
@uppercase_decorator
def example():
    return "Aprendendo Python e criando decorators"

print(example())