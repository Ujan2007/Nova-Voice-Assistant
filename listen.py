import speech_recognition as sr

recognizer = sr.Recognizer()

recognizer.pause_threshold = 0.7
recognizer.non_speaking_duration = 0.4

mic = sr.Microphone()
import time

last_calibration = time.time()
def recalibrate():

    global last_calibration

    with mic as source:
        print("Recalibrating...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

    last_calibration = time.time()

if time.time() - last_calibration > 180:   # 3 minutes
    recalibrate()

print("Calibrating microphone...")

with mic as source:
    recognizer.adjust_for_ambient_noise(source, duration=2)



def listen():

    with mic as source:
        print("listenting..")

        try:
            audio = recognizer.listen(
                source,
                timeout=2.5,
                phrase_time_limit=6
            )

        except sr.WaitTimeoutError:
            return ""

    try:
        text = recognizer.recognize_google(audio)
        return text.lower()

    except sr.UnknownValueError:
        return ""

    except Exception as e:
        print(e)
        return ""