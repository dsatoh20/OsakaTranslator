from google import genai
from google.genai import types

def create_genai_message(message):
    client = genai.Client()
    response = client.models.generate_content(
        model = "gemini-1.5-flash",
        contents = message,
        config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0) # Disables thinking
    ),
    )
    return response.text


def create_single_text_message(message):
    if message == 'ありがとう':
        message = 'どういたしまして！'
    test_message = [
                {
                    'type': 'text',
                    'text': message
                }
            ]
    return test_message

