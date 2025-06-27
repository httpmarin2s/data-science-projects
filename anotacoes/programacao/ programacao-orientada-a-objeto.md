# Programação orientada a objeto em python 
---
## Recursos 
- Video aula 1 (https://www.youtube.com/watch?v=-pEs-Bss8Wc)
- Video aula 2 (https://youtu.be/IbMDCwVm63M?si=7JFNK60xfNcSVJLN)
- Video aula 3 (https://youtu.be/Ej_02ICOIgs?si=TnFVSbjD9JnzSW7d)
- Video aula 4 https://youtube.com/playlist?list=PLt73vsz1XxwxL1mKfebdlpqJvkcukOJ3S&si=ZAdlX2Zx253VVGt0)
- Artigo 1 (https://realpython.com/python3-object-oriented-programming/)

---
## Vídeo Aula 1 
### Princípio de POO
- Classes: Classes são por definição um indicativo de como um objeto deve ser. Indica o comportamento e o funcionamento dele
- Desse modo, quando eu digo que estou criando uma instânciaa de uma classe, é como se tudo que eu defini eu pudesse encaixar em um objeto.
- A classe é a forma do nosso bolo e o objeto é o bolo que foi feito usando essa forma.
- Para uma única forma eu posso fazer bolos de diferente tipos como chocolate, morango e etc. 

  
    ```python
    # criando um primeiro objeto
    # posição, nome, idade, level, salário
    
    se1 = ["Engenheiro de Software", "Max", 20, "Junior", 5000]
    se2 = ["Engenheiro de Software", "Lisa", 25, "Sênior", 7000]

    # definindo uma classe
    class EngenheiroSoftware:
      def __init__(self, name, idade, level, salario):
      # instance atributes
        self.name = name
        self.idade = idade
        self.level = level
        self.salary = salario 

    # Criando uma instância 
    se1 = EngenheiroSoftware("Engenheiro de Software", "Max", 20, "Junior", 5000)
    print(se1.name, se1.age)

    ```
  ### Síntese
  - Criamos a classe Engenheiro de Software
  - Criamos a instância objeto (se1) que recebeu os atributos
  - Sabemos a diferença entre Classe e a Instância de uma Classe

  ### Utilização de funções em POO
   ```python
    # criando um primeiro objeto
    # posição, nome, idade, level, salário
    
    se1 = ["Engenheiro de Software", "Max", 20, "Junior", 5000]
    se2 = ["Engenheiro de Software", "Lisa", 25, "Sênior", 7000]

    # definindo uma classe
    class EngenheiroSoftware:
      def __init__(self, name, idade, level, salario):
      # instance atributes
        self.name = name
        self.idade = idade
        self.level = level
        self.salary = salario

   
     def code(self):
       print(f"{self.name} is writting code..."

    # Criando uma instância 
    se1 = EngenheiroSoftware("Engenheiro de Software", "Max", 20, "Junior", 5000)
    print(se1.name, se1.age)

   se1.code()
   # Max is writting code

    ```
  ### Under Métodos
   ```python
    # criando um primeiro objeto
    # posição, nome, idade, level, salário
    
    se1 = ["Engenheiro de Software", "Max", 20, "Junior", 5000]
    se2 = ["Engenheiro de Software", "Lisa", 25, "Sênior", 7000]

    # definindo uma classe
    class EngenheiroSoftware:
      def __init__(self, name, idade, level, salario):
      # instance atributes
        self.name = name
        self.idade = idade
        self.level = level
        self.salary = salario

   
     def code(self):
       print(f"{self.name} is writting code..."

     def __str__(self):
       information =  f"name = {self.name}

    # Criando uma instância 
    se1 = EngenheiroSoftware("Engenheiro de Software", "Max", 20, "Junior", 5000)
    print(se1.name, se1.age)

   se1.code()
   # Max is writting code

   print(se1)
   # retorna Max 

    ```
   - O funcionamento do __str__ funciona da seguinte forma. Quando       você passa um objeto para o print(), o Python chama
     automaticamente o método especial __str__() daquele objeto pars
     obter a string que deve ser exibida.
  
