from googletrans import Translator

translator = Translator()

def translate_to_english(text):
    result = translator.translate(text, dest="en")
    return result.text, result.src   # translated text + detected language

def translate_back(text, target_lang):
    return translator.translate(text, dest=target_lang).text
