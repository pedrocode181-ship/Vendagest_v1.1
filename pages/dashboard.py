import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Aba lateral
st.set_page_config(initial_sidebar_state='collapsed')

# CSS PERSONALIZADO
st.markdown("""
<style>
.stApp {
    background-color: #0D0D0D;
    color: #E6EDF3;
}

div[data-testid="stMetric"] {
    background-color: #161B22;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #00FF88;
}

[data-testid="stDataFrame"] {
    background-color: #161B22;
}
</style>
""", unsafe_allow_html=True)

st.title("💰 Dashboard Financeiro")

# Layout principal
col1, col2 = st.columns([2,1])

# Gráfico principal
with col1:
    st.subheader("📊 Vendas Mensais")

    df = pd.DataFrame({
        "Mes": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"],
        "Vendas": [200, 150, 300, 250, 400, 220]
    })

    fig = px.bar(df, x="Mes", y="Vendas")

    fig.update_traces(marker_color="#00FF88")

    fig.update_layout(
        plot_bgcolor="#161B22",
        paper_bgcolor="#161B22",
        font_color="#E6EDF3"
    )

    st.plotly_chart(fig, use_container_width=True)

# Gauge verde
with col2:
    st.subheader("📈 Performance")

    fig2 = go.Figure(go.Indicator(
        mode="gauge+number",
        value=82,
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "#00FF88"},
        }
    ))

    fig2.update_layout(
        paper_bgcolor="#161B22",
        font_color="#E6EDF3"
    )

    st.plotly_chart(fig2, use_container_width=True)

# Métricas
st.markdown("## 📌 Indicadores")

m1, m2, m3 = st.columns(3)

m1.metric("💵 Total Vendas", "R$ 10,00")
m2.metric("📊 Lucro Líquido", "R$ 18.230")
m3.metric("👥 Clientes", "154")

# Tabela
st.markdown("## 🧾 Transações Recentes")

df2 = pd.DataFrame({
    "Cliente": ["Pedro", "Lucas", "Ana", "Carlos"],
    "Valor": ["R$ 500", "R$ 800", "R$ 300", "R$ 1.200"],
    "Status": ["Pago", "Pago", "Pendente", "Pago"]
})

st.dataframe(df2, use_container_width=True)

# Botão de voltar 
if st.button('Voltar'):
    st.switch_page('pages/principal.py')