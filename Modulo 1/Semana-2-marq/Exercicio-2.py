import os

def add_contact():
    name = input("Informe o Nome: \n")
    address = input("Informe o Endereço: \n")
    phone = input("Informe o Telefone: \n")
    
    contact = f"Nome: {name}\nEndereço: {address}\nTelefone: {phone}\n"
    
    with open("contacts.txt", "a", encoding="utf-8") as file:
        file.write(contact)
    
    print("Contato adicionado com sucesso!")

def view_contacts():
    if not os.path.exists("contacts.txt"):
        print("Lista de contatos está vazia.")
        return
    
    with open("contacts.txt", "r", encoding="utf-8") as file:
        contacts = file.read()
    
    print("Address Book:")
    print(contacts)

def delete_contacts():
    if not os.path.exists("contacts.txt"):
        print("Lista de Contatos está vazia.")
        return
    
    with open("contacts.txt", "w") as file:
        file.write("")
    
    print("Contatos excluídos com sucesso!")


def main():
    while True:
        print("\nMenu:")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Delete all contacts")
        print("4. Quit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            delete_contacts()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

main()