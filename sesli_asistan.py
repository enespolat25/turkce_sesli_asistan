#%% gerekli kütüphaneler
import os

import speech_recognition as sr

from pydub import AudioSegment
from pydub.playback import play
from gtts import gTTS as tts

#%%
def capture():
    """Capture audio"""

    rec = sr.Recognizer()

    with sr.Microphone() as source:
        print('Dinliyorum...')
        audio = rec.listen(source, phrase_time_limit=5)

    try:
        text = rec.recognize_google(audio, language='tr-TR')
        return text

    except:
        speak('Üzgünüm, Ne söylediğinizi anlayamadım.')
        return 0
def process_text(name, input):
    """Process what is said"""

    speak(name + ', Sen şunu söyledin: "' + input + '".')
    return
def speak(text):
    """Say something"""

    # Write output to console
    print(text)

    # Save audio file
    speech = tts(text=text, lang='tr')
    speech_file = 'input.mp3'
    speech.save(speech_file)

    # Play audio file
    sound = AudioSegment.from_mp3(speech_file)
    play(sound)
    os.remove(speech_file)
#%%
    
    if __name__ == "__main__":
        # First get name
        speak('İsminiz ne?')
        name = capture()
        speak('Merhaba, ' + name + '.')
    # Then just keep listening & responding
    while 1:
        speak('Görüşmenin tamamlanması için ne söylemelisiniz?')
        captured_text = capture().lower()

        if captured_text == 0:
            continue

        if 'bitti' in str(captured_text):
            speak('Tamam, tekrar görüşmek üzere. Selamlar, ' + name + '.')
            break
        # Process captured text
        process_text(name, captured_text)
        
    
