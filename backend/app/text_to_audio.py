"""
تحويل نص إلى ملف صوت MP3 باستخدام Google Text-to-Speech (gTTS).
يدعم العربية الفصحى، الدارجة المغربية (رمزيًا)، والإنجليزية.
"""

from gtts import gTTS
import os

# خريطة الرموز اللغوية
LANG_MAP = {
    "ar": "ar",       # العربية الفصحى
    "ar-ma": "ar",    # الدارجة المغربية (نستخدم صوت العربية الفصحى بديلًا)
    "en": "en",       # الإنجليزية
}

def text_to_audio(
    script: str,
    lang: str = "ar",
    output_path: str = "static/output_audio.mp3"
) -> str:
    """
    يُحوّل نص إلى صوت MP3 ويحفظه في المسار المحدد.

    Args:
        script (str): النص المراد تحويله.
        lang (str): اللغة ('ar', 'ar-ma', 'en').
        output_path (str): المسار الذي سيتم حفظ ملف الصوت فيه.

    Returns:
        str: مسار ملف الصوت الناتج.
    """
    # تأكد من اللغة المدعومة
    selected_lang = LANG_MAP.get(lang.lower(), "en")

    # تحويل النص إلى صوت
    tts = gTTS(text=script, lang=selected_lang)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    tts.save(output_path)
    return output_path
