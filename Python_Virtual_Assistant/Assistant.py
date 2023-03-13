import pyttsx3  # Used by system to speak
import datetime
import speech_recognition as sr  # Used by system to listen
import wikipedia
import webbrowser  # To open web browser
import os  # To execute system programs
import pywhatkit  # To search things on Youtube or Google
import time
import keyboard
import psutil  # For finding process IDs


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour <= 12:
        speak("Good Morning Sir!")

    elif hour > 12 and hour < 18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    speak("My Name is Zero")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print("User Said : ", query)

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def waitALittle():
    time.sleep(2)
    speak("Now I'm on pause, to resume kindly press spacebar")
    while True:
        if keyboard.read_key() == 'space':
            break
    speak("I'm resumed sir, say something")


def docString():
    functionNames = ['wishMe', 'docString', 'presentFeatures']
    functionExplanation = [
        'wish me feature wishes you according to the current time',
        'doc string let you hear the work of specific feature',
        'present features tells you about all the things, I, your assistant can do'
    ]

    print("Which function doc string you want to hear ?")
    speak("Which function doc string you want to hear ?")

    i = 0
    for item in functionNames:
        print(f"{i},", functionNames[i])
        speak(f"{i}{item}")
        i = i + 1

    speak("Enter the choice : ")
    choice = int(input("Enter the choice : "))
    print(functionExplanation[choice])
    speak(functionExplanation[choice])


def close_app(app_name):
    running_apps = psutil.process_iter(['pid', 'name'])
    found = False

    for app in running_apps:
        sys_app = app.info.get('name').split('.')[0].lower()

        if sys_app in app_name.split() or app_name in sys_app:
            pid = app.info.get('pid')

            try:
                app_pid = psutil.Process(pid)
                app_pid.terminate()
                found = True

            except:
                pass

    if not found:
        print(app_name + "Not found running")
        speak(app_name + "Not found running")
    else:
        print(app_name + " closed successfully")
        speak(app_name + " closed successfully")


def presentFeatures():
    speak("I can do several things sir!")
    speak("Do you want me to tell you full list, yes or no?")
    speak("Enter your choice")
    ans = input("Enter your choice\n yes or no?\n").lower()
    if ans == 'yes':
        speak("Do you want to listen the list, view on notepad, or both?")
        speak("Enter your choice")
        ans2 = input(
            "Enter your choice\nlisten, notepad or both?\n").lower()

        if ans2 == 'both':
            file = open('assistant_features.txt', 'r')
            codePath = 'C:\\Users\Bhave\Desktop\My Code\Python Projects\\assistant_features.txt'
            os.startfile(codePath)

            for items in file:
                speak(items)
            file.close()

            speak("Closing notepad...")
            close_app('notepad')
            time.sleep(3)

        if ans2 == 'listen':
            file = open('assistant_features.txt', 'r')
            for items in file:
                speak(items)
            file.close()

        if ans2 == 'notepad':
            file = open('assistant_features.txt', 'r')
            codePath = 'C:\\Users\Bhave\Desktop\My Code\Python Projects\\assistant_features.txt'
            os.startfile(codePath)

    else:
        speak("As you wish sir!")


if __name__ == "__main__":
    wishMe()
    speak("How may I help you sir?")

    while True:
        query = takeCommand().lower()

    # Logic for executing tasks based on query
        if 'wikipedia' in query:
            print("1")
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            print("2")
            webbrowser.open("youtube.com")
            waitALittle()

        elif 'open google' in query:
            print("3")
            webbrowser.open("google.com")
            waitALittle()

        elif 'search' in query:
            print("4")
            command = query.replace('search', '')
            # webbrowser.open(command) # OR Below Line
            pywhatkit.search(command)
            waitALittle()

        elif 'open code' in query:
            print("5")
            codePath = "C:\\Users\\Bhave\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("Opening VS Code Sir")
            os.startfile(codePath)
            waitALittle()

        elif 'time' in query:
            print("6")
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            print(strTime)
            speak("The time is : " + strTime)

        elif 'play on youtube' in query:
            print("7")
            song = query.replace("play on youtube", "")
            pywhatkit.playonyt(song)
            waitALittle()

        elif 'wish me' in query:
            print("8")
            wishMe()

        elif 'who are you' in query:
            print("9")
            speak("My name is zero sir, I'm a virtual assistant")
            speak("Developed by Mr. Rohit")

        elif 'exit' in query:
            print("10")
            speak("Exiting Sir")
            speak("Have a nice day!!!")
            exit()

        elif 'Do you have boyfriend' in query:
            print("11")
            speak("HEHEHE, That's a se-c-re-t")

        elif 'i love you' in query:
            print("12")
            speak("Awwww....., I have a boyfriend dear, sorry!!")

        elif 'what can you do' in query:
            print("13")
            presentFeatures()

        elif 'a second' in query:
            print("13")
            waitALittle()

        elif 'docstring' in query:
            print("14")
            docString()

        elif 'close an app' in query or 'close an application' in query:
            speak("Which app you want to get closed sir ?")
            app_name = takeCommand()

            confirm = "Are you sure you want " + app_name + " to be closed sir?"
            speak(confirm)
            confirmation = takeCommand()

            while 1:
                if confirmation == 'yes':
                    app = app_name.lower()
                    close_app(app)
                    break

                else:
                    speak("Which app you want to get closed sir ?")
                    app_name = takeCommand()
                    confirm = "Are you sure you want " + app_name + " to be closed sir?"
                    speak(confirm)
                    confirmation = takeCommand()

        elif 'thank you' in query:
            speak("You're most welcome sir")
            time.sleep(1)
