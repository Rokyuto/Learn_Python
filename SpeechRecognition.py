import speech_recognition as sr

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Speak Anything : ') 
        r.pause_threshold = 0.6
        audio = r.listen(source)
    
    try:
        text = r.recognize_google(audio)
        print(f"You said : {text}")
    except Exception:
        print("Say that again...")
        return ""

    return text


command()
