# código de pesquisa binária 
# livro 1 de entendendo algoritmos 


def pesquisa_binaria(lista, item):
    
    baixo = 0 
    alto = len(lista) - 1
    
    while baixo <= alto:
        meio = (alto+baixo)//2 
        chute = lista[meio]
        
        if item == chute:
            return chute

        if item > chute:
            baixo = meio + 1
        
        else:
            alto = meio - 1

    return None

minha_lista = [1,2,6,4,5,8,7,8,9,10]
resultado = pesquisa_binaria(minha_lista, 6)
print(resultado)