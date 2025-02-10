import streamlit as st
import random

# Functie om een willekeurige oefening te genereren
def generate_question():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    return a, b, a * b

# Initialiseer sessievariabelen
if "score" not in st.session_state:
    st.session_state.score = 0
if "attempts" not in st.session_state:
    st.session_state.attempts = 0


st.title("🧮 Tafels van Vermenigvuldiging Trainer")

a, b, correct_answer = generate_question()
st.write(f"**Wat is {a} × {b}?**")

# Invoer voor antwoord met sessievariabele
user_answer = st.text_input(
    "Jouw antwoord:",
    value="",
    key="answer",
    help="Typ hier je antwoord en druk op Enter."
)

# Controleer het antwoord

try:
        user_answer = int(user_answer)
        st.session_state.attempts += 1
        
        if user_answer == correct_answer:
            st.success("✅ Correct!")
            st.session_state.score += 1
            user_answer = ""
            
        else:
            st.error(f"❌ Fout! Het juiste antwoord is {correct_answer}.")

        # Reset de invoer en genereer een nieuwe vraag
        
        

except ValueError:
        st.warning("⚠️ Voer een geldig getal in.")

# Score tonen
st.write(f"**Score:** {st.session_state.score} / {st.session_state.attempts}")
