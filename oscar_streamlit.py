import pandas as pd
import streamlit as st


st.header("Análise de Dados | Passo a Passo", divider=True)

st.write("Este projeto..... Confira na página principal.")

st.subheader("1. Entendendo os dados e suas limitações", divider="gray")

st.markdown("""O primeiro passo é abrir os conjuntos de dados.

Na base de dados utilizada, temos dois arquivos:

- `full_data.csv`:
- `the_oscar_award.csv`:
""")

st.write("Vamos começar abrindo o arquivo `full_data.csv` pelo OnlyOffice antes de abrir pelo Pandas. O programa irá nos informar algumas coisas interessantes, a começar pela formatação dos dados:")


left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image("fulldata_onlyoffice.png", caption="Abrindo o arquivo `full_data.csv` pelo OnlyOffice.")

st.markdown("""Há algumas coisas interessantes a se apontar sobre este procedimento:

- :red[Limitações de programa:] este procedimento **NÃO** é útil para bases de dados muito grandes, que exigem maior poder de processamento para sequer carregar no seu programa de planilha comparados a uma operação direta pelo Pandas/Python;
- :red[Amplitude de conteúdo]: apesar do Pandas conter funções como `head()`, `tail()` ou `sample()` para procurar por linhas da tabela, utilizando um programa de planilha se tem uma praticidade muito maior de analisar os dados de um número muito maior de colunas.""")

st.write("Agora abriremos o mesmo arquivo pelo Pandas utilizando a referência que nos foi dada:")

st.code("""import pandas as pd
df = pd.read_csv("full_data.csv", encoding="utf-8", sep="\ t")""", language="python")


df = pd.read_csv("full_data.csv", encoding="utf-8", sep='\t')

st.write(f"Número de linhas e colunas: `{df.shape}`")
st.dataframe(df, hide_index=True)


st.write("Utilizando o método `describe`:")
df_describe = df.describe(include='all').fillna("").astype("str")
st.write(df_describe)



st.write("Faremos o mesmo procedimento para o arquivo `the_oscar_award.csv`, para checar as diferenças entre as duas bases de dados:")

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image("the_oscar_award_onlyoffice.png", caption="Abrindo o arquivo `the_oscar_award.csv` pelo OnlyOffice.")

st.code("""import pandas as pd
df = pd.read_csv("the_oscar_award.csv", encoding="utf-8", sep=",")""", language="python")

df2 = pd.read_csv("the_oscar_award.csv", encoding="utf-8", sep=',')

st.write(f"Número de linhas e colunas: `{df2.shape}`")
st.dataframe(df2, hide_index=True)

st.write("Utilizando o método `describe`:")
df2_describe = df2.describe(include='all').fillna("").astype("str")
st.write(df2_describe)


st.html("""<h2>Conclusão da análise prévia dos dados</h2>
Podemos, a partir disso, coletar algumas informações importantes e já tomar algumas decisões de acordo com algumas colunas:""")

st.write("""
| Coluna | Ajuste |
| --- | --- |
| `Year` | A coluna no arquivo `full_data.csv` não possui uma formatação correta de data para o Pandas, somente indicando a referência de qual evento do Oscar se tratou. |
| `name` e `film` | O arquivo `full_data.csv` possui mais nomes de indicados e de filmes presentes do que `the_oscar_award.csv`. Isso precisará ser analisado para entender e padronizar as informações entre as duas tabelas. Além disso, há dados vazios nestas colunas em ambas bases de dados. |
| `note` | Algumas informações de grande revelância para alguns dos conflitos com as colunas `name` e `film` estão descritos nesta coluna. |
""")

st.subheader("2. Tratando os dados da planilha", divider="gray")

st.write("""Vamos começar tentando padronizar os dados das colunas `year` e `film`. O objetivo é termos o mesmo número de linhas entre as duas bases após removermos os valores vazios e outras alterações.

Para isso, fazemos:""")

st.code('print("Olá, mundo!")', language="python")

st.dataframe(df.dropna(axis=0, subset=["Name", "Film"]).reset_index())
st.dataframe(df2.dropna(axis=0, subset=["name", "film"]).reset_index())

st.write("Verificando as notas...")
st.dataframe(df[["Year", "Category", "Film", "Name", "Note"]].dropna(subset=["Note", "Film", "Name"]))
st.dataframe(df2[["year_ceremony", "category", "film", "name"]].dropna(subset=["film", "name"]))

st.html("""<br><br><br><br><br><br>
<details>r
<summary>How do I dropdown?</summary>
<br>
This is how you dropdown.
</details>
""")