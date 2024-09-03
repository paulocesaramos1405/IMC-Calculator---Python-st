import streamlit as st
import os

with st.sidebar:
    st.title("Calculadora de IMC")
    st.header("IMC: Definição?")
    st.write("Índice de Massa Corporal (IMC)")
    st.write("É um índice que relaciona peso e altura de uma pessoa, a fim de informar a qualidade da saúde de uma pessoa.")
    st.write("É utilizado como uma medida de saúde geral e para determinar se uma pessoa está com um peso ideal.")
  
st.title("Calculadora")

peso = st.number_input(label="Digite o seu peso em Kg", min_value=0.0, format="%.2f")

altura = st.number_input(label="Digite a sua altura em Metros", min_value=0.0, format="%.2f")

if st.button("Calcular"):
    if altura > 0: 
        imc = peso / (altura ** 2)
        imc_ideal = 21.7
        imc_delta = round(imc - imc_ideal, 2)

        if imc < 18.5:
            classe = 'Abaixo do peso!'
        elif 18.5 <= imc < 25:
            classe = 'Peso ideal!'
        elif 25 <= imc < 30:
            classe = 'Sobrepeso!'
        elif 30 <= imc < 40:
            classe = 'Obesidade!'
        else:
            classe = 'Obesidade mórbida'

        st.write(f"**Resultado:** {classe}")

        col1, col2 = st.columns(2)

        col1.metric("IMC Classificado", classe)     
        col2.metric("IMC Calculado", f"{round(imc, 2)}")     

        st.divider()
        st.text("Fonte: Academia da Nutrição")

        if os.path.exists("./tabelaimc.png"):
            st.image("./tabelaimc.png")
        else:
            st.error("Imagem 'tabelaimc.png' não encontrada!")
    else:
        st.error("Por favor, insira uma altura válida maior que 0.")