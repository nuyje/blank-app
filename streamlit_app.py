import streamlit as st

animal_shelter = ['cat', 'dog', 'rabbit', 'bird']

if "animal_input" not in st.session_state:
    st.session_state.animal_input = ""

def clear_input():
    st.session_state["animal_input"] = ""

def check_availability(): 
    if st.session_state.animal_input.lower() in animal_shelter:
        st.success('We have that animal!')
    else:
        st.error('We don\'t have that animal.')



st.session_state["animal_input"] = st.text_input('Type an animal', key="animal_input")

check_availability()
clear_input()

