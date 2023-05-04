
def sumar():
    n1 = input("Ingresa un numero: ")
    n2 = input("Ingresa el siguiente numero: ")
    return print(int(n1) + int(n2))

sumar()


def isDigit(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


print(isDigit("-3.5"))