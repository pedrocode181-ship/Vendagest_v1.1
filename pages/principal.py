import streamlit as st 

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

# Contatos
st.write('## Página principal')
st.write('## Contatos dos desenvolvedores: ')
st.write('Pedro Gabriel -> 81994317883 ')

numero_pedro = 81994317883

mensagem = 'Olá vim pelo seu site'

link = f'https://wa.me/{numero_pedro}?text={mensagem}'

st.link_button('Contato de Pedro', link)


# Àrea de acesso as proximas páginas 
st.write('### acesso para as proximas páginas:')
st.write('-> Click em um dos botões para trocar de página.')
if st.button('Página de calculo '):
    st.switch_page('pages/calculo.py')

if st.button('Dashboard geral.'):
    st.switch_page('pages/dashboard.py')