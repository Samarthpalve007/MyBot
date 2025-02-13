from transformers import pipeline

def translate_text(text, src="en", dest="hi"):
    """Translates text using Hugging Face's M2M100 model."""
    # Load Hugging Face model for translation
    translator = pipeline("translation", model="facebook/m2m100_418M")
    
    # Translate the text
    result = translator(text, src_lang=src, tgt_lang=dest)
    
    return result[0]['translation_text']

# Example Usage
if __name__ == "__main__":
    print(translate_text("Hello, how are you?", "en", "hi"))
