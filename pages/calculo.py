import streamlit as st
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

# botão de voltar
if st.button('Voltar'):
    st.switch_page('pages/principal.py')

st.write('## Página de calculo ')

orçamento = st.number_input('Orçamento: ')
custos = st.number_input('Digite o valor em custos: ')
lucro = st.number_input('Digite aproximadamente o seu lucro: ')

lucro_total = orçamento - custos + lucro 

if lucro_total > custos : 
    st.success('Seu lucro foi positivo.')

else:
    st.error('Seu lucro foi negativo.')

st.write('lucro foi de: ', lucro_total)   