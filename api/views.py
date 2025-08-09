from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

from api.translator import translate_by_genai

@csrf_exempt
def index(request):
    if request.method == 'POST':
        request_data = json.loads(request.body.decode('utf-8'))
        data = request_data['events'][0]
        textToTranslate = data['text']
        print("Received text to translate: ", textToTranslate)
        try:
            translated_messages = translate_by_genai(textToTranslate)
        except Exception as e:
            print("Error translating text: ", e)
            translated_messages = [{'type': 'text', 'text': 'Error translating text. Please try again.'}]
        print("Translated text: ", translated_messages)
        return HttpResponse(json.dumps(translated_messages), content_type='application/json')