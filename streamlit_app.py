import streamlit as st
import openai
import os

# Obtener la clave de API de OpenAI desde una variable de entorno
api_key = os.getenv("OPENAI_API_KEY")


def main():
    st.title("Comparación de Filósofos")
    st.write("Esta aplicación compara las posiciones de varios filósofos sobre un problema dado.")

    # Definir la lista de filósofos
    filosofos = [
        "Platón", "Aristóteles", "San Agustín", "Santo Tomás de Aquino", "Guillermo de Ockham", "Duns Escoto",
        "Descartes", "Leibniz", "Spinoza", "Locke", "Hume", "Hobbes", "Kant", "Hegel", "Marx", "Nietzsche",
        "Heidegger", "Wittgenstein", "W. James", "Dewey", "Putnam", "Rorty", "Ayn Rand", "Derrida", "Foucault",
        "John Rawls", "Nozick", "Charles Taylor"
    ]

    # Obtener el problema del usuario
    problema = st.text_input("Ingresa el problema que quieres comparar", "")

    # Obtener los filósofos seleccionados por el usuario
    filosofos_seleccionados = st.multiselect("Selecciona los filósofos que quieres comparar", filosofos)

    if st.button("Comparar") and filosofos_seleccionados:
        st.subheader("Posiciones de los Filósofos:")
        for filosofo in filosofos_seleccionados:
            # Realizar llamada a la API de OpenAI para obtener la posición del filósofo actual
            respuesta = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Problema: {problema}\n\nFilósofo: {filosofo}",
                max_tokens=650,
                temperature=0.7,
                stop=None
            )

            # Mostrar la posición del filósofo actual
            st.write(f"- {filosofo}:")
            st.write(respuesta.choices[0].text.strip())

if __name__ == "__main__":
    main()
