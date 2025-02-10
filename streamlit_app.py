import streamlit as st
import random

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.write("Hello world") 

# Functie om een willekeurige oefening te genereren
def generate_question():
    a = random.randint(1, 12)
    b = random.randint(1, 12)
    return a, b, a * b

# Initialiseer sessievariabelen
if "score" not in st.session_state:
    st.session_state.score = 0
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "current_question" not in st.session_state:
    st.session_state.current_question = generate_question()

st.title("🧮 Tafels van Vermenigvuldiging Trainer")

a, b, correct_answer = st.session_state.current_question
st.write(f"**Wat is {a} × {b}?**")

# Invoer voor antwoord
user_answer = st.text_input("Jouw antwoord:", value="", key="answer", help="Typ hier je antwoord en druk op Enter.")

# Controleer het antwoord
if user_answer:
    try:
        user_answer = int(user_answer)
        st.session_state.attempts += 1
        
        if user_answer == correct_answer:
            st.success("✅ Correct!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Fout! Het juiste antwoord is {correct_answer}.")
        
        # Genereer een nieuwe vraag
        st.session_state.current_question = generate_question()
        st.experimental_rerun()

    except ValueError:
        st.warning("⚠️ Voer een geldig getal in.")

# Score tonen
st.write(f"**Score:** {st.session_state.score} / {st.session_state.attempts}")
