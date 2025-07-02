# Regsistro de Aluno com POO 
# Notas e Registro da Média

class Registro:
    
    def __init__(self, nome, valor):
        self.nome = nome 
        #self.nota1 = nota1
        #self.nota2 = nota2
        #self.nota3 = nota3
        #self.nota4 = nota4
        self.lista_notas = valor
    

    def calcular_media(self):
        #self.notas = [self.nota1, self.nota2, self.nota3, self.nota4]
        self.media = sum(self.lista_notas)/(len(self.lista_notas))
        return self.media
    

nome = input("Digite o nome do aluno: ")
notas = int(input("Digite a quantidade de Notas: "))
nota_dos_alunos = []

for i in range(notas):
    nota = float(input(f"Digite a Nota {i+1}: "))
    nota_dos_alunos.append(nota)
    print(nota_dos_alunos)


cadastro = Registro(nome, nota_dos_alunos)  
print(f"A média do aluno {cadastro.nome} é igual a  {cadastro.calcular_media()}")
