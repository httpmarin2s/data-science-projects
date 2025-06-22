# programa de eleição

print("Análise de idade para votação")
print("============================")

def idade_analise(x):
    if x < 18:
        return 'Menor de idade, não pode votar'
    elif x >= 18:
        return 'Maior de idade, pode votar'


print("============================")
registro = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
genero = input("Digite seu gênero: ")

print("Relatório:")
print(f"Nome: {registro}")
print(f"Idade: {idade}")
print(f"Gênero: {genero}")
print(f"Resultado: {idade_analise(idade)}")