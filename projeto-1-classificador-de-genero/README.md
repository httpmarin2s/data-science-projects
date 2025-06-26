# Classificador de Gênero com Python e Scikit-learn

Este projeto é uma implementação educacional de um **classificador de gênero (Masculino/Feminino)** com base em características físicas (altura, peso e número do sapato). Inspirado pela série de vídeos do canal **Siraj Raval** no YouTube, este notebook demonstra o uso de bibliotecas como `pandas`, `numpy` e `scikit-learn` para criação de um modelo de *Machine Learning supervisionado* com árvore de decisão.

🎥 Vídeo de referência: [YouTube - Siraj Raval](https://youtu.be/T5pRlIbr6gg?si=FK3fOr4En3J5E95j)

---

## 📌 Objetivo

Construir um modelo simples de Machine Learning capaz de classificar uma pessoa como **homem (1)** ou **mulher (0)** com base em:

- Altura (cm)
- Peso (kg)
- Tamanho do sapato (número BR)

---

## 🔧 Tecnologias e Bibliotecas Utilizadas

- Python 3.x
- `NumPy`
- `Pandas`
- `Matplotlib`
- `Scikit-learn`

---

## ⚙️ Etapas do Projeto

### 1. **Preparação do ambiente**
Importação de bibliotecas essenciais e definição dos parâmetros.

### 2. **Geração de dados simulados**
Criação de dados fictícios com distribuição normal para representar amostras de homens e mulheres.

```python
# Exemplo:
peso_mulher = np.random.normal(loc=60, scale=5, size=500)
```

### 3. **Mesclagem e rotulagem dos dados**
Concatenamos os dados de altura, peso e sapato, e aplicamos os rótulos:
- `0` para mulheres
- `1` para homens

### 4. **Criação do DataFrame**
Transformamos os dados em um `pandas.DataFrame`, tratando e arredondando valores.

### 5. **Separação dos dados**
Separação entre `features` (X) e `target` (y), com divisão em treino e teste (70%/30%).

### 6. **Treinamento do modelo**
Utilização do algoritmo `DecisionTreeClassifier` para treinar o modelo.

```python
modelo = DecisionTreeClassifier()
modelo.fit(X_train, y_train)
```

### 7. **Avaliação**
Avaliação do modelo com *classification report* e matriz de confusão.

Resultado típico:
```
accuracy: 94%
precision: 94%
recall: 94%
```

### 8. **Visualização**
Exibição gráfica da árvore de decisão e da matriz de confusão.

```python
plot_tree(modelo, ...)
ConfusionMatrixDisplay(...)
```

### 9. **Predição com novos dados**
Entrada de dados pelo usuário e classificação com base no modelo treinado.

```python
vetor = np.array([altura, peso, sapato]).reshape(1, -1)
previsao = modelo.predict(vetor)
```

---

## ✅ Exemplo de uso

```text
Digite o seu nome: Marianna
Digite a sua altura: 160
Digite o seu peso: 60
Digite o tamanho do seu sapato: 36
```

Resultado:
```
[0]
0 = Mulher; 1 = Homem
```

---

## 📁 Estrutura do Projeto

```
classificador_de_genero.ipynb
README.md
```

---

## 📚 Créditos

Este projeto é baseado nos ensinamentos de [Siraj Raval](https://www.youtube.com/@SirajRaval), com adaptações para fins didáticos.

---

## 📌 Observações

- Os dados utilizados são **sintéticos** e gerados de forma **aleatória**.
- O objetivo é apenas **educacional**, não sendo recomendado para aplicações reais sem ajustes e validações adequadas.
