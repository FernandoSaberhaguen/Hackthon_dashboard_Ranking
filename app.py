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
    st.subheader(title)

    # Gráfica del Score modelo
    chart_data = data.set_index('Name team')[['Score modelo']]
    st.line_chart(chart_data, use_container_width=True)

    # Gráfica de la STD añadida al Score modelo
    data['Score + STD'] = data['Score modelo'] + data['STD']
    st.line_chart(data.set_index('Name team')[['Score + STD']], use_container_width=True, color="orange")

    # Linea del threshold
    threshold = pd.DataFrame([0.90] * len(data), columns=['Threshold'], index=data['Name team'])
    st.line_chart(threshold, use_container_width=True, color="red")
    
st.write(data[['Name team', 'Score modelo', 'STD']])

# Gráfica Neural Network Model
plot_data(data, 'Neural Network Model Scores')
st.write('Neural Network Model Table')

# Gráfica Time Series Model 
plot_data(data, 'Time Series Model Scores')
st.write('Time Series Model Table')
st.write(data[['Name team', 'Score modelo', 'STD']])
