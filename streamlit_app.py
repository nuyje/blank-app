import streamlit as st

# Sessievariabele voor inputveld initialiseren
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# Functie om invoerveld leeg te maken
def clear_input():
    st.session_state.user_input = ""
    st.rerun()

st.title("📝 Test Input Reset")

# Tekstveld met sessievariabele
user_input = st.text_input("Typ iets:", value=st.session_state.user_input, key="input_field")

# Knop om invoerveld te resetten
if st.button("Verzend"):
    if user_input:
        st.success(f"Je invoer: {user_input}")
        clear_input()  # Leegmaken en herladen
    else:
        st.warning("Voer eerst iets in.")
