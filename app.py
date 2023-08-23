import pandas as pd
import streamlit as st
import plotly.graph_objects as go

# Función para cargar los datos
def load_data(file_name: str):
    return pd.read_csv(file_name, encoding='utf-8')

data = load_data('data.csv')

# Creando la interfaz de usuario con Streamlit
st.title('Ranking Team')

# Función para graficar los datos
def plot_data(data, title):
    # Definir colores únicos para cada equipo
    colors = ['blue', 'green', 'red', 'purple', 'orange']
    
    # Crear el gráfico de dispersión con triángulos para cada equipo
    fig = go.Figure()
    
    for idx, row in data.iterrows():
        fig.add_trace(go.Scatter(x=[row['Name team']], 
                                 y=[row['Score modelo']],
                                 mode='markers',
                                 marker=dict(symbol='triangle-up', 
                                             size=15, 
                                             color=colors[idx]),
                                 name=row['Name team']))
        
        fig.add_shape(go.layout.Shape(
            type="line",
            x0=row['Name team'],
            y0=row['Score modelo'],
            x1=row['Name team'],
            y1=row['Score modelo'] + row['STD'],
            line=dict(color=colors[idx], dash="dash")
        ))
        
    # Agregar la línea punteada roja para el threshold
    fig.add_shape(go.layout.Shape(
            type="line",
            x0=data['Name team'].iloc[0],
            y0=0.90,
            x1=data['Name team'].iloc[-1],
            y1=0.90,
            line=dict(color='red', dash="dash")
        ))
    
    fig.update_layout(title=title, 
                      yaxis_range=[0.7, 1.0], 
                      xaxis_title='Team',
                      yaxis_title='Score',
                      showlegend=True,
                      gridcolor="gray")
    
    st.plotly_chart(fig)

st.write(data[['Name team', 'Score modelo', 'STD']])

# Gráfica Neural Network Model
st.subheader('Neural Network Model')
plot_data(data, 'Neural Network Model Scores')
st.write('Neural Network Model Table')

# Gráfica Time Series Model 
st.subheader('Time Series Model')
plot_data(data, 'Time Series Model Scores')
st.write('Time Series Model Table')
st.write(data[['Name team', 'Score modelo']])
