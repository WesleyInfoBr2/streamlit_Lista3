import streamlit as st

st.markdown("# Teste de widget")
st.sidebar.markdown("# Teste de widget")

st.subheader("Usando widget para interação com usuário")
x = st.slider('x') 
st.write('O quadrado de', x, 'é', x * x)

st.write("Também é possível mover o widget para a barra lateral")
st.write(" x = st.sidebar.slider('x') ")
