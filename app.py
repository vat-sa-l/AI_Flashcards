import streamlit as st
from utils import extract_text_from_pdf, generate_flashcards

st.set_page_config(page_title="AI Flashcards", layout="centered")

st.title("AI Flashcards Generator")
st.write("Upload your notes or paste text to generate AI-powered flashcards.")


input_type = st.radio("Choose input type:", ["Upload PDF", "Paste Text"])

notes_text = ""

if input_type == "Upload PDF":
    uploaded_file = st.file_uploader("Upload PDF notes", type=["pdf"])
    if uploaded_file:
        with st.spinner("Extracting text from PDF..."):
            notes_text = extract_text_from_pdf(uploaded_file)
else:
    notes_text = st.text_area("Paste your notes here", height=250)

num_cards = st.slider("Number of flashcards", 5, 20, 10)

if st.button("Generate Flashcards"):
    if notes_text.strip() == "":
        st.warning("Please provide notes first.")
    else:
        with st.spinner("Generating flashcards using AI..."):
            flashcards_text = generate_flashcards(notes_text, num_cards)

        flashcards = flashcards_text.split("\n\n")

        st.subheader(" Generated Flashcards")

        for card in flashcards:
            if "Q:" in card and "A:" in card:
                q, a = card.split("A:")
                with st.expander(q.replace("Q:", "").strip()):
                    st.write(a.strip())
