# Minha primeira árvore 

# criando a classe arvore binaria
class ArvoreBinaria:
    def __init__(self, value): # parametros
        self.value = value # no pai principal (raiz)
        self.left_child = None # no filho esquerda
        self.right_child = None # no filho direita 
    
    def insert_left(self,value):
        if self.left_child == None: #se o no esquerdo esta vazio 
            self.left_child = ArvoreBinaria(value)
        
        else: # caso não esteja vazio
            new_node = ArvoreBinaria(value) #
            new_node.left_child = self.left_child 
            self.left_child = new_node

    def insert_right(self,value):
        if self.right_child == None:
            self.right_child = ArvoreBinaria(value)
        
        else: # caso não esteja vazio 
            new_node = ArvoreBinaria(value)
            new_node.right_child = self.right_child
            self.right_child = new_node


# imaginando que queremos criar a seguinte árvore
#          A
#       /    \
#      B      C
#       \    / \
#        D  E   F

         
# criando a arvore primaria
raiz = ArvoreBinaria("A")
raiz.insert_left("B") # inserindo nó a esquerda
raiz.insert_right("C") #inserindo nó a direita

# criando um nó filho de b 
b = raiz.left_child #defindo uma outra variável como b = 'B'
b.insert_right('D') # é como se nesse caso b fosse a minha raiz

#criando os nós filhos de c
c = raiz.right_child #defino uma outra variavel que é como se fosse minha raiz
c.insert_left('E') #a
c.insert_right('F')


d = b.right_child #d
e = c.left_child
f = c.right_child

print(raiz.value)
print(b.value)
print(c.value)
print(d.value)
print(e.value)
print(f.value)