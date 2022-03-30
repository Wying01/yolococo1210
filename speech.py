import speech_recognition as sr  # 導入語音辨識模組 記得先去cmd安裝更新模組跟python
import pyttsx3
import detect01C

r = sr.Recognizer()
engine = pyttsx3.init()

def intro(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def take_order():
    try:
        with sr.Microphone() as source:  # 麥克風開啟(電腦內建)
            r.adjust_for_ambient_noise(source)  # 減少雜音(精準度有待確認)
            cmd = 0
            print('speak something：')
            audio = r.listen(source, phrase_time_limit=10)  # 語音辨識範圍，接收5秒內的input
            cmd = r.recognize_google(audio, language='en-us')# 選擇google模組，將剛說的話轉成zh-TW 繁體中文/en-US 美國英文的字串
            cmd = cmd.lower()
    except:
        pass
    return cmd

def run():
    cmd = take_order()
    list = ["wrench", "tweezer", "cut", "knife", "close"]
    if list[0] in cmd:
        intro(list[0])
        run()
    if list[1] in cmd:
        intro(list[1])
        run()
    if list[2] in cmd:
        intro(list[2])
        run()
    if list[3] in cmd:
        intro(list[3])
        run()
    if list[4] in cmd:
        intro(list[4])
        close()
    else:
        intro("not in list,please try again")
        run()

def detect():
    print("0")
    cmd = take_order()
    if "robot" in cmd:
        intro("what do you want to do")
        run()
    else:
        intro("please try again")
        detect()

def close():
    print("1")
    detect01C.shut()

#記得下載pip install pywhatkit，解鎖上網功能等等
#pip install flask
#Chinese (Taiwan)	zh-tw
#English (United States)	en-us
#Japanese	ja
#Korean	ko