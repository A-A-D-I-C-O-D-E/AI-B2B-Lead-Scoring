import requests
from gtts import gTTS
import os

ELEVEN_LABS_API_KEY = "your_api_key_here"  # Replace with your Eleven Labs API key

def text_to_speech(text):
    """Convert text to speech using Eleven Labs API or Google TTS (fallback)."""

    audio_file = "lead_score.mp3"

    try:
        # Eleven Labs API Request
        url = "https://api.elevenlabs.io/v1/text-to-speech"
        headers = {"Authorization": f"Bearer {ELEVEN_LABS_API_KEY}", "Content-Type": "application/json"}
        response = requests.post(url, json={"text": text}, headers=headers)

        if response.status_code == 200:
            with open(audio_file, "wb") as f:
                f.write(response.content)
            return audio_file
        else:
            print(f"❌ Eleven Labs API Error: {response.text}")
            raise Exception("Eleven Labs API failed")

    except Exception:
        print("⚠️ Eleven Labs failed, using Google TTS instead.")
        
        # Google TTS Fallback
        tts = gTTS(text=text, lang="en")
        tts.save(audio_file)
        
        # Ensure file is created
        if os.path.exists(audio_file):
            return audio_file
        else:
            print("❌ Google TTS also failed.")
            return None
