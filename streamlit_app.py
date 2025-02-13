import streamlit as st

animal_shelter = ['cat', 'dog', 'rabbit', 'bird']

animal = st.text_input('Type an animal', key="animal_input")

def clear_input():
    st.session_state["animal_input"] = ""

st.button("clear text input", on_click=clear_input)
st.write(input)

if st.button('Check availability'):
    if st.session_state.animal_input.lower() in animal_shelter:
        st.success('We have that animal!')
    else:
        st.error('We don\'t have that animal.')

clear_input()

