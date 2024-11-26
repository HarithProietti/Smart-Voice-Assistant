# Smart-Voice-Assistant

This project aims at developing a vocal assistant that is able to answer questions asked by a user via its microphone. The answer is also provided via a vocal assistant. It uses the speech2text capabilities of the OpenAI whisper model, and the text2speech capabilities of ElevenLabs. To generate the answer, we use an LLM agent with langchain.

## Package requirements

After cloning the repo, please create a new conda environment, and within it install the package requirements, with:

```
pip install -r requirements.txt
```

## Environment variables

Please create an environment file called .env at the root of the project, with a similar structure to the .env.example. You should add your API keys for the different services used (OpenAI, ElevenLabs, Google Search). We provide detail for each service in the following subsections.

### Spech2Text (OpenAI Whisper model)

We use the Whisper API from OpenAI. Please make sure you have a valid OpenAI key added in the .env file, add it like: OPENAI_API_KEY = insert_your_key

### Setup of Eleven Labs (Text2Speech)

For the Text2Speech (answer of the assistant), we use the Eleven Labs services. Please create a free account on the ElevenLabs website: https://elevenlabs.io/. You will then be able to create an API key to use the service, which you should insert in the .env file as: ELEVENLABS_API_KEY = insert_your_key

To be able to play audio from your computer, you need to download ffmpeg on your system.

On MacOS, simply do:

```
brew install ffmpeg
```

### Setup of Google Search

One needs to create a new project on GCP. Once the project is created, click "Select Project" with an API key. Then, click on "API and services", search for "custom search API" in the search bar. You will then be able to add the Custom Search API extension. Then go to the Credentials section, click on "Create credentials", select "API key". It will create an API key that you will be able to use as GOOGLE_API_KEY in the .env file. 

You will also need credentials for the search engine: go to https://programmablesearchengine.google.com/, create a search engine. In the "what to search" section, make sure to select "Search the entire web". In the list of search engines, go to the one you've just created, copy paste the "Search Engine ID", and paste it in the .env file as GOOGLE_CSE_ID.

One should also install the google client on python (google-api-python-client) which has normally already been installed when you installed the requirements.

## Setup of pyaudio

To run the app and allowing your local environment to work with the microphone inputs, you need to install the PyAudio package (cf requirements.txt).

On my mac, to make it work, I had to install portaudio via brew:

```
brew update
brew install portaudio
brew link --overwrite portaudio
```

## Running the project

At the root of the project, please run the following command:

````
python src/app.py
````

You will be prompted "Say something", you can ask your question, and after a few seconds the assistant voice will answer. Note that there is a memory kept during the different exchanges, which means you can have a true discussion with the assistant.
