import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from plotly import graph_objs as go

# Carregar variáveis de ambiente
load_dotenv()

db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")


def connect_to_db():
    # Formatar a string de conexão
    connection_string = (
        f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    )
    engine = create_engine(connection_string)
    return engine


def run_query(query, engine):
    with engine.connect() as conn:
        return pd.read_sql_query(query, conn)


def create_plot(df, plot_type):
    if plot_type == "bar":
        return go.Figure(data=[go.Bar(x=df["nome"], y=df["preco"])])
    elif plot_type == "line":
        return go.Figure(
            data=[go.Scatter(x=df.index, y=df["preco"], mode="lines+markers")]
        )
    elif plot_type == "scatter":
        return go.Figure(
            data=[go.Scatter(x=df["nome"], y=df["preco"], mode="markers")]
        )
    elif plot_type == "pie":
        return go.Figure(data=[go.Pie(labels=df["nome"], values=df["preco"])])



def main():
    st.title("Gerenciador de Produtos")

    engine = connect_to_db()
    query = "SELECT DISTINCT nome, preco FROM produtos ORDER BY preco DESC"
    df = run_query(query, engine)

    st.write("Produtos:")
    st.dataframe(df)

    uploaded_file = st.file_uploader("Carregar arquivo Excel", type="xlsx")
    if uploaded_file is not None:
        excel_data = pd.read_excel(uploaded_file)
        df = pd.concat([df, excel_data])  # Combinar com dados do banco
        df = df.nlargest(
            5, "preco"
        )  # Atualizar o DataFrame para o top 5 após concatenação

    st.write("Top 5 Produtos (Atualizado):")
    st.dataframe(df)

    plot_types = ["bar", "line", "scatter", "pie"]
    plot_type = st.selectbox("Selecione o tipo de gráfico", plot_types)
    plot = create_plot(df, plot_type)
    st.plotly_chart(plot)


if __name__ == "__main__":
    main()