import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

with st.sidebar:
    st.title(" Identificação do Aluno")
    st.markdown("---")
    
    st.markdown("**Aluno: Gustavo Yvo")
    st.markdown("**Nº da Chamada: 16")
    st.markdown("**Turma: 3B2")
    st.markdown("**Disciplina: Python")
    st.markdown("---")
    st.caption("Utilize a seta no topo para recolher ou expandir esta barra de menu.")


    st.title(" Dashboard de Visualização de Dados")
    st.markdown("Acompanhamento e análise visual das métricas acadêmicas e operacionais.")
    st.markdown("---")

np.random.seed(42)

df_vendas = pd.DataFrame({
    'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
    'Vendas': [120, 150, 170, 160, 210, 240]
})

df_cursos = pd.DataFrame({
    'Curso': ['Python', 'SQL', 'Dashboards', 'Machine Learning'],
    'Alunos': [450, 300, 200, 150]
})

df_desempenho = pd.DataFrame({
    'Horas Estudo': np.random.randint(2, 20, 50),
    'Nota Final': np.random.randint(50, 100, 50)
})

df_satisfacao = pd.DataFrame({
    'Categoria': ['Excelente', 'Bom', 'Regular', 'Ruim'],
    'Quantidade': [55, 30, 10, 5]
})

df_presenca = pd.DataFrame({
    'Semana': [f'Semana {i}' for i in range(1, 9)],
    'Presença (%)': [95, 92, 88, 94, 96, 90, 93, 97]
})

df_projetos = pd.DataFrame({
    'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
    'Entregues': [5, 8, 12, 10, 15, 18],
    'Atrasados': [1, 2, 0, 3, 1, 0]
})

st.subheader("Bloco 1: Desempenho e Distribuição")

col1, col2, col3 = st.columns(3)

with col1:
        fig1 = px.line(df_vendas, x='Mês', y='Vendas', title='Evolução de Vendas/Acessos', markers=True)
        st.plotly_chart(fig1, use_container_width=True)
    
with col2:
        fig2 = px.bar(df_cursos, x='Curso', y='Alunos', color='Curso', title='Matrículas por Curso')
        st.plotly_chart(fig2, use_container_width=True)
    
with col3:
        fig3 = px.scatter(df_desempenho, x='Horas Estudo', y='Nota Final', title='Relação Estudo vs. Nota', trendline="ols")
        st.plotly_chart(fig3, use_container_width=True)
  
st.info("""
**Breve Análise dos Dados (Bloco 1):**
* **Gráfico 1:** Identifica-se uma tendência consistente de crescimento nas vendas/acessos ao longo do semestre, atingindo o pico no mês de Junho.
* **Gráfico 2:** O curso de *Python* é o líder absoluto de matrículas.
* **Gráfico 3:** Há uma correlação positiva clara entre a quantidade de horas dedicadas aos estudos e o aumento na nota final obtida pelos alunos.
""")

st.markdown("---")


st.subheader("Bloco 2: Engajamento e Indicadores")

col4, col5, col6 = st.columns(3)

with col4:
    fig4 = px.pie(df_satisfacao, values='Quantidade', names='Categoria', title='Índice de Satisfação', hole=0.4)
    st.plotly_chart(fig4, use_container_width=True)

with col5:
    fig5 = px.area(df_presenca, x='Semana', y='Presença (%)', title='Taxa de Presença Semanal')
    st.plotly_chart(fig5, use_container_width=True)

with col6:
    fig6 = px.bar(df_projetos, x='Mês', y=['Entregues', 'Atrasados'], title='Status dos Projetos Entregues', barmode='group')
    st.plotly_chart(fig6, use_container_width=True)


st.info("""
**Breve Análise dos Dados (Bloco 2):**
* **Gráfico 4:** A satisfação dos usuários é predominantemente positiva, onde mais de 85% das avaliações estão entre "Excelente" e "Bom".
* **Gráfico 5:** A taxa de presença em sala manteve-se alta e estável durante todas as 8 semanas, sempre acima da média de 88%.
* **Gráfico 6:** A produtividade das entregas de projetos aumentou significativamente a partir do mês de Março, mantendo os índices de atraso próximos de zero.
""")


