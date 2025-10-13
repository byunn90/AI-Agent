import os
from dotenv import load_dotenv
from google import genai
# Load environment variables from .env
load_dotenv()
print("Hello testing")
api_key = os.environ.get("GEMINI_API_KEY")


client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model='gemini-2.5-flash', contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
)
print(response.text)


print("Prompt tokens: 19", response.usage_metadata.prompt_token_count)
print("Response tokens:", response.usage_metadata.candidates_token_count)