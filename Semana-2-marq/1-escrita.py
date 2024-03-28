name = input("Qual seu nome?\n")

# r - leitura
# w - escrita
# a - append
file = open("names.txt", "w")
file.write(name)
file.close()

name = input("Qual seu nome?\n")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()

name = input("Qual seu nome?\n")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")