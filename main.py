from listen import listen
import webbrowser
import subprocess
from rapidfuzz import process
import os 
from speak import speak
import pyautogui
import time
import sys 
import urllib.parse
import winsound
from pathlib import Path
from datetime import datetime
from dictation import dictation_mode
import keyboard
import pygetwindow as gw
# Apps

app_map = {
    # Browsers
    "chrome": "chrome",
    "google chrome": "chrome",

    # Coding
    "vscode": r"C:\Users\ujanb\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk",
    "vs code": r"C:\Users\ujanb\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk",
    "visual studio code": r"C:\Users\ujanb\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk",

    

    # Music
    "spotify": r"C:\Users\ujanb\AppData\Roaming\Spotify\Spotify.exe",

    # Gaming
    "steam": r"C:\Program Files (x86)\Steam\Steam.exe",
    "epic games": r"C:\Program Files\Epic Games\Launcher\Portal\Binaries\Win64\EpicGamesLauncher.exe",

    # Recording
    "obs": r"C:\Program Files\obs-studio\bin\64bit\obs64.exe",
    "obs studio": r"C:\Program Files\obs-studio\bin\64bit\obs64.exe",

    # Office
    "excel": "excel",
    "word": "winwrd",
    "powerpoint": "powerpnt",

    # Utilities
    "notepad": "notepad",
    "calculator": "calc",
    "cmd": "cmd",
    "terminal": "wt",
    "whatsapp": r"C:\Users\ujanb\OneDrive\Desktop\WhatsApp - Shortcut.lnk",
    # AI
    "chatgpt app": "OpenAI.ChatGPT-Desktop_2p2nqsd0c76g0!ChatGPT"
}


# Websites
sites = {
    "youtube": "https://youtube.com",
    "github": "https://github.com",
    "chatgpt": "https://chatgpt.com",
    "gmail": "https://mail.google.com",
    "reddit": "https://reddit.com",
    "reels": "https://www.instagram.com/reels",
    "instagram": "https://www.instagram.com/"
}

WAKE_BY_KEY = False

def wake_up():
    global WAKE_BY_KEY
    WAKE_BY_KEY = True

keyboard.add_hotkey("f8", wake_up)

def open_app(app_name):

    match = process.extractOne(
        app_name,
        app_map.keys()
    )

    if not match:
        
        speak("App not found")
        return

    best_match = match[0]
    score = match[1]

    if score < 60:
        speak("No close match found")
        return

    target = app_map[best_match]

    if "spotify" not in app_name:
        speak(f"Opening {best_match}")

    try:
        # exe path
        if target.endswith(".exe")or target.endswith(".lnk"):
            os.startfile(target)

        # command/app id
        else:
            subprocess.run(
                ["cmd", "/c", "start", "", target],
                shell=True
            )

    except Exception as e:
        speak(f"Error: {e}")


WAKE_WORDS = [
    "hey nova",
    "nov",
    "hey rova",
    "hova",
    "hey lova",
    "gova",
    "hello",
    "talk",
    "wake",
    "wake up"
    
]
ACTIVE_MODE = False
REELS_MODE = False
CONTINUOUS_MODE = False
speak("nova Online")






while True:

    try:

        if REELS_MODE:

            command = listen().strip().lower()

            if not command:
                continue

            print("Reels:", command)

            if command in ["exit reels mode", "stop reels mode", "deactivate"]:
                speak("Exiting reels mode.")
                REELS_MODE = False
                ACTIVE_MODE = False
                continue

            if "down" in command or "next" in command:
                pyautogui.scroll(-700)
                continue

            if "up" in command or "previous" in command:
                pyautogui.scroll(700)
                continue

        


        
        # CONTINUOUS MODE
        
        elif CONTINUOUS_MODE:

            command = listen().strip().lower()

            if not command:
                continue

            print("Command:", command)

            if command in ["exit continuous mode", "deactivate"]:
                speak("Continuous mode disabled.")
                CONTINUOUS_MODE = False
                ACTIVE_MODE = False
                continue


        
        # SLEEP MODE
        
        elif not ACTIVE_MODE:




                # Keyboard wake-up
            if WAKE_BY_KEY:

                WAKE_BY_KEY = False

                winsound.Beep(900, 200)

                ACTIVE_MODE = True

                continue

            wake_text = listen().strip()

            if not wake_text:
                continue

            print("Heard:", wake_text)

            if wake_text in [
                "go away",
                "bye nova",
                "shutdown nova",
                "shutdown",
                "fuck off"
            ]:
                speak("Goodbye!")
                break

            match = process.extractOne(
                wake_text,
                WAKE_WORDS
            )

            if not match or match[1] < 70:
                continue

            winsound.Beep(900, 500)

            ACTIVE_MODE = True

            continue


        
        # NORMAL ACTIVE MODE
        
        else:

            time.sleep(0.3)

            command = listen().strip().lower()

            if not command:

                print("Waiting for another command...")

                command = listen().strip().lower()

                if not command:
                    ACTIVE_MODE = False
                    print("Nova sleeping...")
                    continue

            print("Command:", command)



        # Spotify
        if command.startswith("play "):

            query = command.replace("play", "", 1).strip()
            
            speak(f"Playing {query} on spotify")
            



            open_app("spotify")

            
            start = time.time()

            while time.time() - start < 10:

                windows = gw.getWindowsWithTitle("Spotify")

                if windows:
                    spotify = windows[0]

                    if spotify.isMinimized:
                        spotify.restore()

                    spotify.activate()

                    break

                time.sleep(0.2)

            time.sleep(0.3)

            pyautogui.hotkey("ctrl", "l")

            time.sleep(0.2)

            pyautogui.write(query, interval=0.02)

            time.sleep(0.2)

            pyautogui.press("tab")

            time.sleep(1)

            pyautogui.press("down")

            time.sleep(0.1)

            pyautogui.press("enter")

            
            



            
        # Scroll up
        elif "scroll up" in command:

            

            pyautogui.scroll(700)


        # Scroll down
        elif "scroll down" in command:

            

            pyautogui.scroll(-700)
        elif "down" in command:
            pyautogui.press("down")
        elif "up" in command:
            pyautogui.press("up")
        # Screenshot
        elif "screenshot" in command:
            downloads = Path.home() / "Downloads"

            filename = downloads / f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"

            pyautogui.screenshot(str(filename))

            speak("Screenshot taken and saved in downloads folder.")

        elif "continuous" in command or "activate continuous" in command:
            print("ENTERED CONTINUOUS MODE")

            speak("continuous mode On")
            CONTINUOUS_MODE = True

        # dictation mode 
        elif "dicatation" in command or "activate dictation" in command:
            dictation_mode()
        # YouTube
        elif command.startswith("open youtube and search"):

            query = command.replace(
                "open youtube and search",
                "",
                1
            ).strip()
            
            speak(f"Searching YouTube for {query}")

            query = urllib.parse.quote(query)

            webbrowser.open(
                f"https://www.youtube.com/results?search_query={query}"
            )

        # WhatsApp
        elif command.startswith("send "):

            parts = command.rsplit(" to ", 1)

            if len(parts) != 2:
                speak("Please say send hello to papa")
                continue

            message = parts[0].replace(
                "send",
                "",
                1
            ).strip()

            person = parts[1].strip()

            speak(f"Sending your message to {person}")

            open_app("whatsapp")

            time.sleep(2)

            pyautogui.hotkey("ctrl", "f")
            pyautogui.write(person)

            time.sleep(0.5)

            pyautogui.press("enter")

            time.sleep(0.5)

            pyautogui.write(
                message,
                interval=0.03
            )

            pyautogui.press("enter")

        # Google Search
        elif command.startswith("search "):

            query = command.replace(
                "search",
                "",
                1
            ).strip()
            #speak("Get to work iris")
            speak(f"Searching for {query}")

            query = urllib.parse.quote(query)

            webbrowser.open(
                f"https://www.google.com/search?q={query}"
            )

        # Open
        elif command.startswith("open") or "reels" in command or "reels mode" in command:
            

            if "reels" in command:
                target = "reels"
                speak("reels mode activated")
                REELS_MODE = True
            else:
                target = command.replace(
                    "open",
                    "",
                    1
                ).strip()

            if target in sites:
                #speak("Get to work iris")
                speak(f"Opening {target}")

                webbrowser.open(
                    sites[target]
                )

            else:
                
                open_app(target)


        else:

            speak("Command not recognised")

    except Exception as e:
        print(e)
        speak(f"Critical Error: {e}")

    