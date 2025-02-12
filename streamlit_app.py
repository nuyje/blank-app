import streamlit as st
if "animal" not in st.session_state:
    st.session_state.animal_input = ""

animal_shelter = ['cat', 'dog', 'rabbit', 'bird']

animal = st.text_input('Type an animal', value=st.session_state.animal_input, key="animal_input")

if st.button('Check availability'):
    have_it = animal.lower() in animal_shelter
    if have_it:
        'We have that animal!' 
        animal = "" 
    else:
        'We don\'t have that animal.'

st.session_state.animal = ""  
st.rerun()  # Herlaad de app om de v