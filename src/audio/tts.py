import pyttsx3

engine = pyttsx3.init()
def say(phrase):
    engine.say(phrase)
    print("Said :",phrase)
    engine.runAndWait()
