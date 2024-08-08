import pyttsx3

player = pyttsx3.init()
player.say("Hello everyone! This is my mini RoboSpeaker project, built using the Python library pyttsx3. The goal of this project is to convert text into speech, creating a basic text-to-speech application that can speak any text input")
player.runAndWait()
print("WELCOME TO ROBOSPEAKER")

while True:
    x = input("Enter what you want to speak (or type 'exit' to quit): ")
    if x.lower() == 'exit':
        player.say(" Exiting the RoboSpeaker")
        player.runAndWait()
        break
    player.say(x)
    player.runAndWait()


