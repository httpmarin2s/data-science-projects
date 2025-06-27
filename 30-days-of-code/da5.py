# Regsistro de Aluno com POO 
# Notas e Registro da Média

class Registro:
    
    def __init__(self, nome, nota1, nota2, nota3, nota4):
        self.nome = nome 
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
    

    def calcular_media(self, nota1, nota2, nota3, nota4):
        self.media = (nota1 + nota2 + nota3 + nota4)/4
    




nome = input("Digite o nome do aluno: ")
nota1 = int(input("Digite o nota 1 do aluno: "))
nota2 = int(input("Digite o nota 2 do aluno: "))
nota3 = int(input("Digite o nota 3 do aluno: "))
nota4 = int(input("Digite o nota 4 do aluno: "))


cadastro = Registro(nome, nota1, nota2, nota3, nota4)  
print(cadastro.nome, cadastro.nota1)
print(cadastro.calcular_media)
