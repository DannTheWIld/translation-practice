import streamlit as st
import random

# Define words
english_words = ["Acquire", "Amateur", "Argument", "Faith", "Calendar", "Category", "Cemetery", "Changeable", "Collectibles", "Column", "Commitment", "Conscience", "Conscious", "Definite", "Discipline", "Solid", "Equipment", "Exaggerate", "Excellent", "Existence", "Experience", "Foreign", "Friend", "Grammar", "Harass", "Height", "Independence", "Indispensable", "Intelligence", "Jewelry", "Review", "Knowledge", "Contact", "License", "Maintenance", "Maneuver", "Millennium", "Misspelling", "Necessary", "Noticeable", "Occasion", "Preferred", "Endurance", "Privilege", "Public", "Receive", "Recommend"]

swedish_words = ["Få", "Amatör", "Argument", "Tro", "Kalender", "Kategori", "Kyrkogård", "Föränderlig", "Samlarobjekt", "Kolumn", "Engagemang", "Samvete", "Medveten", "Definitivt", "Disciplin", "Gensamt", "Utrustning", "Överdriva", "Utmärkt", "Existens", "Erfarenhet", "Utländsk", "Vän", "Grammatik", "Trakassera", "Höjd", "Oberoende", "Oumbärlig", "Intelligens", "Smycken", "Omdöme", "Kunskap", "Kontakt", "Licens", "Underhåll", "Manöver", "Millennium", "Felstavning", "Nödvändigt", "Märkbart", "Tillfälle", "Föredragen", "Uthållighet", "Privilegium", "Offentligt", "Ta emot", "Rekommendera"]

# Initialize session state variables
if "restart" not in st.session_state:
    st.session_state.restart = False

if "random_order" not in st.session_state:
    st.session_state.random_order = False

st.title("Swedish to English Translation Game")

# Difficulty slider
difficulty = st.slider("Select Difficulty (1 = Longest, 10 = Shortest)", 1, 10, 5)
num_words = max(1, len(english_words) // difficulty)
st.write(f"Translate {num_words} words!")

# Random order toggle
st.session_state.random_order = st.checkbox("Randomize word order", st.session_state.random_order)

# Restart game logic
if "words" not in st.session_state or st.session_state.restart:
    words = list(zip(english_words, swedish_words))
    if st.session_state.random_order:
        random.shuffle(words)
    st.session_state.words = words[:num_words]
    st.session_state.current_word_index = 0
    st.session_state.points = 0
    st.session_state.finished = False
    st.session_state.restart = False  # Reset restart flag

# Get the current word
if not st.session_state.finished:
    eWord, sWord = st.session_state.words[st.session_state.current_word_index]
    st.subheader(f"Translate: {sWord}")

    user_input = st.text_input("Your answer:", "")
    submit = st.button("Submit")
    next_button = st.button("Next")

    if submit:
        if user_input.lower() == eWord.lower():
            st.session_state.points += 1
            st.success("✅ Correct!")
        else:
            st.error(f"❌ Incorrect! Expected: {eWord}")

    # Move to the next word when "Next" is clicked
    if next_button:
        if st.session_state.current_word_index + 1 < num_words:
            st.session_state.current_word_index += 1
        else:
            st.session_state.finished = True

# Show final results
if st.session_state.finished:
    st.write(f"🎉 Game over! You scored {st.session_state.points} out of {num_words}")

# Restart button
if st.button("Restart"):
    st.session_state.restart = True
    st.rerun()
