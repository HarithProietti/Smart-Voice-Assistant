from dotenv import load_dotenv
load_dotenv()

from interface import AudioInterface
from agents import ConversationAgent, SmartChatAgent

interface = AudioInterface()
# agent = ConversationAgent()
agent = SmartChatAgent()

while True: # until we stop, the model will keep listening and answering
    text = interface.listen()  # speech to text
    text = "Please explain me what are LLM agents"
    # print(text)
    response = agent.run(text)  # response of the llm agent to our request
    # text = "Hey how are you?"
    interface.speak(response)  # answer of the llm with an assistant voice