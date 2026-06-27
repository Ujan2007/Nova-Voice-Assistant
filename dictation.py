import keyboard
from speak import speak
from listen import listen

PUNCTUATION = {
    " comma" or "coma": ",",
    " period": ".",
    " full stop": ".",
    " question mark": "?",
    " exclamation mark": "!",
    " colon": ":",
    " semicolon": ";",
    " open bracket": "(",
    " close bracket": ")",
    " open quote": '"',
    " close quote": '"',
    " at the rate": "@",
    " hash": "#",
    " dollar": "$",
    " percent": "%",
    " ampersand": "&"
}


def dictation_mode():

    speak("Dictation mode enabled.")

    while True:

        text = listen().strip().lower()

        if not text:
            continue

        print(text)

        # Exit
        if "stop dictation" in text or "deactivate dictation" in text:
            speak("Dictation mode disabled.")
            break

        # Editing commands
        if text == "delete last word":
            keyboard.send("ctrl+backspace")
            continue

        if text == "delete last character":
            keyboard.send("backspace")
            continue

        if text == "undo":
            keyboard.send("ctrl+z")
            continue

        if text == "select all":
            keyboard.send("ctrl+a")
            continue
        if text == "delete":
            keyboard.send("backspace")
            continue
        if text == "enter":
            keyboard.send("enter")
            continue

        # New line
        if "new line" in text:
            keyboard.press_and_release("shift+enter")
            text = text.replace("new line", "").strip()

        # New paragraph
        if "new paragraph" in text:
            keyboard.press_and_release("enter")
            keyboard.press_and_release("enter")
            text = text.replace("new paragraph", "").strip()

        # Replace spoken punctuation
        for word, symbol in PUNCTUATION.items():
            text = text.replace(word, symbol)

        # Capitalize first letter
        if text:
            text = text[0].upper() + text[1:]

        keyboard.write(text + " ")