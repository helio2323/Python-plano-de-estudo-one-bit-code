#Antecessor e Sucessor

num1 = int(input("Informe o primeiro numero: "))
num2 = int(input("Informe o segundo numero: "))

result = num1 < num2

if result == True:
    print(f"O numero {num1} e antecessor do numero {num2}")
else:
    print(f"O numero {num1} e sucessor do numero {num2}")



note1 = float(input("Digite a nota 1\n"))
note2 = float(input("Digite a nota 2\n"))
note3 = float(input("Digite a nota 3\n"))
note4 = float(input("Digite a nota 4\n"))

average = (note1 + note2 + note3 + note4) /4

print(f"Médias das notas é: {average:.2f}")