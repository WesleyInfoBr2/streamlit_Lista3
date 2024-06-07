import pandas as pd
import streamlit as st
import ipeadatapy as ip
import matplotlib.pyplot as plt
import Projetos as main

st.markdown("# Projetos + Ipeadata")
st.sidebar.markdown("# Projetos + Ipeadata")

#cabeçalho
st.subheader("Uso combinado de dados em CSV e web")

st.write("Criação de duas variáveis do tipo lista e alimente com a série de dados do Projeto5 em uma e  com os valores da taxa Selic em outra")

code = '''df = main.carrega("https://raw.githubusercontent.com/WesleyInfoBr2/streamlit_Lista3/main/projetos.csv")
df1 = pd.DataFrame({'mes': [12], 'ano': [2023], 'Projeto1': [29376], 'Projeto2': [40392], 'Projeto3': [63648], 'Projeto4': [29376], 'Projeto5': [25704] })
df = pd.concat([df, df1])

selic = ip.timeseries('BM12_TJOVER12', yearGreaterThan=2020, yearSmallerThan=2023)
ListaP5 = list(df['Projeto5'])
ListaSelic = list(selic['VALUE ((% a.m.))'])
st.write(ListaP5)
st.write(ListaSelic)'''
st.code(code, language='python')

df = pd.read_csv("https://raw.githubusercontent.com/WesleyInfoBr2/streamlit_Lista3/main/projetos.csv", sep=";") 
df1 = pd.DataFrame({'mes': [12], 'ano': [2023], 'Projeto1': [29376], 'Projeto2': [40392], 'Projeto3': [63648], 'Projeto4': [29376], 'Projeto5': [25704] })
df = pd.concat([df, df1])

selic = ip.timeseries('BM12_TJOVER12', yearGreaterThan=2020, yearSmallerThan=2023)

ListaP5 = list(df['Projeto5'])
ListaSelic = list(selic['VALUE ((% a.m.))'])
st.write(ListaP5)
st.write(ListaSelic)

"---"  

st.write("Cálculo do VPL (Valor Presente Líquido) do Projeto5 com base na taxa Selic do período")

code = '''VP = 0
for i in range(0,24):
    VP = VP + (ListaP5[i] - (ListaP5[i] * (ListaSelic[i]/100) * i))
st.write('VPL do Projeto 5:', round(VP - 160000,2))'''
st.code(code, language='python')

VP = 0
for i in range(0,24):
    VP = VP + (ListaP5[i] - (ListaP5[i] * (ListaSelic[i]/100) * i))
st.write('VPL do Projeto 5:', round(VP - 160000,2))
