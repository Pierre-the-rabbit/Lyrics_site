import requests
import streamlit as st

#funções
def buscar_letra(banda,musica):
    endpoint = f"https://api.lyrics.ovh/v1/{banda}/{musica}"
    response = requests.get(endpoint)
    letra = response.json()["lyrics"] if response.status_code == 200 else ""
    return letra
st.image("https://i.imgur.com/SmktDIH.png")
#titulo
st.title("Letras de músicas")
#inserir nome e musica da banda
banda = st.text_input("Digite o nome da banda: ", key="banda")
musica = st.text_input("Digite o nome da música:",key="musica")
#botao de pesquisa
pesquisar = st.button("Pesquisar")
#condição de pesquisa
if pesquisar:
    letra = buscar_letra(banda,musica)
    if letra:
        st.success("Encontramos a letra da sua música")
        st.text(letra)
    else:
        st.error("Infelizmeente não foi possivel encontrar a letra dessa musica")


