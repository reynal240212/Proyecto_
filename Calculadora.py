import streamlit as st

# Agregar CSS para estilizar los botones y los fondos
st.markdown("""
    <style>
        body {
            background-color: #f0f8ff;  /* Fondo suave y relajante */
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        .stButton>button {
            background-color: #4CAF50; /* Botón verde */
            color: white;
            padding: 12px 24px;
            font-size: 16px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Sombra sutil */
            transition: background-color 0.3s ease, transform 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: #45a049; /* Cambio de color al pasar el ratón */
            transform: scale(1.05); /* Efecto de expansión */
        }
        
        .stButton>button:active {
            background-color: #388E3C; /* Color al hacer clic */
        }
        
        .stTextInput>div>div>input {
            font-size: 18px;
            padding: 10px;
            border-radius: 5px;
            border: 2px solid #4CAF50; /* Borde verde */
        }
        
        .stTextInput>div>div>input:focus {
            border-color: #388E3C; /* Borde al hacer clic */
        }
        
        .stMarkdown {
            color: #333333;
            font-size: 18px;
        }

        .stSuccess {
            background-color: #e8f5e9;
            border-left: 4px solid #388E3C;
            color: #388E3C;
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

