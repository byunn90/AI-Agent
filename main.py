import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.call_function import call_function
from functions.available_functions import available_functions
load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
is_verbose = "--verbose" in sys.argv

if len(sys.argv) < 2:
    print("Error: Please provide a prompt.")
    sys.exit(1)

prompt = sys.argv[1]
system_prompt = """
You are a helpful AI coding agent.

When a user asks about how the code works or to fix/inspect something,
DO NOT ask for clarification first. Instead:
1) Call get_files_info to see what's in the directory.
2) Then call get_file_content on the most relevant files (e.g., main.py).
3) Only after inspecting files should you answer or proceed to run/write.

You can perform the following operations:
- List files and directories (get_files_info)
- Read file contents (get_file_content)
- Execute Python files with optional arguments (run_python_file)
- Write or overwrite files (write_file)

Rules:
- All paths are relative to the working directory (which will be injected).
- If asked to create/save/generate content, use write_file directly:
  - Default directory: "."
  - Default file name: "notes.txt"
  - Default file format: .txt
  - After writing, display its contents with get_file_content.

Be decisive. Prefer acting with tools over asking questions.
"""
client = genai.Client(api_key=api_key)

config = types.GenerateContentConfig(
    tools=[available_functions],
    system_instruction=system_prompt,
)

response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=prompt,
    config=config
)
found_fc = False
for part in response.candidates[0].content.parts:
    fc = getattr(part, "function_call", None)
    if fc:
        found_fc = True
        tool_msg = call_function(fc, verbose=is_verbose)
        payload = tool_msg.parts[0].function_response.response
        print("✅ payload:", payload)

if not found_fc:
    raise RuntimeError("❌ No function_call found in Gemini response")


prompt_tokens = response.usage_metadata.prompt_token_count
response_tokens = response.usage_metadata.candidates_token_count



if is_verbose:
    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {response_tokens}")
    print(f"response: {response.text}")

def generate_content():
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)])
    ]

    config = types.GenerateContentConfig(
        tools=[available_functions],
        system_instruction=system_prompt,
    )

    try:
        for i in range(20):
            content_catcher = client.models.generate_content(
                model="gemini-2.0-flash-001",
                contents=messages,
                config=config
            )

            model_msg = content_catcher.candidates[0].content
            messages.append(model_msg)

            found_fc = False
            for part in model_msg.parts:
                fc = getattr(part, "function_call", None)
                if fc:
                    tool_msg = call_function(fc, verbose=is_verbose)
                    messages.append(tool_msg)
                    found_fc = True
                    break          

            if found_fc:
                continue


            print(content_catcher.text)
            return


        print("⚠️ Reached 20 iterations—stopping.")
        return

    except Exception as e:
        print(f"❌ Agent error: {e}")
        return





    

print(generate_content())

