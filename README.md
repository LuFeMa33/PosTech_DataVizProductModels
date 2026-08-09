# Verificador de Obesidade — Machine Learning

Projeto desenvolvido como parte da pós-graduação em Data Analytics, com o objetivo de aplicar técnicas de Machine Learning para classificação de diferentes níveis relacionados ao peso corporal.

A aplicação utiliza um modelo de Machine Learning treinado a partir de dados comportamentais e características físicas do indivíduo e disponibiliza uma interface interativa desenvolvida em Streamlit.

---

## Objetivo

O objetivo do projeto é desenvolver um modelo capaz de classificar um indivíduo em uma das seguintes categorias:

- Peso insuficiente
- Peso normal
- Sobrepeso Nível I
- Sobrepeso Nível II
- Obesidade Tipo I
- Obesidade Tipo II
- Obesidade Tipo III

A classificação é realizada a partir de características físicas, hábitos alimentares, atividade física e outros comportamentos relacionados ao estilo de vida.

> **Importante:** este projeto possui finalidade acadêmica e não deve ser utilizado como ferramenta de diagnóstico médico.

---

## Dataset

Foi utilizado o dataset **Obesity Dataset**, contendo informações relacionadas a características físicas e comportamentais dos indivíduos.

Entre as variáveis utilizadas estão:

- Idade
- Altura
- Peso
- Histórico familiar de obesidade
- Consumo de alimentos altamente calóricos
- Frequência de consumo de vegetais
- Número de refeições principais
- Tabagismo
- Consumo de água
- Monitoramento do consumo de calorias
- Frequência de atividade física
- Tempo de utilização de dispositivos eletrônicos
- Gênero
- Consumo de lanches entre refeições
- Consumo de bebidas alcoólicas
- Meio de transporte

---

## Tratamento dos dados

Durante o processo de preparação dos dados foram realizadas algumas etapas de tratamento:

- Conversão de variáveis categóricas em variáveis numéricas;
- Aplicação de One-Hot Encoding em variáveis categóricas;
- Criação de índices para algumas variáveis;
- Tratamento das variáveis booleanas;
- Análise da distribuição das variáveis;
- Análise de correlação;
- Avaliação de possíveis outliers;
- Separação dos dados em conjuntos de treinamento e teste.

A variável **IMC** foi inicialmente calculada durante a análise exploratória, porém posteriormente retirada das variáveis utilizadas no treinamento do modelo, evitando que uma variável diretamente derivada de peso e altura influenciasse excessivamente a classificação.

---

## Modelos avaliados

Foram avaliados diferentes algoritmos de classificação, incluindo:

- Decision Tree
- K-Nearest Neighbors (KNN)
- Gradient Boosting Classifier

Após a avaliação dos resultados, o modelo selecionado para a aplicação foi o:

### Gradient Boosting Classifier

O modelo apresentou desempenho superior aos demais modelos avaliados no conjunto de teste.

### Resultado

**Acurácia aproximada: 97%**

Além da classe prevista, a aplicação apresenta as probabilidades estimadas pelo modelo para cada uma das sete categorias.

---

## Importância das variáveis

Entre as variáveis que apresentaram maior importância para o modelo estão:

1. Peso
2. Altura
3. Frequência de consumo de vegetais
4. Índice de gênero
5. Idade
6. Consumo de bebidas alcoólicas
7. Consumo de água
8. Frequência de atividade física

A variável **Peso** apresentou a maior importância entre as features utilizadas pelo modelo.

---

## Aplicação

A aplicação foi desenvolvida utilizando **Streamlit**.

O usuário fornece informações como:

- Idade
- Gênero
- Altura
- Peso
- Histórico familiar
- Hábitos alimentares
- Consumo de água
- Atividade física
- Tabagismo
- Consumo de álcool
- Meio de transporte

Após o preenchimento, o modelo realiza a classificação e apresenta:

- Categoria prevista;
- Confiança da previsão;
- Probabilidade estimada para cada categoria.

---

## Estrutura do projeto

```text
PosTech_DataVizProductModels/
│
├── app_novo.py
├── modelo_gradient_boosting.joblib
├── colunas_modelo.joblib
├── Obesity.csv
├── requirements.txt
├── README.md
│
├── notebooks/
│   └── ...
│
└── imagens/
    └── ...
