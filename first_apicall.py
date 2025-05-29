import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("Error: GEMINI_API_KEY not found in .env file.")
    exit(1)

# Configure Gemini
genai.configure(api_key=api_key)

# Get user input
user_input = input("Enter your question: ")

# Initialize Gemini model
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# Start chat
chat = model.start_chat()

# Send user prompt and get response
response = chat.send_message(user_input)

# Print formatted assistant response
print("\n🤖 Assistant's Response:\n")
print(response.text)

# Show token usage if available
if hasattr(response, 'usage_metadata'):
    usage = response.usage_metadata
    print("\n📊 Token Usage:")
    print(f"Prompt Tokens: {usage.prompt_token_count}")
    print(f"Response Tokens: {usage.candidates_token_count}")
    print(f"Total Tokens: {usage.total_token_count}")
else:
    print("\nToken usage data not available.")
