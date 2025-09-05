import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os
os.system('cls')

#leer un atchivo que vamos a utilizar
df = pd.read_csv('accidentes.csv')

# Título
st.set_page_config(page_title="🌍 Dashboard Interactivo", layout="wide")
st.title("🌍 Dashboard Interactivo con Streamlit con archivo csv")