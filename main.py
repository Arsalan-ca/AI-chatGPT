import speech_recognition as sr
import openai
import pyttsx3

situation = True

openai.api_key = ""
model_engine = "text-davinci-003"

## this is text to speech
text_speech = pyttsx3.init()


## writing the voice recognizer

def voice():
    print("Say something...")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        command = r.recognize_google(audio)
        command = command.lower()
    return command


def chat_answer():
    command = voice()
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=command,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    response = completion.choices[0].text
    print(response)
    text_speech.say(response)
    text_speech.runAndWait()


while situation:
    chat_answer()
