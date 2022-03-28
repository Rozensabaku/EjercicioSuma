# Funcion para sumar numeros enteros

def plus(x, y):
    if isinstance(x, int) and isinstance(y, int):
        return x + y 
    else:
        raise TypeError('Los numeros deben ser enteros')





print(plus(4, 9))


