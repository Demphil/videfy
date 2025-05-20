# app/tts.py

from gtts import gTTS
from io import BytesIO


def text_to_speech(text: str, lang: str = "ar") -> bytes:
    """
    يحول النص إلى صوت باستخدام gTTS ويعيده كـ bytes.
    :param text: النص الذي تريد تحويله
    :param lang: لغة الصوت ('ar'، 'en'، 'fr'...)
    :return: الصوت بصيغة mp3 كـ bytes
    """
    try:
        tts = gTTS(text=text, lang=lang)
        audio_bytes = BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)
        return audio_bytes.read()
    except Exception as e:
        raise RuntimeError(f"TTS Error: {str(e)}")
