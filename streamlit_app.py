import streamlit as st

animal_shelter = ['cat', 'dog', 'rabbit', 'bird']

if "animal_input" not in st.session_state:
    st.session_state.animal_input = ""

def clear_input():
    st.session_state["animal_input"] = ""

clear_input()

st.text_input('Type an animal', key="animal_input")
animal = st.session_state.animal_input

if st.button('Check availability'):
    if animal.lower() in animal_shelter:
        st.success('We have that animal!')
    else:
        st.error('We don\'t have that animal.')

