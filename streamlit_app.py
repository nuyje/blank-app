import streamlit as st

animal_shelter = ['cat', 'dog', 'rabbit', 'bird']

# Initialiseer sessievariabele voor input
if "animal_input" not in st.session_state:
    st.session_state.animal_input = ""

# Tekstveld gekoppeld aan sessievariabele
animal = st.text_input('Type an animal', key="animal_input")

if st.button('Check availability'):
    if st.session_state.animal_input.lower() in animal_shelter:
        st.success('We have that animal!')  
    else:
        st.error('We don\'t have that animal.')

animal = ""
    

st.rerun()