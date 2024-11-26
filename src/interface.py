import speech_recognition as  sr
import os
from elevenlabs import play
from elevenlabs.client import ElevenLabs


class AudioInterface:

    def listen(self) -> str:
        # listens to the microphone and translates it to text
        recognizer = sr.Recognizer()
        with sr.Microphone(device_index=1) as source:
            print("Say something")
            audio = recognizer.listen(source)

        text = recognizer.recognize_whisper_api(
            audio,
            api_key=os.environ['OPENAI_API_KEY']
        )

        return text

    def speak(self, text):
        # takes as input a text and speaks with the assistant voice
        client = ElevenLabs(
            api_key=os.environ['ELEVENLABS_API_KEY']

        )
        # response = client.voices.get_all()
        # print(response.voices) # available voices
        audio = client.generate(
            text=text,
            voice='Brian',
            model='eleven_monolingual_v1'
        )
        
        play(audio)