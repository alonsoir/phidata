from dotenv import load_dotenv

from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat

load_dotenv()

error_message = ""
troubleshooting_assistant = Assistant(
    llm=OpenAIChat(model="gpt-4o"),
    description="You help people with their refactor needs of code goals.",
    instructions=["I’m encountering an error message {error_message} in my code. Can you help me troubleshoot and find a solution?"],
)
# -*- Print a response to the cli
troubleshooting_assistant.print_response(f"help me with my code, this is the error i found:\n{error_message}", markdown=True)
