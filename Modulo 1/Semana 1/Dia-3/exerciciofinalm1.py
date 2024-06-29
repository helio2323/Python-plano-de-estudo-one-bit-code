"""## Gerenciamento de Jogadores e Times

Escreva um programa em python que realize o gerenciamento de jogadores. Ele deve atender aos seguintes requisitos:

- Adicionar um time
- Remover um time
- Listar times
- Adicionar jogador em um time
- Remover jogador de um time
- Listar jogadores de um time
1. A opção de listar os times deve mostrar o índice, o nome e a quantidade de jogadores do time.
2. A opção de adicionar um time deve pedir um nome para o time que será cadastrado.
3. A opção de remover um time deve pedir o índice específico do time que foi cadastrado para fazer a sua exclusão.
4. A opção de adicionar um jogador em um time deve pedir um índice do time que foi cadastrado e associar com o nome do jogador que será adicionado.
5. A opção de remover um jogador em um time deve pedir um índice do time que foi cadastrado e utilizar esse índice para remover o jogador que fora cadastrado no time.
6. A opção de listar os jogadores de um time deve ser informado o índice de um time e listar os jogadores que foram associados a ele.

Este é o exercício de revisão do módulo, então aproveite para utilizar todos os recursos vistos até agora, como os funções, condições, loop, listas, etc."""

#zerar dicionario

import pprint

pp = pprint.PrettyPrinter(depth=4)

timeDict = {"Sao paulo": [],
            "Flu": ["a"]}



def add_time():
    name = input("Digite o nome do time: ")
    if name in timeDict:
        print("Já existe um time com esse nome")
    else:
        timeDict[name] = []
        print("Time cadastrado com sucesso")

def remove_time():
    print("Times cadastrados: ")
    for i in timeDict:
        print(f"{i}")
    time_excluido = input("Digite o nome do time que deseja excluir: ")
    if time_excluido in timeDict:
        timeDict.pop(time_excluido)
    else:
        print("Digite um nome de time valido")    

def listar_times():
    print("Times cadastrados: ")
    for i in timeDict:
        print(f"{i}")
        
def add_jogadr():
    time_name = input("Digite o nome do time que deseja adicionar um novo jogador: ")
    if time_name in timeDict:
        name = input("Informe o nome do jogador: ")
        timeDict[time_name] = [name]        
        print(f"O jogador {name} foi adicionado ao time {time_name}")
    else:
        print("Digite um nome de time valido")
        
def remove_jogador():
    time_name = input("Digite o nome do time que deseja remover um jogador: ")
    if time_name in timeDict:
        print("Jogadores do time: ")
        for i in timeDict[time_name]:
            print(f"{i}")
        name = input("Informe o nome do jogador: ")
        if name in timeDict[time_name]:
            print(f"O jogador {name} foi removido do time {time_name}")
            timeDict[time_name].remove(name)
        else:
            print("Digite um nome de jogador valido")
    else:
        print("Digite um nome de time valido")

def listar_jogadores():
    time_name = input("Digite o nome do time que deseja listar os jogadores: ")
    if time_name in timeDict:
        print("Jogadores do time: ")
        for i in timeDict[time_name]:
            print(f"{i}")
    else:
        print("Digite um nome de time valido")
        
def listar_times():
    print("Times cadastrados: ")
    for i in timeDict:
        print(f"{i}")   

print("Bem vindo ao gerenciador de times selecione sua opcao para continuar")
print("1 - Adicionar um time")
print("2 - Remover um time")
print("3 - Listar times")
print("4 - Adicionar jogador em um time")
print("5 - Remover jogador de um time")
print("6 - Listar jogadores de um time")

def menu():
    print("Bem vindo ao gerenciador de times selecione sua opcao para continuar")
    print("1 - Adicionar um time")
    print("2 - Remover um time")
    print("3 - Listar times")
    print("4 - Adicionar jogador em um time")
    print("5 - Remover jogador de um time")
    print("6 - Listar jogadores de um time")
    

while True:

    
    if opcao := int(input("Digite a opcao desejada: ")):
        if opcao == 1:
            add_time()
        elif opcao == 2:
            remove_time()
        elif opcao == 3:
            listar_times()
        elif opcao == 4:
            add_jogadr()
        elif opcao == 5:
            remove_jogador()
        elif opcao == 6:
            listar_jogadores()
        elif opcao == 0:
            menu()
        else:
            print("Opcao invalida")
    else:
        print("Opcao invalida")
        
    print("Caso queira ver o menu de opcoes digite 0")
    
    