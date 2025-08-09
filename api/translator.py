from google import genai
from google.genai import types

def translate_by_genai(textToTranslate):
    client = genai.Client()
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = textToTranslate,
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0), # Disables thinking
            system_instruction="You are a helpful assistant that translates text from Japanese to Osaka dialect. Please provide the translation in Osaka dialect. \
                                \Fowllow the 2 instructions below.\
                                \nInstruction1: If a message is osaka dialect, return as it is.\
                                \nInstruction2: Exaggerate as osaka people do. (Most IMPORTANT)",
        ),
    )
    messages = [
                {
                    'type': 'text',
                    'text': response.text
                }
            ]
    return messages