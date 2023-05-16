import calendar
import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("good morning sir")
    elif hour >= 12 and hour<= 18:
        speak("good afternoon sir")
    elif hour>= 18 and hour <21:
        speak("good evening sir")
    else:
        speak("good night sir")

def takecommand():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("[+] LISTENING ... ")
        r.pause_threshold = 0
        r.energy_threshold = 10
        audio = sr.Recognizer().listen(source)
    
    try:
        print("[+] RECOGNIZING ...")
        query = r.recognize_google(audio, language='en-in')
        print(f"blackdevil:~ {query}\n")

    except Exception as e:
        speak("say that again please !")
        return "None"

    return query


def track_location():
    address = input("Enter address: ")

    geolocator = Nominatim(user_agent="location_tracker")
    location = geolocator.geocode(address)

    if location is not None:
        print(f"Latitude: {location.latitude}, Longitude: {location.longitude}")
    else:
        print("Location not found.")

def calender_ai():
    year = int(input("Enter the year: "))
    month = int(input("Enter the month: "))
    print(calendar.month(year, month))

if __name__ == "__main__":
    wishme()
    calender_ai()
    while True:
        query = takecommand().lower()
        
        if "track a location" in query:
            track_location()
            
        elif "jarvis quit" in query:
            break