import datetime
import random
import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 170)  # Speaking speed

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id) 

# Function to make bot speak
def speak(text):
    print(f"Bot: {text}")
    engine.say(text)
    engine.runAndWait()

# Function to listen from microphone
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)  # Reduces background noise
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I could not understand.")
        return ""
    except sr.RequestError:
        speak("Sorry, speech recognition service is unavailable.")
        return ""

# Chatbot function
def chatbot():
    jokes = [
        "Why don't skeletons fight each other? They don't have the guts.",
        "I'm reading a book about anti-gravity. It's impossible to put down!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!"
    ]
    
    speak("Hello! I'm your chatbot. Say 'exit' to quit.")
    
    while True:
        user_input = listen()
        
        if "exit" in user_input:
            speak("Goodbye! 👋")
            break
        elif "date" in user_input:
            today = datetime.date.today()
            speak(f"Today's date is {today}")
        elif "time" in user_input:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {now}")
        elif "joke" in user_input:
            speak(random.choice(jokes))
        else:
            speak("Sorry, I don't understand that. Try asking for 'date', 'time', or 'joke'.")

# Run chatbot
chatbot()
