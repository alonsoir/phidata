import io

from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat
from dotenv import load_dotenv

load_dotenv()

code = io.FileIO('../agents/agent.py').read().decode('utf-8')
refactor_assistant = Assistant(
    llm=OpenAIChat(model="gpt-4o"),
    description="You help people with their refactor needs of code goals.",
    instructions=["I have a code that needs refactoring. "
                  "Can you provide suggestions to improve its readability and efficiency? Here is the code: {code}"],
)
# -*- Print a response to the cli
refactor_assistant.print_response(f"Refactor this code:\n{code}", markdown=True)
