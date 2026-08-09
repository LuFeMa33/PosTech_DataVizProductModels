import streamlit as st
import pandas as pd
import joblib


# =========================================================
# CARREGAMENTO
# =========================================================

dados = pd.read_csv(
    'https://raw.githubusercontent.com/LuFeMa33/PosTech_DataVizProductModels/refs/heads/main/Obesity.csv'
)

modelo = joblib.load('modelo_gradient_boosting.joblib')

colunas_modelo = joblib.load('colunas_modelo.joblib')


# =========================================================
# TÍTULO
# =========================================================

st.title('🔎 Verificador de Obesidade')

st.write(
    'Preencha as informações abaixo para que o modelo '
    'realize a classificação.'
)


# =========================================================
# ENTRADAS DO USUÁRIO
# =========================================================

st.write('### Idade')

input_idade = float(
    st.slider(
        'Selecione sua idade',
        18,
        100
    )
)


st.write('### Gênero')

input_genero = st.selectbox(
    'Escolha seu gênero',
    dados['Gender'].unique()
)


st.write('### Altura')

input_altura = float(
    st.number_input(
        'Digite sua altura em metros (ex.: 1.75)',
        min_value=1.00,
        max_value=2.50,
        value=1.70,
        step=0.01
    )
)


st.write('### Peso')

input_peso = float(
    st.number_input(
        'Digite seu peso em quilogramas (ex.: 75.0)',
        min_value=20.0,
        max_value=300.0,
        value=75.0,
        step=0.1
    )
)


st.write('### Histórico Familiar')

input_historico_familiar = st.selectbox(
    'Tem histórico familiar de obesidade?',
    dados['family_history'].unique()
)


st.write('### Consumo de Calorias')

input_consumo_calorias = st.selectbox(
    'Faz consumo frequente de alimentos muito calóricos?',
    dados['FAVC'].unique()
)


st.write('### Consumo de Vegetais')

input_consumo_vegetais = st.selectbox(
    'Faz consumo frequente de vegetais nas refeições?',
    ['raramente', 'às vezes', 'sempre']
)

input_consumo_vegetais_dict = {
    'raramente': 1,
    'às vezes': 2,
    'sempre': 3
}

input_consumo_vegetais = input_consumo_vegetais_dict[
    input_consumo_vegetais
]


st.write('### Refeições por dia')

input_refeicoes_diarias = st.selectbox(
    'Faz quantas refeições por dia?',
    [
        '1 refeição',
        '2 refeições',
        '3 refeições',
        '4 ou mais'
    ]
)

input_refeicoes_diarias_dict = {
    '1 refeição': 1,
    '2 refeições': 2,
    '3 refeições': 3,
    '4 ou mais': 4
}

input_refeicoes_diarias = input_refeicoes_diarias_dict[
    input_refeicoes_diarias
]


st.write('### Consumo de Lanches')

input_consumo_lanches = st.selectbox(
    'Faz consumo frequente de lanches?',
    dados['CAEC'].unique()
)


st.write('### Fumante')

input_fumante = st.selectbox(
    'É fumante?',
    dados['SMOKE'].unique()
)


st.write('### Consumo de Água')

input_consumo_agua = st.selectbox(
    'Faz consumo frequente de água?',
    [
        '< 1 L/Dia',
        '1-2 L/Dia',
        '> 2 L/Dia'
    ]
)

input_consumo_agua_dict = {
    '< 1 L/Dia': 1,
    '1-2 L/Dia': 2,
    '> 2 L/Dia': 3
}

input_consumo_agua = input_consumo_agua_dict[
    input_consumo_agua
]


st.write('### Monitoramento de Calorias')

input_monitoramento_calorias = st.selectbox(
    'Faz monitoramento frequente de calorias?',
    dados['SCC'].unique()
)


st.write('### Frequência Semanal de Atividade Física')

input_frequencia_atividade_fisica = st.selectbox(
    'Faz atividade física regularmente?',
    [
        'nenhuma',
        '~1-2x/sem',
        '~3-4x/sem',
        '5x/sem ou mais'
    ]
)

input_frequencia_atividade_fisica_dict = {
    'nenhuma': 0,
    '~1-2x/sem': 1,
    '~3-4x/sem': 2,
    '5x/sem ou mais': 3
}

input_frequencia_atividade_fisica = (
    input_frequencia_atividade_fisica_dict[
        input_frequencia_atividade_fisica
    ]
)


st.write('### Tempo diário utilizando dispositivos eletrônicos')

input_tempo_dispositivos = st.selectbox(
    'Quanto tempo gasta diariamente utilizando dispositivos eletrônicos?',
    [
        '0-2h/dia',
        '3-5h/dia',
        '> 5h/dia'
    ]
)

input_tempo_dispositivos_dict = {
    '0-2h/dia': 0,
    '3-5h/dia': 1,
    '> 5h/dia': 2
}

input_tempo_dispositivos = input_tempo_dispositivos_dict[
    input_tempo_dispositivos
]


st.write('### Consumo de Bebidas Alcoólicas')

input_consumo_bebidas_alcoolicas = st.selectbox(
    'Faz consumo frequente de bebidas alcoólicas?',
    dados['CALC'].unique()
)


st.write('### Meio de transporte')

input_meio_transporte = st.selectbox(
    'Qual o principal meio de transporte utilizado?',
    dados['MTRANS'].unique()
)


# =========================================================
# CRIAÇÃO DO DATAFRAME
# =========================================================

dados_usuario = pd.DataFrame({
    'Idade': [input_idade],
    'Altura': [input_altura],
    'Peso': [input_peso],

    'historico_familiar': [
        1 if input_historico_familiar == 'yes' else 0
    ],

    'frequencia_consumo_alta_caloria': [
        1 if input_consumo_calorias == 'yes' else 0
    ],

    'frequencia_consumo_vegetais': [
        input_consumo_vegetais
    ],

    'numero_refeicoes_principais': [
        input_refeicoes_diarias
    ],

    'fumante': [
        1 if input_fumante == 'yes' else 0
    ],

    'consumo_agua': [
        input_consumo_agua
    ],

    'monitoramento_consumo_calorias': [
        1 if input_monitoramento_calorias == 'yes' else 0
    ],

    'frequencia_atividade_fisica': [
        input_frequencia_atividade_fisica
    ],

    'tempo_uso_dispositivos_eletronicos': [
        input_tempo_dispositivos
    ],

    'Indice_Genero': [
        1 if input_genero == 'Male' else 0
    ]
})


# =========================================================
# ONE-HOT ENCODING
# =========================================================

# Lanches

dados_usuario[
    'consumo_lanches_entre_refeicoes_Frequently'
] = (
    1 if input_consumo_lanches == 'Frequently' else 0
)

dados_usuario[
    'consumo_lanches_entre_refeicoes_Sometimes'
] = (
    1 if input_consumo_lanches == 'Sometimes' else 0
)

dados_usuario[
    'consumo_lanches_entre_refeicoes_no'
] = (
    1 if input_consumo_lanches == 'no' else 0
)


# Álcool

dados_usuario[
    'consumo_alcool_Frequently'
] = (
    1 if input_consumo_bebidas_alcoolicas == 'Frequently' else 0
)

dados_usuario[
    'consumo_alcool_Sometimes'
] = (
    1 if input_consumo_bebidas_alcoolicas == 'Sometimes' else 0
)

dados_usuario[
    'consumo_alcool_no'
] = (
    1 if input_consumo_bebidas_alcoolicas == 'no' else 0
)


# Meio de transporte

dados_usuario[
    'meio_transporte_Bike'
] = (
    1 if input_meio_transporte == 'Bike' else 0
)

dados_usuario[
    'meio_transporte_Motorbike'
] = (
    1 if input_meio_transporte == 'Motorbike' else 0
)

dados_usuario[
    'meio_transporte_Public_Transportation'
] = (
    1 if input_meio_transporte == 'Public_Transportation' else 0
)

dados_usuario[
    'meio_transporte_Walking'
] = (
    1 if input_meio_transporte == 'Walking' else 0
)


# =========================================================
# ORGANIZAÇÃO DAS FEATURES
# =========================================================

dados_usuario = dados_usuario.reindex(
    columns=colunas_modelo,
    fill_value=0
)


# =========================================================
# CLASSES
# =========================================================

classes_obesidade = {
    0: 'Insufficient_Weight',
    1: 'Normal_Weight',
    2: 'Obesity_Type_I',
    3: 'Obesity_Type_II',
    4: 'Obesity_Type_III',
    5: 'Overweight_Level_I',
    6: 'Overweight_Level_II'
}


# =========================================================
# PREVISÃO
# =========================================================

if st.button('🔎 Verificar'):

    previsao = modelo.predict(dados_usuario)[0]

    probabilidades = modelo.predict_proba(
        dados_usuario
    )[0]

    confianca = probabilidades.max()

    nome_classe = classes_obesidade[previsao]

    st.success(
        f'### Resultado: {nome_classe}'
    )

    st.metric(
        'Confiança do modelo',
        f'{confianca:.2%}'
    )

    # ---------------------------------------------
    # Probabilidades
    # ---------------------------------------------

    resultado_probabilidades = pd.DataFrame({
        'Classe': [
            classes_obesidade[i]
            for i in range(len(probabilidades))
        ],
        'Probabilidade': probabilidades
    })

    resultado_probabilidades[
        'Probabilidade'
    ] = (
        resultado_probabilidades[
            'Probabilidade'
        ] * 100
    ).round(2)

    st.write(
        '### Probabilidade por categoria'
    )

    st.dataframe(
        resultado_probabilidades,
        hide_index=True
    )