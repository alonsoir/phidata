from dotenv import load_dotenv

from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat

load_dotenv()

insert_functionality_or_task = "data manipulation with python using pandas"

"""
    This is a good prompt to generate a starter code pack. But be sure not just to copy the code and use it,
    be cautious with the code generated by LLMs as they contain security flaws and bugs as well.
"""
library_recommendations_assistant = Assistant(
    llm=OpenAIChat(model="gpt-4o"),
    description="You help people with their programming needs of code goals.",
    instructions=[
        f"I need a code snippet for {insert_functionality_or_task}. Can you generate a sample code snippet?"
    ],
)
# -*- Print a response to the cli
library_recommendations_assistant.print_response(
    f"please help the best you can me with this functionality:{insert_functionality_or_task}, "
    f"provide me the best sample you can using this technology or concept: {insert_functionality_or_task}.",
    markdown=True,
)
