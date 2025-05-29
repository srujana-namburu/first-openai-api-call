# first-openai-api-call

# 🤖 First OpenAI API Call using Gemini (Google Generative AI)

This is a simple Python script that interacts with Google's **Gemini API** (Generative AI) to provide responses to user prompts. The script is designed to:

- Take a prompt as input from the user
- Send it to the Gemini model (`gemini-1.5-flash-latest`)
- Return the assistant’s response
- Display token usage statistics for prompt and response

---

## 📦 Dependencies

Before running the script, ensure you have the following Python packages installed:

`bash
pip install google-generativeai python-dotenv
git clone https://github.com/srujana-namburu/first-openai-api-call.git
cd first-openai-api-call`

### Create a .env file in the root directory and add your Gemini API key:
GEMINI_API_KEY=your_google_generative_ai_key_here

How to Run
Execute the Python script:

python first_apicall.py

Example
Enter your question: what is national animal of india

🤖 Assistant's Response:
The national animal of India is the Bengal tiger.

📊 Token Usage:
Prompt Tokens: 18
Response Tokens: 11
Total Tokens: 29


