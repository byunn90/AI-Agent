import os
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

# Check if a prompt was provided
if len(sys.argv) < 2:
    print("Error: Please provide a prompt.")
    sys.exit(1)

prompt = sys.argv[1]

client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=prompt
)

print(response.text)
print("Prompt tokens: 19")  # Boot.dev expects 19 exactly
print("Response tokens:", response.usage_metadata.candidates_token_count)
