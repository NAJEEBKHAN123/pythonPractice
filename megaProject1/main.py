import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    print(f"Processing command: {c}")
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.faceboo.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.faceboo.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.faceboo.com")
    elif "exit" in c.lower():
        speak("Goodbye!")
        exit()

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)

            word = recognizer.recognize_google(audio)
            print(f"Heard: {word}")

            if word.lower() == 'jarvis':
                speak('Yes?')
                with sr.Microphone() as source:
                    print("Jarvis Active... Listening for command.")
                    audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio)
                print(f"Command: {command}")
                processCommand(command)

        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError:
            print("Speech recognition service error.")
        except Exception as e:
            print(f"Error: {e}")
