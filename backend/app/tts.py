from gtts import gTTS

def text_to_speech(text, filename="output.mp3", lang="ar"):
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)
    return filename
