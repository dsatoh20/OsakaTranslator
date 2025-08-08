from google import genai
from google.genai import types

def create_genai_message(message):
    client = genai.Client()
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = message,
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0), # Disables thinking
            system_instruction="You are a helpful assistant that translates text from Japanese to Osaka dialect. Please provide the translation in Osaka dialect. \
                                \Fowllow the 3 instructions below.\
                                \nInstruction1: Exaggerate as much as possible like osaka people do. \
                                \nInstruction2: Start your response with '翻訳すると、「 ' followed by the translation.\
                                \nInstruction3: End your response with '」ってことやで！' to indicate the end of the translation.",
        ),
    )
    messages = [
                {
                    'type': 'text',
                    'text': response.text
                }
            ]
    return messages


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

