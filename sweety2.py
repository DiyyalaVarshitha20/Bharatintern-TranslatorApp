pip install googletrans==4.0.0-rc1
from googletrans import Translator
 def translate(source_lang, target_lang, text):
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(text, src=source_lang, dest=target_lang)
    return translation.text
 source_language = 'en'  # Example: English
target_language = 'es'  # Example: Spanish
text_to_translate = 'Hello, how are you?'  # Example: Text to be translated

translated_text = translate(source_language, target_language, text_to_translate)
print(f'Translation: {translated_text}')