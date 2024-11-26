# Smart-Voice-Assistant

## Setup of pyaudio

To run the app, you need to install the PyAudio package (cf requirements.txt).

On my mac, to make it work, I had to install portaudio via brew:

```
brew update
brew install portaudio
brew link --overwrite portaudio
```

## Setup of Eleven Labs

To be able to play audio from your computer, you need to download ffmpeg.

On mac, simply do:

```
brew install ffmpeg
```

## Spech2Text

We use the Whisper API from openai

## Text2Speech

We use the ElevenLabs API.
