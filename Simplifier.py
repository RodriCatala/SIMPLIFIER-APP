import streamlit as st
import openai
import os 
api_key= os.environ.get("API_KEY")

# Configurar la clave de API de OpenAI
openai.api_key = api_key  # Reemplaza con tu clave real

# Función para generar la receta
def generar_receta(ingredientes):
    prompt = f"Con los siguientes ingredientes, crea una receta fácil, detallando nombre y paso a paso en 100 tokens: {ingredientes}"

    messages = [
        {"role": "system", "content": "Eres un asistente de cocina."},
        {"role": "user", "content": prompt}
    ]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  
            messages=messages,
            max_tokens=120,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error al generar la receta: {e}"

# Interfaz con Streamlit
st.title("Asistente de Cocina 🍽️")

st.write("Ingresa los ingredientes disponibles en tu cocina.")

ingredientes = st.text_input("Ingredientes (ejemplo: huevo, pan, tomate):")

if st.button("Generar receta"):
    if ingredientes:
        receta = generar_receta(ingredientes)
        st.subheader("Receta Sugerida:")
        st.write(receta)
    else:
        st.warning("Por favor, ingresa algunos ingredientes.")

