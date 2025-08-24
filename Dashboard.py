import streamlit as st
import pandas as pd
import plotly.express as px

# Dataset de ejemplo
df = px.data.gapminder()

# Título
st.set_page_config(page_title="🌍 Dashboard Interactivo", layout="wide")
st.title("🌍 Dashboard Interactivo con Streamlit")

# Sidebar para filtros
st.sidebar.header("Filtros")
continent = st.sidebar.selectbox("Selecciona un continente", df['continent'].unique())

# Filtrar datos
dff = df[df['continent'] == continent]

# Gráfico 1
fig1 = px.scatter(
    dff, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
    size="pop", color="country", hover_name="country", log_x=True, size_max=60,
    title=f"Evolución de {continent}", template="plotly_dark"
)

# Gráfico 2 (extra)
fig2 = px.line(
    dff.groupby(["year"])["lifeExp"].mean().reset_index(),
    x="year", y="lifeExp", title=f"Esperanza de vida promedio en {continent}", 
    template="plotly_dark"
)

# Layout del dashboard
col1, col2 = st.columns(2)
col1.plotly_chart(fig1, use_container_width=True)
col2.plotly_chart(fig2, use_container_width=True)

st.markdown("📊 **Datos interactivos en tiempo real con Streamlit + Plotly**")
