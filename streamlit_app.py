import streamlit as st

animal_shelter = ['cat', 'dog', 'rabbit', 'bird']

# Functie om het invoerveld te resetten
def clear_input():
    st.session_state.animal_input = ""  # Zet de waarde leeg
    st.rerun()  # Herstart de app zodat de wijziging zichtbaar wordt

# Initialiseer sessievariabele als die nog niet bestaat
if "animal_input" not in st.session_state:
    st.session_state.animal_input = ""

# Tekstveld ZONDER `value=`
animal = st.text_input('Type an animal', key="animal_input")

if st.button('Check availability'):
    if st.session_state.animal_input.lower() in animal_shelter:
        st.success('We have that animal!')
    else:
        st.error('We don\'t have that animal.')

    clear_input()  # Roep de functie aan om de invoer te wissen