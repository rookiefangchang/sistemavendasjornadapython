# Importar a base de vendas
# titulo - Sistema de Vendas
# 3 Sessões: Cadastrar Vendas, Vendas Cadastradas, Secao Dashboard
#  Cadastrar Vendas
# 	- Campos:
# 		- Data
# 		- Vendedor: Ana, Bruno, Carla
# 		- Produto: Notebook, Fone, Celular
#       - Quantidade
#       - Valor
# 		- Botão de cadastrar a venda
# Vendas cadastradas
    # Tabela com as vendas
# Dashboard
    # Card/Metrica -> Faturamento Total
    # Grafico de Barra -> Venda por vendedor
    # Grafico de Pizza -> Venda por produto

import pandas as pd
import streamlit as st
import plotly.express as px

# Carregar a base de vendas
tabela_vendas = pd.read_csv("vendas.csv")

st.title("Sistema de Vendas")

st.sidebar.write("### Cadastro de Vendas")
data = st.sidebar.date_input("Data")
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Fernando"])
produto = st.sidebar.selectbox("Produto", ["Notebook", "Celular", "Fone"])
quantidade = st.sidebar.number_input("Quantidade", step=1)
valor = st.sidebar.number_input("Valor")
cadastrar_venda = st.sidebar.button("Cadastrar venda")

# Logica do cadastro

if(cadastrar_venda):
    if valor <= 0:
        st.warning("Favor preencher o valor da venda")
    elif quantidade <= 0:
        st.warning("Informe a quantidade")
    else:
        nova_venda = [str(data), vendedor, produto, quantidade, valor]
        ultima_linha_tabela = len(tabela_vendas)
        tabela_vendas.loc[ultima_linha_tabela] = nova_venda
        tabela_vendas.to_csv("vendas.csv", index=False)
        st.success("Venda registrada com sucesso!")


# Visualiação de vendas
st.write("### Vendas Cadastradas") 
st.dataframe(tabela_vendas)

# Criar um botao para filtrar através do ID da venda.
# id_venda = st.number_input("IO da Venda", step=1)
# botao_pesquisar = st.button("Pesquisar")

#Dashboard das vendas
st.write("### Dashboard")

#Card/Metrica -> Faturamento Total
faturamento = tabela_vendas["valor"].sum()
st.metric("Faturamento Total",f"R$ {faturamento:.2f}")

#Grafico de Barra
grafico_barra = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto")
st.plotly_chart(grafico_barra)

#Grafico de Pizza
grafico_pizza = px.pie(tabela_vendas, names="produto", values="valor", hole=0.025)
st.plotly_chart(grafico_pizza)

