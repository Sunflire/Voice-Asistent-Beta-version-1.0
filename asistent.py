import webbrowser
import pyttsx3
import speech_recognition as sr


def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Скажите что нибудь: ')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        our_speech = r.recognize_google(audio, language='ru-RU')
        print('Вы сказали:' + our_speech)
        return our_speech
    except sr.UnknownValueError:
        return  'Ошибка'
    except sr.RequestError:
        return 'Ошибка'





def do_this_message(message):
    message = message.lower()
    if 'привет' in message:
        say_message('привет!')
    elif 'как дела' in message:
        say_message('Хорошо')
    elif 'пока' in message:
        say_message('Пока')
        exit()
    elif 'поздравь ярину' in message:
        say_message('Поздравляю тебя ярина')
    elif 'открой браузер' in message:
        say_message('Хорошо, открываю гугл хром')
        webbrowser.open('https://www.google.com/', new=1)
    elif '1' in message:
        say_message('гугл вершина опера пробитая шина')
    elif 'как меня зовут' in message:
        say_message('какаха слона')
    elif 'почему' in message:
        say_message('потому что глист в скафандре хахахахахха')
    elif 'открой карту' in message:
        say_message('Открываю гугл карту')
        webbrowser.open('https://www.google.com./maps/', new=1)
    elif 'открой youTube' in message:
        say_message('Открываю ютуб')
        webbrowser.open('https://www.youtube.com/', new=1)
    else:
        say_message("не очень поняла о чём вы")

# гугл вершина опера пробитая шина





def say_message(message):
    engine.say(message)
    engine.runAndWait()
    print(message)



engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)

while True:
    command = listen_command()
    do_this_message(command)