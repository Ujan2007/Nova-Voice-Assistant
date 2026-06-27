# 🎙️ Nova - AI Voice Assistant

Nova is a desktop voice assistant built in Python that lets you control your computer using natural voice commands. It combines speech recognition, text-to-speech, desktop automation, and intelligent command handling to create a fast, hands-free desktop experience.

> 🚧 This project is currently under active development.

---

Note - If you have a poor quality mic then Nova may struggle to understand your wake word. Press the **F8** key in that case.

## ✨ Features

### 🎤 Voice Activation
- Wake Nova by saying **"Hey Nova"** or **"Talk Nova"**
- Wake Nova instantly using the **F8** key
- Fuzzy wake-word detection for improved recognition
- Audible confirmation beep

---

### 💻 Open Applications

Launch desktop applications with your voice by saying : "Open {app name}"

Supported apps include:

- Chrome
- VS Code
- Spotify
- Steam
- Epic Games Launcher
- OBS Studio
- WhatsApp
- Calculator
- Terminal
- Command Prompt
- ChatGPT Desktop
- All MS Office applications

You can make nova open any app by just adding its path in the "app_path" dictionary in the main file.

Example:

```
Open Chrome
```

---

### 🌐 Open Websites

Open websites instantly by saying : "Open {site name}"

Supported websites:

- YouTube
- GitHub
- Gmail
- Reddit
- Instagram
- Instagram Reels

make nova open any site by just adding its url in the "sites" dictionary in the main file.

Example:

```
Open YouTube
```

---

### 🔎 Google Search

Search anything directly from your voice.

Example:

```
Search best machine learning roadmap
```

---

### ▶️ Spotify Control

Play music completely hands-free by saying "Play {song info}"

Example:

```
Play Blinding Lights
```

Nova automatically:

- Opens Spotify
- Focuses the search box
- Searches for the song
- Starts playback

---

### 📺 YouTube Search

Example:

```
Open YouTube and search Interstellar soundtrack
```

---

### 💬 WhatsApp Messaging

Send messages using your voice.
Note - You must have whatsapp installed on your machine.

Example:

```
Send I'll be there in ten minutes to John
```

Nova automatically:

- Opens WhatsApp
- Finds the contact
- Types the message
- Sends it

---

### 📸 Screenshot

Take screenshots instantly.

Example:

```
Take a screenshot
```

Screenshots are automatically saved to the **Downloads** folder.

---

### 🖱️ Scroll Control

Navigate pages using your voice.

Commands:

- Scroll up
- Scroll down

---

## 🎞️ Reels Mode

A dedicated mode for browsing Instagram Reels or YouTube Shorts.

Activate:

```
Reels mode
```

Commands:

- Down
- Up
- Next
- Previous
- Exit reels mode

No wake word is required while Reels Mode is active.

---

## ♾️ Continuous Mode

Activate:

```
Continuous mode
```

Nova stays awake and continuously accepts commands without requiring the wake word after every interaction.

Exit using:

```
Exit continuous mode
```

---

## 📝 Dictation Mode

Convert speech directly into text.

Works in:

- Notepad
- VS Code
- Microsoft Word
- Chrome
- Discord
- Any text field

Supported commands:

- New line
- New paragraph
- Comma
- Period
- Question mark
- Delete last word
- Undo
- Stop dictation

---

## 🔊 Voice Responses

Nova uses Microsoft's Edge Neural TTS for realistic speech synthesis.

Support for custom prerecorded voice responses is also available.

---

# 🛠 Built With

- Python
- SpeechRecognition
- Edge-TTS
- PyAutoGUI
- RapidFuzz
- Keyboard
- PyGetWindow
- Pygame
- Winsound

---

# 📂 Project Structure

```
Nova/
│
├── main.py
├── listen.py
├── speak.py
├── dictation.py
├── sounds/
└── README.md
```

---

# 🚀 Planned Features

- AI Conversation Mode (LLM)
- Email Assistant
- File Search
- Clipboard Manager
- OCR
- Screen Understanding
- Local AI Support
- Front end dashboard for Nova

---

# 📸 Demo

*(Coming Soon)*

---

# 👨‍💻 Author

**Ujan**

A personal project built to explore speech recognition, desktop automation, and artificial intelligence.
