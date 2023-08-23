import pandas as pd
import streamlit as st

# Función para cargar los datos
def load_data(file_name: str):
    return pd.read_csv(file_name, encoding='utf-8')


data = load_data('data.csv')

# Creando la interfaz de usuario con Streamlit
st.title('Ranking Team')

# Gráfica Neural Network Model
st.write(data[['Name team', 'Score modelo']])
st.subheader('Neural Network Model')
st.bar_chart(data[['Name team', 'Score modelo']].set_index('Name team'))
st.write('Neural Network Model Table')

    
# Gráfica Time Series Model 
st.subheader('Time Series Model')
st.bar_chart(data[['Name team', 'Score modelo']].set_index('Name team'))
st.write('Time Series Model Table')
st.write(data[['Name team', 'Score modelo']])
