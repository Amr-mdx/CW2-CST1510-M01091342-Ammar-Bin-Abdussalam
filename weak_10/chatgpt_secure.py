from openai import OpenAI
from dotenv import load_dotenv
import os
import sys

# Load environment variables from a .env file (if present)
load_dotenv()

# Read the API key from an env var. Make sure you set OPENAI_API_KEY in your .env
# or in your shell environment. Do NOT hard-code keys in source code.
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("ERROR: OPENAI_API_KEY not set. Add it to your .env or export it in your shell.")
    sys.exit(1)

# Initialize client
client = OpenAI(api_key=api_key)

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
]

print("chatgpt console chat (type 'quit' to exit)")
print("-" * 50)

while True:
    try:
        user_input =st.chat_input("You: ").strip()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye")
        break

    if not user_input:
        continue
    if user_input.lower() == 'quit':
        print("Goodbye")
        break

    messages.append({"role": "user", "content": user_input})

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
    )

    assistant_message = completion.choices[0].message.content
    messages.append({"role": "assistant", "content": assistant_message})
    print(f"AI: {assistant_message}\n")