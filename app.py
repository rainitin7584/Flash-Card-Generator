import streamlit as st
from app.generator import generate_flashcards

st.set_page_config(page_title="AI Flashcard Generator", page_icon="🧠", layout="centered")

st.title("🧠 AI Flashcard Generator")
st.caption("Generate study flashcards using a Hugging Face model.")

text = st.text_area(
    "Paste your study notes or topic",
    height=220,
    placeholder="Example: Explain CPU scheduling, FCFS, SJF, Round Robin..."
)

col1, col2 = st.columns(2)
with col1:
    count = st.slider("Number of cards", 3, 15, 5)
with col2:
    difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])

if st.button("✨ Generate Flashcards", use_container_width=True):
    if not text.strip():
        st.warning("Please enter a topic or some notes.")
    else:
        with st.spinner("Generating flashcards..."):
            try:
                cards = generate_flashcards(text, count, difficulty)
                st.session_state["cards"] = cards
            except Exception as e:
                st.error(f"Generation failed: {e}")

cards = st.session_state.get("cards", [])

if cards:
    st.divider()
    st.subheader("Your Flashcards")

    for i, card in enumerate(cards, 1):
        with st.expander(f"Card {i}: {card.get('question', 'Question')}"):
            st.markdown("### Question")
            st.write(card.get("question", ""))
            st.markdown("### Answer")
            st.write(card.get("answer", ""))
            st.caption(f"Difficulty: {card.get('difficulty', difficulty)}")
