import streamlit as st

animal_shelter = ['cat', 'dog', 'rabbit', 'bird']

if "animal_input" not in st.session_state:
    st.session_state.animal_input = ""

def clear_input():
    st.session_state["animal_input"] = ""

def check_availability(): 
    if animal.lower() in animal_shelter:
        st.success('We have that animal!')
    else:
        st.error('We don\'t have that animal.')

clear_input()

animal = st.text_input('Type an animal', key="animal_input", on_change=check_availability)



