import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I didn't get that.")
        return ""
    except sr.RequestError as e:
        print(f"Sorry, an error occurred: {e}")
        return ""

def play_music(genre):
    # Add your code to play music based on the genre (e.g., pop, energetic dance) here
    print(f"Now playing {genre} music...")

if __name__ == "__main__":
    speak("Hello, I'm your voice assistant. How can I help you?")

    while True:
        query = listen().lower()

        if "hello" in query:
            speak("Hi there! How can I assist you today?")
        elif "goodbye" in query or "bye" in query:
            speak("Goodbye! Have a great day!")
            break
        elif "play music" in query:
            speak("Which type of songs do you want to listen?")
            genre_query = listen().lower()
            if "upbeat" in genre_query or "energetic" in genre_query:
                speak("How about some pop or energetic dance music? I can queue up a playlist with artists like Devi Sri Prasad, Thaman, etc.")
                speak("Enjoy your music.")
                play_music("energetic")
            else:
                speak("Sorry, I'm not sure which genre you want to listen to.")
        elif "increase volume" in query:
            speak("Sure. Enjoy the music. Just let me know if you need to change the music or playlist at any point.")
            # Add code to increase volume here
        else:
            speak("Sorry, I'm not sure how to help with that.")

