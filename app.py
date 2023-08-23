import pandas as pd
import streamlit as st

# Función para cargar los datos
def load_data(file_name: str):
    return pd.read_csv(file_name, encoding='utf-8')

data = load_data('data.csv')

# Creando la interfaz de usuario con Streamlit
st.title('Ranking Team')

# Función para graficar los datos
def plot_data(data, title):
    chart = st.bar_chart(data.set_index("Name team")["Score modelo"])
    # Aquí tendrías que agregar la lógica para mostrar las líneas de STD, pero la API nativa de Streamlit no proporciona una forma fácil de hacerlo.
    # Si el STD es absolutamente necesario, es posible que necesites otra biblioteca (como bokeh o plotly) y que luego la integres con st.bokeh_chart o st.plotly_chart respectivamente.
    
# Gráfica Neural Network Model
st.write('Neural Network Model Table')
st.write(data[['Name team', 'Score modelo', 'STD']])
st.subheader('Neural Network Model')
plot_data(data, 'Neural Network Model Scores')

# Gráfica Time Series Model 
st.subheader('Time Series Model')
plot_data(data, 'Time Series Model Scores')
st.write('Time Series Model Table')
st.write(data[['Name team', 'Score modelo', 'STD']])
