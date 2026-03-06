import streamlit as st 
from sqlalchemy import create_engine, Column, String, Integer, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base

# Aba lateral
st.set_page_config(initial_sidebar_state='collapsed')

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
# Login 
st.title('Seja bem vindo á VendaGest')

nome_usuario = st.text_input('Digite seu nome: ')
senha_s = st.text_input('Digite sua senha: ', type=True)

if senha_s in ['pedro.code00', 'pedrox13'] and nome_usuario == 'pedro':
    st.session_state['logado'] = True
    st.switch_page('pages/principal.py')
else:
    st.error('Tente novamente, senha ou nome incorreto')


# Informações
st.write('### Sobre a VendaGest:')
st.write('-> A VendaGest é um site de gestão de vendas da sua empresa. Com pagamento de planos mensais parti de R$ 29,90')
st.write('-> Faça o cadastro da sua empresa para ter acesso a graficos e dashboards de dados da sua empresa.')
st.write('-> Para mais informações acesse nosso instagram. ')
st.caption('VendaGest v1.1')


# Banco de dados 
engine = create_engine('sqlite:///usuarios.db')
session = sessionmaker(bind=engine)
session = session()
base = declarative_base()

# Tabela
class Usuario(base):
    __tablename__ = 'usuarios'
    id = Column('id', Integer, primary_key=True)
    nome = Column('nome', String)
    senha = Column('senha', String)
    ativo = Column('ativo', Boolean)

    def __init__(self, nome, senha, ativo):
        self.nome = nome
        self.senha = senha
        self.ativo = ativo 


base.metadata.create_all(bind=engine)        

# Adicionar no banco de dados 
usuario1 = Usuario(nome=nome_usuario, senha=senha_s, ativo=True)
session.add(usuario1)
session.commit()

