import streamlit as st

animal_shelter = ['cat', 'dog', 'rabbit', 'bird']

animal = st.text_input('Type an animal')

if st.button('Check availability'):
    have_it = animal.lower() in animal_shelter
    if have_it:
        'We have that animal!' 
        animal = "" 
    else:
        'We don\'t have that animal.'
