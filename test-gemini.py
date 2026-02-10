import google.generativeai as genai

genai.configure(api_key="GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-2.5-flash")

response = model.generate_content(
    "Say hello in one sentence",
    request_options={"timeout": 120}
)

print(response.text)
