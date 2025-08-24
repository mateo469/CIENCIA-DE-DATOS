import dash
from dash import dcc, html
from dash.dependencies import Input, Output   # <-- Importar correctamente
import plotly.express as px
import pandas as pd

# Dataset de ejemplo
df = px.data.gapminder()

# Inicializar la app
app = dash.Dash(__name__)

# Layout del dashboard
app.layout = html.Div([
    html.H1("🌍 Dashboard Interactivo - Gapminder", 
            style={'textAlign': 'center', 'color': '#2C3E50'}),

    html.Div([
        html.Label("Selecciona un continente:", style={'fontWeight': 'bold'}),
        dcc.Dropdown(
            id='dropdown-continent',
            options=[{'label': cont, 'value': cont} for cont in df['continent'].unique()],
            value='Americas',
            clearable=False,
            style={'width': '50%'}
        ),
    ], style={'padding': '20px'}),

    dcc.Graph(id='graph-scatter', style={'height': '70vh'}),

    html.Div("📊 Datos interactivos en tiempo real", 
             style={'textAlign': 'center', 'marginTop': '20px', 'fontSize': '18px'})
])

# Callback para actualizar gráfico
@app.callback(
    Output('graph-scatter', 'figure'),   # <-- corregido
    [Input('dropdown-continent', 'value')]  # <-- corregido
)
def update_graph(selected_continent):
    dff = df[df['continent'] == selected_continent]
    fig = px.scatter(
        dff, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
        size="pop", color="country", hover_name="country", log_x=True, size_max=60,
        template="plotly_dark", title=f"Evolución de {selected_continent}"
    )
    fig.update_layout(
        margin=dict(l=20, r=20, t=60, b=20),
        paper_bgcolor="#1E1E1E",
        font=dict(color="white")
    )
    return fig

if __name__ == '__main__':
    app.run(debug=True)
