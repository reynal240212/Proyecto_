import streamlit as st

# Agregar CSS para estilizar los botones y los fondos
st.markdown("""
    <style>
        body {
            background-color: #f0f8ff;  /* Color de fondo */
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .stButton>button {
            background-color: #008CBA;  /* Botón azul */
            color: white;
        }
        .stButton>button:hover {
            background-color: #006F87;  /* Color del botón al pasar el mouse */
        }
    </style>
""", unsafe_allow_html=True)

# Título de la aplicación
st.title("🌟 Calculadora de Promedio Estudiantil 🌟")

# Ingresar nombre y calificaciones
nombre_completo = st.text_input('🔑 Ingresa tu nombre completo:')

# Calificaciones
calificaciones = []
materias = 5
for i in range(materias):
    calificacion = st.number_input(f'📚 Calificación Materia {i+1}:', min_value=0.0, max_value=10.0, step=0.1)
    calificaciones.append(calificacion)

# Botón para calcular
if st.button("🎯 Calcular Promedio"):
    if nombre_completo and all(calificaciones):
        promedio = sum(calificaciones) / materias
        st.success(f"**¡Hola {nombre_completo}!** El promedio es **{promedio:.2f}**")
    else:
        st.error("🚨 Por favor, completa todos los campos correctamente.")

