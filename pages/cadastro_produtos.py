import streamlit as st 
import pandas as pd 
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Aba lateral
st.set_page_config(initial_sidebar_state='collapsed')

# Segurança
if "logado" not in st.session_state or not st.session_state["logado"]:
    st.switch_page("login.py")  # Se não estiver logado, volta pro login

# Cores
st.markdown("""
<style>
            .stApp{
            background:
linear-gradient(to right, 
#32CD32, #E3F2FD);
            } 
            </style>
""", unsafe_allow_html=True)

# Página (intrdução)
if st.button('Voltar'):
    st.switch_page('pages/principal.py')
st.write('## Cadastro de produtos.')
st.write('Digite as informações desejadas e click no botão para cadastrar o produto')

nome_produto = st.text_input('Digite o nome do produto: ')
valor_produto = st.number_input('Digite o valor da compra do produto: ')
venda_produto = st.number_input('Digite o valor da venda do produto: ')
quantidade = st.text_input('Digite a quantidade do produto')

# Banco de dados dos produtos
engine = create_engine('sqlite:///produtos.db')
session = sessionmaker(bind=engine)
session = session()
base = declarative_base()

# Tabela do banco de dados
class Produtos(base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    produto = Column('nome do produto', String)
    valor = Column('valor da compra ', Integer)
    venda = Column('valor venda', Integer)
    estoque = Column('quantidade', String)

    def __init__(self, produto, valor, venda, estoque):
        self.produto = produto
        self.valor = valor
        self.venda = venda
        self.estoque = estoque 

base.metadata.create_all(bind=engine)       

# cadastrar os produtos
if st.button('Cadastrar o produto'):
    produto_cadastrado = Produtos(produto=nome_produto, valor=valor_produto, venda=venda_produto, estoque=quantidade)
    session.add(produto_cadastrado)
    session.commit()

# Tabela de produtos cadastrados
produtos = session.query(Produtos).all()

dados = []

for produto in produtos:
    dados.append({
        "ID": produto.id,
        "Nome": produto.produto,
        "Valor Compra": produto.valor,
        "Valor Venda": produto.venda,
        'Quantidade do produto': produto.estoque
    })

df = pd.DataFrame(dados)

# Pesquisa
st.write("### Pesquisar Produto")

pesquisa = st.text_input("Digite o nome do produto")

if pesquisa:
    df = df[df["Nome"].str.contains(pesquisa, case=False)]

# Mostrar tabela
st.write("### Tabela de Produtos")
st.dataframe(df)

# Deletar produto
st.write("### Deletar Produto")

id_delete = st.number_input("ID do produto para deletar", step=1)

if st.button("Deletar"):
    
    produto = session.query(Produtos).filter(Produtos.id == id_delete).first()
    
    if produto:
        session.delete(produto)
        session.commit()
        st.success("Produto deletado!")
    else:
        st.error("Produto não encontrado")