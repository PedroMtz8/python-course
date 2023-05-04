print("""
      Bievenido a tu calculadora, una calculadora aritmetica sencilla,
      donde podras ejecutar tus operaciones escribiendo: "sumar", "restar",
      "multiplicar" y "dividir".
      
        * Cada que termine una operación, la siguiente se operara con el resultado anterior,
        si quieres empezar una operación nueva escribe: "reiniciar"
      
      Para cerrar la calculadora escribe: "salir"
      """)

result = ""

options = ["sumar", "restar", "multiplicar", "dividir"]

def isDigit(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

while True:
    if not result: 
        result = input("Ingresa número: ")
        isInt = isDigit(result) 
        # result.isdigit()
        while not isInt:
            result = input("Solo se aceptan numeros, ingresa: ")
            isInt = isDigit(result)
            if result.lower() == "salir":
                break
        if result.lower() == "salir":
            print("Calculadora cerrada")
            break
    result = float(result)
    op = input("Ingresa la operación que deseas realizar: ")
    op = op.lower()
    if op == "salir":
        print("Calculadora cerrada")
        break
    # elif op != "sumar":
    elif op == "reiniciar":
        result = ""
        result = input("Ingresa número: ")
        continue
    #     print("SUMA A FUERZA")
    # xd = not op == "sumar" or not op == "restar" or not op == "multiplicar" or not "dividir"
    # print("El objeto arroja: ", options[op])
    xd = op not in options
    while xd:
        # print("Viendo", xd)
        op = input("Operacion no valida, reingresar operación: ")
        if op == "salir":
            print("Calculadora cerrada")
            break
        elif op == "sumar" or op == "restar" or op == "multiplicar" or op == "dividir":
            xd = False
    if op == "salir":
            break
    n2 = input("Ingresa el siguiente numero: ")
    isInt2 = isDigit(n2)
    while not isInt2:
        n2 = input("Solo acepta numeros: ")
        isInt2 = isDigit(n2)
    if n2 == "salir":
        print("Calculadora cerrada")
        break
    
    elif op == "sumar":
        result += float(n2)
    elif op == "restar":
        result -= float(n2)
    elif op == "dividir":
        result /= float(n2)
    elif op == "multiplicar":
        result *= float(n2)
        
    else: 
        print("Operación no valida")
        break
    
    print(f"El resultado es: {result}")