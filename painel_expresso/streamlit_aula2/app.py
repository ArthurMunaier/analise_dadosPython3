import streamlit as st

st.title("🚌 Expresso Mobilidade")
st.write("Painel do Operador")

# Identificação do operador
nome = st.text_input("Digite seu nome:")
if nome:
    st.write("Olá,", nome, "! Bom trabalho hoje 🚍")

linha = st.selectbox(
    "Escolha uma linha:",
    ["510", "520", "550"]
)
st.write("Linha selecionada:", linha)

horarios = {
    "510": "06:00 - 06:30 - 07:00",
    "520": "06:15 - 06:45 - 07:15",
    "550": "06:40 - 07:20 - 08:00",
}
st.write("Próximos horários:", horarios[linha])

linhas = st.multiselect(
    "Escolha as linhas:",
    ["510", "520", "550", "620"]
)
st.write(linhas)

if st.button("Calcular"):
    st.write("Calculando...")
    st.write("Linhas analisadas:", len(linhas))
    st.write("Ônibus necessários:", len(linhas) * 5)