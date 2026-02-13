import streamlit as st

def index():
    st.header("Projeto de Análise de Dados", divider="gray")
    st.write("Página ainda em construção!")
    st.write("")
    with st.expander("Detalhes do Projeto"):
        st.write("Aqui está uma descrição mais detalhada...")


def page_2():
    st.write("Hello!")


def page_3():
    st.header("Extras", divider="red")
    st.write("Página ainda em construção!")


pages = {
    "":[st.Page(index, title="Página Principal")],
    "Análise Oscar": [
        st.Page("oscar_streamlit.py", title="Passo a Passo"),
        st.Page(page_2, title="Dashboard")
    ],
    "Outros": [
        st.Page(page_3, title="Extras")
    ],
}

pg = st.navigation(pages)
pg.run()