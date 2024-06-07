import pandas as pd
import streamlit as st
import ipeadatapy as ip
import matplotlib.pyplot as plt

st.markdown("# Ipeadata")
st.sidebar.markdown("# Ipeadata")

#cabeçalho
st.subheader("Uso do pacote Ipeadata para análise de dados web")

st.write("Busca na base do IPEADATA indicadores relacionados a taxa de juros Selic")

code = '''@st.cache_data
def lista_kpi(termo):
    lista_selic = ip.list_series(termo)
    return lista_selic

lista_selic = lista_kpi('Selic')
st.dataframe(lista_selic)'''
st.code(code, language='python')

@st.cache_data
def lista_kpi(termo):
    lista_selic = ip.list_series(termo)
    return lista_selic

lista_selic = lista_kpi('Selic')
st.dataframe(lista_selic)

"---"  

st.write("Utilização da biblioteca do IPEADATA para apresentar os valores do indicador 'Taxa de juros - Over / Selic - acumulada no mês' dos anos de 2021 e 2022")

code = '''@st.cache_data
def lista_dados(termo, ano1, ano2):
    selic = ip.timeseries(termo, yearGreaterThan=ano1, yearSmallerThan=ano2)
    return selic

selic = lista_dados('BM12_TJOVER12', 2020, 2023)    
st.dataframe(selic)'''
st.code(code, language='python')


@st.cache_data
def lista_dados(termo, ano1, ano2):
    selic = ip.timeseries(termo, yearGreaterThan=ano1, yearSmallerThan=ano2)
    return selic

selic = lista_dados('BM12_TJOVER12', 2020, 2023)    
st.dataframe(selic)

"---"  

st.write("Geração de dois gráficos de linha, apresentando os meses e valores das taxas, para 2021 e 2022")

code = '''selic2021 = lista_dados('BM12_TJOVER12', 2020, 2022)
selic2022 = lista_dados('BM12_TJOVER12', 2021, 2023)
fig, ax = plt.subplots()
selic2021.plot("MONTH", "VALUE ((% a.m.))", ax=ax)
selic2022.plot("MONTH", "VALUE ((% a.m.))", ax=ax)
st.pyplot(fig)'''
st.code(code, language='python')

selic2021 = lista_dados('BM12_TJOVER12', 2020, 2022)
selic2022 = lista_dados('BM12_TJOVER12', 2021, 2023)
fig, ax = plt.subplots()
selic2021.plot("MONTH", "VALUE ((% a.m.))", ax=ax)
selic2022.plot("MONTH", "VALUE ((% a.m.))", ax=ax)
st.pyplot(fig)


"---"  

st.write("Utilização da função `st.columns` e do método `metric` para apresentar medidas de forma mais amigável")

code = '''col1, col2 = st.columns(2)
col1.metric("2021", selic2021["VALUE ((% a.m.))"].mean(), "-10%")
col2.metric("2022", selic2022["VALUE ((% a.m.))"].mean(), "269%")'''
st.code(code, language='python')

col1, col2 = st.columns(2)
col1.metric("2021", selic2021["VALUE ((% a.m.))"].mean(), "-10%")
col2.metric("2022", selic2022["VALUE ((% a.m.))"].mean(), "269%")