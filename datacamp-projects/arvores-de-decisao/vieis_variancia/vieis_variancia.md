# Proposta

## 10 questões teóricas

Durante meus estudos de árvore de decisão. Aproveito para desenvolver 10 questões teóricas 
e 10 questões práticas. Nesse MD vocês verão questão teórica e no arquivo jupyter os exercícios
práticos

---
1. O que significa o erro de generalização em um modelo? Como ele se relaciona com o desempenho real do modelo?

* Resposta: Um erro de generalização ocorre na diferença de performace do modelo entre os dados de treino e os dados de teste. Trata-se da diferença de erros de teste e de treino.

---

2. Explique com um exemplo real o que é sobreajuste (overfitting) e por que isso é um problema.

* Resposta: O modelo com métricas de avaliação muito alta, como acurácia beirando a 100% indica que ele sabe prever aqueles dados de treinamento, entretanto, suas previsões não serão corretas ou assertivas com outros dados. 

Desse modo, ele tem baixo viés (se ajusta bem aos dados de treino), mas alta variância (não generaliza bem para novos dados)."

---

3. Explique o que é subajuste (underfitting) e por que modelos muito simples falham.

* Resposta: O underfiting já se enquadra no critério de uma falha de adaptação, ele não consegue processar ou lidar com os dados. Significa viés alto (modelo não aprende o padrão dos dados) e baixa variância (respostas muito semelhantes, mesmo para entradas diferentes).

---
4. Se um modelo tem alta variância, o que está acontecendo? Como você percebe isso nos dados?

* Resposta: Uma alta variância pode apontar um overfiting, uma ajustação elevada aos dados de treino, porém uma baixa adaptação aos dados de treino. 
---
5. Como a complexidade do modelo influencia o viés e a variância? Dê um exemplo de cada extremo.

* Resposta: A complexidade de um modelo ajuda a tornálo mais robusto, conseguindo chegar em um nível de equilíbrio entre variância e vièis. Modelos muito complexos, como árvores profundas, têm baixo viés e alta variância. A complexidade ideal busca um ponto de equilíbrio entre os dois."

---
6. Por que o uso de validação cruzada ajuda a diagnosticar problemas de viés e variância?

* Respota: A validação cruzada é uma técnica de repartição, em que pegamos os dados de treino e separams em blocos, e cada um dos blocos é passado para o modelo. Isso ajuda a medir como o modelo se comporta em relação a variância e ao vièis.

    * Erro da validação cruzada > erro de treino = alta variância -> baixo viéis = overfiting = ajuste aos dados de treino 

    * Erro de validação cruzada e erro de treino forem altos = baixa variância -> alto viéis -> underfiting -> não se adapta a nenhum dos dados
---
7. Explique com suas palavras o que é “agrupamento de modelos” (ensemble) e como isso reduz o erro.

* Resposta: O ensemble é uma técnica do sklearn que ajuda a refinar os modelos através da votação (para classificação) e da média para regressão. O agrupamento de modelo funciona semelhante a uma floresta aleatória de árvore de decisão, porém de diversos modelos diferentes, como KNN + REGRESSÃO LOGÍSTICA + ÁRVORE DE DECISÃO = Onde o rótulo previsto será aquele adotado pelo rótulo marjoritário dos outros modelos
---
8. Como um classificador de votação (voting classifier) pode ter melhor desempenho do que os classificadores individuais?

* Resposta: Um classificador de votação, utiliza da premissa de rótulos previstos pela classe marjoritária prevista pelos modelos. Exemplo 

        KNN = 1 
        Regressão Logistica = 0
        Decision Tree = 1 

        Rótulo final 1
---
9. Se você treinar 10 modelos diferentes e combiná-los, por que o resultado tende a ser mais estável?

* Resposta: Você está vendo diversas abordagens e métricas diferentes, tanto de classificação quanto de regressão. 
---
10. Por que não adianta aumentar a complexidade do modelo se os dados não têm sinal suficiente?

* Resposta: Acima de tudo, a matéria prima do modelo são dados de qualidade. Mesmo que o modelo seja refinado, isso não ajudaria se a qualidade dos dados forem ruins ou inclucusivos. 

---

## Conceitos de reforço 

### Variância -> 
    Variância é o quanto as previsões de um modelo mudam se ele for treinado com conjuntos de dados ligeiramente diferentes.

    Alta variância significa que o modelo é muito sensível aos dados de treino → decorando detalhes específicos → overfitting.

    Baixa variância: o modelo é mais estável, não muda tanto.

    Analogia simples:
    Imagine um amigo que muda de opinião toda vez que ouve alguém novo — ele tem "alta variância", é instável.

    Exemplo:
    Uma árvore de decisão profunda (sem limitação de profundidade) pode dar respostas completamente diferentes se mudarmos só 5% dos dados.


---

### Viéis
    Viés é o erro sistemático do modelo.

    Ocorre quando o modelo é simples demais para capturar os padrões dos dados.

    Ele generaliza de forma grosseira, simplificando demais o problema.

     Exemplo prático:
    Prever a felicidade de uma pessoa apenas com a idade dela. Isso é um modelo com alto viés: não está considerando outros fatores como saúde, relacionamentos, profissão etc.