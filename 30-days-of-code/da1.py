# Cálculo de IMC 


# funções
def imc(pesox, alturax): 
    calculo = (pesox)/(alturax**2)
    calculo = int(calculo)

    return calculo

def relatorio(x): 
    if x < 18.5:
        return (f"{x} imc aponta magreza extrema")
    elif 18.5 <= x < 24.9:
        return (f"{x} imc aponta normal ")
    elif 25 <= x < 29.9:
        return (f"{x} imc aponta sobrepeso")
    elif 30 <= x < 39.9:
        return (f"{x} imc aponta obesidade")
    else:
        return(f"IMC aponta obesidade grave")

# front-end
print("bem vindo ao calculo de IMC")
print("[1] INICAR ")
print("[2] SAIR ")

# solicitação do usuário
resposta = int(input("Digite o número de sua escolha: "))

if resposta == 1:
    # solicitando dados de entrada para o usuário
    while resposta == 1:
        peso = float(input("Digite seu peso: "))
        altura = float(input("Digite sua altura: "))
        
        # convertendo a altura
        altura = altura/100
        analise = float(imc(peso, altura))
        print(analise)

        print("========================================")
        analise2 = relatorio(analise)
        print(analise2)
        
        print("========================================")
        print("Deseja repetir o cálculo?")
        print("[1] INICAR ")
        print("[2] SAIR ")

        resposta = int(input("Digite seu numero:"))




