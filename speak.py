import edge_tts
import asyncio
import pygame
import tempfile
import os


pygame.mixer.init()

VOICE = "en-US-JennyNeural"

# PRE-RECORDED HOMELANDER LINES
SOUNDS = {
    #"goodbye!": "sounds/goodbye2.mp3",
    #"opening youtube": "sounds/opening-youtube.mp3",

    #"homelander is online": "sounds/homelander-is-online.mp3",
    #"playing your song on spotify": "sounds/spotify2.mp3",
    #"sending your message, because apparently your fingers are too precious": "sounds/message.mp3",
   # "i cant understand you, speak like a normal human for fucks sake!": "sounds/understand.mp3",
   # "get to work iris" : "sounds/iris.mp3",
    #"you heard him iris": "sounds/heardhim.mp3"
}


def play_sound(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


async def _generate_speech(text, filename):
    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE
    )

    await communicate.save(filename)


def speak(text):

    print(f"Assistant: {text}")

    key = text.lower().strip()

    # Use prerecorded audio if available
    if key in SOUNDS and os.path.exists(SOUNDS[key]):
        play_sound(SOUNDS[key])
        return

    # Otherwise use Edge TTS
    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".mp3"
    )

    temp_path = temp_file.name
    temp_file.close()

    asyncio.run(
        _generate_speech(
            text,
            temp_path
        )
    )

    pygame.mixer.music.load(temp_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove(temp_path)