def sumar(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Mensaje de error: Has introducido datos que no son numéricos")
    else:
        return a + b
    
def restar(a,b):
    if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("Mensaje de error: Has introducido datos que no son numéricos")
    return a - b; 

def multiplicar(a,b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Mensaje de error: Has introducido datos que no son numéricos")
    return a * b; 

def dividir(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Has introducido datos que no son numéricos")
    elif b == 0:
        raise ValueError("El divisor no puede ser cero")
    elif a == 0:
        return 0
    else:
        return a / b


if __name__ == "__main__":
    print("=====Operaciones=====")
    print("Suma: ", sumar(5,3))
    print("Resta: ",restar(5,3))
    print("Multiplicación: ",multiplicar(5,3))
    print("División: ",dividir(5,3))

