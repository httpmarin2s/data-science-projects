# lista de supermercado 

lista = ["maçã", "banana", "pêra", "uva"]

def mostrar_lista():
    print(f"Sua lista de compras atual")
    for i, item in enumerate(lista,1):
        print(f"{i}-{item}")

def adicionar_lista():
    item = input("Digite o item que queria adicionar: ")
    lista.append(item)
    print(lista)
    teste = input("gostaria de adicionar outro item? [s/n]").strip().lower()
    while teste == 's':
        item = input("Digite o item que queria adicionar: ")
        lista.append(item)
        print(lista)
        teste = input("gostaria de adicionar outro item? [s/n]").strip().lower()

def remover_lista():
    item = input("Digite o item que quer remover: ").strip().lower()
    if item in lista:
        lista.remove(item)
        print(lista)
        teste = input("gostaria de remover outro item? [s/n]").strip().lower()
    
        while teste == 's':
            item = input("Digite o item que queria remover: ").strip().lower()
            lista.remove(item)
            print(lista)
            teste = input("gostaria de remover outro item? [s/n]").strip().lower()
    else:
        print(f"{item} não está na lista")

# menu prinicap 
resposta = 's'
while resposta == 's':
    print("Acesse sua lista de compras")
    print("[1] Mostrar a sua lista")
    print("[2] Adicionar item na sua lista")
    print("[3] Remover item da sua lista")
    resposta = int(input("Digite sua resposta: "))

    if resposta == 1:
        mostrar_lista()
    
    elif resposta == 2:
        adicionar_lista()

    elif resposta == 3:
        remover_lista()
    
    else: 
        print("valor não encontrado")
    
    resposta = input("Gostaria de voltar ao menu?[s/n]")
