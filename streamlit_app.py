import streamlit as st
import openai
import os

# Establecer la clave de API de OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_text(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.8
    )
    return response.choices[0].text.strip()

def main():
    st.title("Comparación de Filósofos")
    st.write("Esta aplicación compara las posiciones de varios filósofos sobre un problema dado.")

    # Definir la lista de filósofos
    filosofos = [
        "Platón", "Aristóteles", "San Agustín", "Santo Tomás de Aquino", "Guillermo de Ockham",
        "Descartes", "Locke", "Hume", "Hobbes", "Kant", "Hegel", "Marx", "Nietzsche",
        "Heidegger", "Wittgenstein", "Dewey", "Putnam", "Rorty"
    ]

    # Obtener el problema del usuario
    problema = st.text_input("Ingresa el problema que quieres comparar", "")

    if st.button("Comparar"):
        # Generar el texto de las posiciones de los filósofos utilizando el modelo text-davinci-003
        prompt = f"Problema: {problema}\n\nPosiciones de los filósofos:\n"
        for filosofo in filosofos:
            prompt += f"- {filosofo}: [Posición del filósofo]\n"

        posiciones = generate_text(prompt)

        # Mostrar las posiciones de los filósofos
        st.subheader("Posiciones de los Filósofos:")
        st.write(posiciones)

if __name__ == "__main__":
    main()
