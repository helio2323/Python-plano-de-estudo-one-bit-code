## Conta letras maiúsculas e minúsculas

#Escreva uma função Python que receba uma string e conte o número de letras maiúsculas e minúsculas desta string.

upper = 0

lower = 0

text = input("Digite uma frase: ")

for i in text:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
        
print(f"A frase {text} tem {upper} letras maiúsculas e {lower} letras minúsculas")



## Lista números pares e ímpares de uma lista

#Escreva uma função Python para imprimir os números pares e ímpares em duas listas separadas para cada uma.

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print(f"O número {numero} é par")
else:
    print(f"O número {numero} é ímpar")


# Resolucoes do curso

def check_char(text):
    type={"Uppercase":0, "Lowercase":0}
    for char in text:
        if char.isupper():
           type["Uppercase"]+=1
        elif char.islower():
           type["Lowercase"]+=1
    print ("Texto original: ", text)
    print ("Número de letras maiúsculas: ", type["Uppercase"])
    print ("Número de letras minúsculas: ", type["Lowercase"])

#string_test('The quick Brown Fox')
check_char("A melhor forma de prever o futuro é Criá-Lo")

def check_numbers(numbers):
    pairs = []
    odd = []
    for number in numbers:
        if number % 2 == 0:
            pairs.append(number)
        else:
            odd.append(number)
    return pairs, odd
print(check_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))