import streamlit as st
import openai
import pandas as pd
import os

# Obtener la clave de API de OpenAI desde una variable de entorno
api_key = os.getenv("OPENAI_API_KEY")



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

    # Obtener los filósofos seleccionados por el usuario
    filosofos_seleccionados = st.multiselect("Selecciona los filósofos que quieres comparar", filosofos)

    if st.button("Comparar") and filosofos_seleccionados:
        # Realizar llamada a la API de OpenAI para obtener las posiciones de los filósofos seleccionados
        respuestas = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Problema: {problema}\n\nFilósofos: {', '.join(filosofos_seleccionados)}",
            max_tokens=500,
            n=len(filosofos_seleccionados),
            temperature=0.6,
            stop=None
            
        )

        # Crear un DataFrame con los resultados
        data = {"Filósofo": filosofos_seleccionados, "Posición": [choice.text.strip() for choice in respuestas.choices]}
        df = pd.DataFrame(data)

        # Mostrar los resultados en una tabla
        st.subheader("Posiciones de los Filósofos:")
        st.dataframe(df)

if __name__ == "__main__":
    main()
