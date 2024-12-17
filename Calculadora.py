import streamlit as st

# Título de la aplicación
st.title('Calculadora de Promedio')

# Ingresar nombre
nombre_completo = st.text_input('Ingresa tu nombre completo:')

# Ingresar calificaciones para 5 materias
calificaciones = []
materias = 5

for i in range(materias):
    calificacion = st.number_input(f'Ingrese la calificación de la materia {i+1}:', min_value=0.0, max_value=10.0, step=0.1)
    calificaciones.append(calificacion)

# Botón para calcular el promedio
if st.button('Calcular Promedio'):
    if nombre_completo and all(calificaciones):
        promedio = sum(calificaciones) / materias
        st.write(f'Nombre: {nombre_completo}')
        st.write(f'Promedio: {promedio:.2f}')
    else:
        st.error('Por favor, completa todos los campos.')

