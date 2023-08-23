import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Función para cargar los datos
def load_data(file_name: str):
    return pd.read_csv(file_name, encoding='utf-8')

data = load_data('data.csv')

# Creando la interfaz de usuario con Streamlit
st.title('Ranking Team')

# Función para graficar los datos
def plot_data(data, title):
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # Definir colores únicos para cada equipo
    colors = ['blue', 'green', 'red', 'purple', 'orange']
    
    # Crear el gráfico de dispersión con triángulos para cada equipo
    for idx, row in data.iterrows():
        ax.scatter(row['Name team'], row['Score modelo'], color=colors[idx], marker='^', s=100)
        ax.hlines(row['Score modelo'] + row['STD'], xmin=-0.5, xmax=4.5, color=colors[idx], linestyle='--')
    
    # Agregar la línea punteada roja para el threshold
    ax.hlines(0.90, xmin=-0.5, xmax=4.5, color='red', linestyle='--')
    ax.set_ylim(0.7, 1.0)
    ax.set_title(title)
    
    st.pyplot(fig)

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
