import streamlit as st

animal_shelter = ['cat', 'dog', 'rabbit', 'bird']


# Functie om het invoerveld leeg te maken
def clear_input():
    st.session_state["animal_input"] = ""  # Zet de sessievariabele leeg

# Tekstveld wordt volledig beheerd via `st.session_state`
animal = st.text_input('Type an animal', key="animal_input")

if st.button('Check availability'):
    if st.session_state.animal_input.lower() in animal_shelter:
        st.success('We have that animal!')
    else:
        st.error('We don\'t have that animal.')

clear_input()

