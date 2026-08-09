# 🧠 Verificador de Obesidade — Machine Learning

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![Scikit Learn](https://img.shields.io/badge/Scikit--learn-1.6.1-orange?logo=scikit-learn)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![Status](https://img.shields.io/badge/Status-Concluído-success)

> Projeto acadêmico desenvolvido durante a pós-graduação em Data Analytics.

## 🚀 Aplicação

**[👉 Acessar o Verificador de Obesidade](https://verificador-obesidade.streamlit.app/)**

---

## 🎯 Objetivo

Este projeto tem como objetivo desenvolver um modelo de Machine Learning capaz de classificar indivíduos em diferentes categorias relacionadas ao estado nutricional, utilizando características físicas e comportamentais.

A aplicação permite que o usuário informe seus dados e receba:

- Categoria prevista pelo modelo;
- Confiança da previsão;
- Probabilidade estimada para cada uma das sete categorias.

> ⚠️ **Aviso:** este projeto possui finalidade exclusivamente acadêmica. Os resultados não devem ser utilizados como diagnóstico médico ou substituição de avaliação realizada por profissionais de saúde.

---

## 📊 Dataset

Foi utilizado o **Obesity Dataset**, contendo informações relacionadas às características físicas, hábitos alimentares, atividade física e outros comportamentos dos indivíduos.

Entre as variáveis utilizadas estão:

- Idade
- Altura
- Peso
- Gênero
- Histórico familiar de obesidade
- Consumo de alimentos altamente calóricos
- Frequência de consumo de vegetais
- Número de refeições principais
- Tabagismo
- Consumo de água
- Monitoramento do consumo de calorias
- Frequência de atividade física
- Tempo de utilização de dispositivos eletrônicos
- Consumo de lanches entre refeições
- Consumo de bebidas alcoólicas
- Meio de transporte

---

## 🔎 Tratamento dos dados

Durante o desenvolvimento foram realizadas etapas de análise exploratória e preparação dos dados para Machine Learning.

Entre os procedimentos realizados:

- Análise exploratória dos dados;
- Análise da distribuição das variáveis;
- Análise de correlação;
- Avaliação de valores discrepantes;
- Conversão de variáveis categóricas;
- Aplicação de One-Hot Encoding;
- Conversão de variáveis booleanas para valores numéricos;
- Criação de índices para algumas variáveis;
- Separação dos dados em conjuntos de treinamento e teste.

### IMC

Durante a análise exploratória, foi calculado o Índice de Massa Corporal (IMC) a partir das variáveis de peso e altura.

Entretanto, o IMC não foi utilizado no treinamento do modelo final. A decisão foi tomada porque o IMC é diretamente derivado de peso e altura e apresentou forte relação com a variável alvo.

Dessa forma, o modelo final utiliza as demais características disponíveis na base, sem incluir o IMC como variável de entrada.

---

## 🤖 Modelos avaliados

Foram testados diferentes algoritmos de classificação:

- Decision Tree
- K-Nearest Neighbors (KNN)
- Gradient Boosting Classifier

Após a comparação dos resultados, o **Gradient Boosting Classifier** foi selecionado para a aplicação.

---

## 📈 Resultado do modelo

O Gradient Boosting apresentou **aproximadamente 97% de acurácia no conjunto de teste** utilizado neste projeto.

Esse resultado foi superior ao desempenho observado nos demais modelos avaliados.

Além da acurácia, foram analisadas métricas como:

- Precision
- Recall
- F1-score
- Matriz de confusão

### Classification Report

O modelo apresentou desempenho elevado nas sete classes avaliadas, com destaque para as categorias:

- Obesity Type III
- Obesity Type II
- Overweight Level I
- Overweight Level II

A análise detalhada das métricas pode ser encontrada nos notebooks disponíveis neste repositório.

> **Importante:** a acurácia apresentada corresponde ao conjunto de teste utilizado durante o desenvolvimento. Esse resultado não representa necessariamente o desempenho do modelo em dados reais ou em uma população diferente daquela representada pelo dataset.

---

## 🌳 Importância das variáveis

A análise da importância das features indicou que as variáveis com maior influência na classificação foram:

| Variável | Importância aproximada |
|---|---:|
| Peso | 55,70% |
| Altura | 11,05% |
| Frequência de consumo de vegetais | 10,28% |
| Índice de gênero | 7,65% |
| Idade | 3,34% |
| Consumo de álcool | 2,83% |
| Consumo de água | 2,52% |
| Frequência de atividade física | 1,49% |

O **peso** foi a variável de maior importância no modelo, seguido pela altura e pela frequência de consumo de vegetais.

---

## 🖥️ Aplicação Streamlit

A interface da aplicação foi desenvolvida utilizando Streamlit.

O usuário fornece informações sobre:

- Idade;
- Gênero;
- Altura;
- Peso;
- Histórico familiar;
- Consumo de alimentos altamente calóricos;
- Consumo de vegetais;
- Número de refeições;
- Consumo de lanches;
- Tabagismo;
- Consumo de água;
- Monitoramento de calorias;
- Atividade física;
- Tempo utilizando dispositivos eletrônicos;
- Consumo de bebidas alcoólicas;
- Meio de transporte.

Após o preenchimento, o modelo realiza a classificação e apresenta a categoria mais provável.

A aplicação também apresenta a distribuição das probabilidades entre todas as categorias.

---

## 🧠 Funcionamento do modelo

O fluxo simplificado da aplicação é:

```text
Dados do usuário
       ↓
Tratamento das variáveis
       ↓
Conversão para o formato utilizado no treinamento
       ↓
Organização das 23 features
       ↓
Gradient Boosting Classifier
       ↓
Predição
       ↓
Probabilidade por categoria
       ↓
Resultado apresentado no Streamlit

📁 Estrutura do projeto

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

## ⚙️ Tecnologias utilizadas
Python 3.12
Pandas
NumPy
Scikit-learn
Joblib
Streamlit
Jupyter Notebook
Git
GitHub

## 📌 Principais versões utilizadas

O modelo foi treinado e posteriormente disponibilizado utilizando as seguintes versões:
Python:       3.12.13
NumPy:        2.0.2
Scikit-learn: 1.6.1
Joblib:       1.5.3

As versões de NumPy, Scikit-learn e Joblib foram fixadas no requirements.txt para manter a compatibilidade com o modelo serializado.

