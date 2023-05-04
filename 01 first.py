miprimervariable = "hola"

edad = 20

# if section

if edad > 30:
    print("Eres muy grande, no puedes pasar")
elif edad >= 18:
    if edad == 20:
        print("Sos un crack")
    else: 
        print("Puedes pasar")   
else:
    print("No puedes pasar")

""" sum = "suma"
res = "resta"
div = "division"
mul = "multiplicacion" """


options = ["sumar", "restar", "multiplicar", "dividir"]

print("""
    Esto es una calculadora basica en la cuál podrás elegir que operación realizar
    escribiendo una de las siguientes opciones: "sumar", "restar", "dividir" y "multiplicar"
      """)

first = input("Introduce un numero: ")
if not first:
    first = input("Introduce un numero porfavor")

choose = input("Ingresa la operación: ")


# print(choeaose in options == choose, "hola")
if(choose == "salir"):
    exit
#     # second = input(f"Ingresa el numero a {choose}: ")
#     # response = int(first) + int(second)
#     print(f"Elegiste: {choose}" )

if choose == "sumar":
    second = input("Ingresa el numero a sumar: ")
    response = int(first) + int(second)
    print(f"El resultado es: {response}" )
if choose == "restar":
    second = input("Ingresa el numero a restar: ")
    response = int(first) - int(second)
    print(f"El resultado es: {response}" )
if choose == "dividir":
    second = input("Ingresa el numero a dividir: ")
    response = int(first) / int(second)
    print(f"El resultado es: {response}" )
if choose == "multiplicar":
    second = input("Ingresa el numero a multiplicar: ")
    response = int(first) * int(second)
    print(f"El resultado es: {response}" )

