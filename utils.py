from PyPDF2 import PdfReader
import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
print(os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")



def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text


def generate_flashcards(notes, num_cards=10):
    model = genai.GenerativeModel("gemini-2.5-flash")


    prompt = f"""
    You are an AI tutor.

    Convert the following study notes into {num_cards} flashcards.

    Rules:
    - Each flashcard must have a Question and an Answer
    - Keep answers short and clear
    - Focus on exam-relevant concepts

    Output format:
    Q: question
    A: answer

    Notes:
    {notes}
    """

    response = model.generate_content(prompt)
    return response.text
