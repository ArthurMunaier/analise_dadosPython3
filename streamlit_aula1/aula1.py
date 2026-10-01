
import streamlit as st
import pandas as pd

st.write("Olá, pessoal")

nome = "Arthur Munaier"  
idade = 18            

st.write("Meu nome é", nome, "e eu tenho", idade, "anos")

df = pd.DataFrame({
    'Matéria': ['Português', 'Matemática', 'Python', 'Frame'],
    'Nota': [8, 7, 10, 9]
})


st.title("Meu primeiro dash")

st.subheader(nome)

st.write(df)
