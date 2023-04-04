import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import pywhatkit as kit

# initialize the speech recognizer
r = sr.Recognizer()

# initialize the text-to-speech engine
engine = pyttsx3.init()

# define the function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# define the function to listen for voice commands
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        text = r.recognize_google(audio, language='en-in')
        print(f"You said: {text}\n")
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        text = ""
    except sr.RequestError as e:
        print("Request error from Google Speech Recognition service; {0}".format(e))
        text = ""
    return text

# main loop for the voice assistant
while True:
    command = listen().lower()

    if 'hello' in command:
        hour = datetime.datetime.now().hour
        if hour>=0 and hour<12:
            speak("Good Morning!")
        elif hour>=12 and hour<18:
            speak("Good Afternoon!")
        else:
            speak("Good Evening!")
        speak("How can I help you?")

    elif 'open google' in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com/")

    elif 'play music' in command:
        music_dir = 'C:/Users/Public/Music/Sample Music'
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'what is the time' in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")

    elif 'search for' in command:
        search = command.replace('search for', '')
        speak(f"Searching for {search}")
        webbrowser.open(f"https://www.google.com/search?q={search}")

    elif 'send whatsapp message to' in command:
        speak("What is the message?")
        message = listen()
        speak("When should I send the message?")
        time = listen()
        speak(f"Sending message {message} to {command.replace('send whatsapp message to', '')} at {time}")
        kit.sendwhatmsg_instantly(phone_no="+1234567890", message=message, wait_time=10, print_waitTime=True)

    elif 'bye' in command:
        speak("Goodbye!")
        break

    else:
        speak("Sorry, I didn't understand that. Please try again.")
