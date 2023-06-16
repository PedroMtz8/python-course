def removeSpace(text):
    newText = ""
    for char in text:
        if char != " ":
            newText += char
    return newText

def reverse(text):
    reversedText = ""
    for char in text:
        reversedText = char + reversedText
    return reversedText

def es_palindromo(text):
    text = removeSpace(text)
    reversedText = reverse(text)
    return text == reversedText

result = removeSpace("Hola que tal?")
print("Hola que tal 2".replace(" ", ""))
print(result)

print(es_palindromo("Hola"))
print(es_palindromo("amo la paloma"))